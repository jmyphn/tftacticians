import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
import numpy as np
from dotenv import load_dotenv
from helpers.utils import (
    champions_lower_dict,
    tokenize,
    recommend_champions,
    combined_champions,
)
from helpers.svd import SVDSearcher

# load env variables from .env file
load_dotenv()

k = 5  # Number of champions to recommend

# ROOT_PATH for linking with all your files.
# Feel free to use a config.py or settings.py with a global export variable
os.environ["ROOT_PATH"] = os.path.abspath(os.path.join("..", os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
LOCAL_MYSQL_USER = "root"
LOCAL_MYSQL_USER_PASSWORD = (
    os.getenv("DB_PASSWORD")
    if (os.getenv("DB_PASSWORD") != None or os.getenv("DB_PASSWORD") != "")
    else "admin"
)
LOCAL_MYSQL_PORT = 3306
LOCAL_MYSQL_DATABASE = "tftacticians"

mysql_engine = MySQLDatabaseHandler(
    LOCAL_MYSQL_USER, LOCAL_MYSQL_USER_PASSWORD, LOCAL_MYSQL_PORT, LOCAL_MYSQL_DATABASE
)

# Path to init.sql file. This file can be replaced with your own file for testing on localhost, but do NOT move the init.sql file
mysql_engine.load_file_into_db()

app = Flask(__name__)
CORS(app)

"""
Schemas

champ_info {
    name VARCHAR(64) PRIMARY KEY,
    cost INT,
    traits VARCHAR(256)
};

trait_info {
    name VARCHAR(64) PRIMARY KEY,
    description VARCHAR(256)
}
"""
champion_descriptions = combined_champions
svd_searcher = SVDSearcher(champion_descriptions)


# Sample search, the LIKE operator in this case is hard-coded,
# but if you decide to use SQLAlchemy ORM framework,
# there's a much better and cleaner way to do this
def sql_search_champions(champions, scores):
    champion_info = []
    for champion in champions:
        # Get the champion info from the database
        query_sql = f"""SELECT * FROM champ_info WHERE LOWER( name ) LIKE "%%{champion.lower()}%%" limit 1"""
        champion_result = mysql_engine.query_selector(query_sql)

        # find 5 other champions that can be paired with this champion based on
        # co-occurrence matrix
        champion_scores = recommend_champions(champion)
        champion_scores = np.argsort(champion_scores)[::-1][:k]
        champion_scores = [combined_champions[i] for i in champion_scores]
        best_5_champions_for_this_champion = [
            x.split(":")[0].strip() for x in champion_scores
        ]
        print(best_5_champions_for_this_champion)
        best_5_champions_for_this_champion_info = []

        for other_champion in best_5_champions_for_this_champion:
            query_sql = f"""SELECT * FROM champ_info WHERE LOWER( name ) LIKE "%%{other_champion.lower()}%%" limit 1"""
            other_champion_result = mysql_engine.query_selector(query_sql)
            keys = ["name", "traits"]
            best_5_champions_for_this_champion_info = (
                best_5_champions_for_this_champion_info
                + [dict(zip(keys, row)) for row in other_champion_result]
            )
        print(champion_result.mappings().all())
        to_add = {
            "name": champion,
            "traits": (
                "No traits found." 
                if (not champion_result or len(champion_result.mappings().all()) == 0)
                else champion_result.mappings().all()[0]["traits"]
            ),
            "tags": svd_searcher.get_tags(champion, top_n=5),
            "best_5_champions": best_5_champions_for_this_champion_info,
        }
        # print(to_add)
        champion_info.append(to_add)
    # print(champion_info)
    # trait info
    keys = ["name", "description"]
    for champion in champion_info:
        # Split the traits string into a list
        traits = champion["traits"].split(",")
        # Remove any leading/trailing whitespace from each trait
        traits = [trait.strip() for trait in traits]
        champion["traits"] = []
        for trait in traits:
            query_sql = f"""SELECT * FROM trait_info WHERE LOWER( name ) LIKE '%%{trait.lower()}%%' limit 1"""
            result = mysql_engine.query_selector(query_sql)

            trait_info = [dict(zip(keys, row)) for row in result]
            if len(trait_info) > 0:
                champion["traits"].append(trait_info[0])
            else:
                champion["traits"].append(
                    {"name": trait, "description": "No description found."}
                )

    # score computation for star rating for each champion
    print(scores)
    top_score = scores[0]
    for i, score in enumerate(scores):
        champion_info[i]["score"] = (
            round(score * 5 / top_score, 3) if top_score > 0 else 0
        )

    print(champion_info)
    res = json.dumps(champion_info)
    # print(res)
    return res


@app.route("/")
def home():
    return render_template("base.html", title="TFTacticians")


@app.route("/champions")
def champions_search():

    query = request.args.get("query", "")
    # TODO: cho'gath not being tokenized properly, need to fix
    svd_results_all_champions = svd_searcher.search(query)
    svd_results_all_champions = np.array(svd_results_all_champions).flatten()

    tokenized_text = tokenize(query)

    # now we find the champions in the text that the user queried.
    # TODO: we can probably use text similarity to find the closest match
    # to the champions in the database (using edit distance metrics)
    champions_to_find = []
    for token in tokenized_text:
        print(token)
        if token.lower() in champions_lower_dict:
            print(f"Found champion: {token.lower()}")
            champions_to_find.append(token.lower())

    champions_csv = ",".join(champions_to_find)

    # get the recommended units for the user's comp
    recommended_champions = recommend_champions(champions_csv)

    # linear combination between the svd results and the recommended champions
    # print(svd_results_all_champions)
    # print("-"*20)
    # print(recommended_champions)
    find_champions = 0.5 * svd_results_all_champions + 0.5 * recommended_champions
    scores = np.sort(find_champions)[::-1][:k]
    find_champions = np.argsort(find_champions)[::-1][:k]
    find_champions = [combined_champions[i] for i in find_champions]
    find_champions = [x.split(":")[0].strip() for x in find_champions]
    for champion in find_champions:
        print(champion)

    # return recommended champions
    return sql_search_champions(find_champions, scores)


@app.route("/champion-lore")
def champion_lore():
    from flask import jsonify
    from static.lore import tft_champions

    champion_name = request.args.get("name", "")

    normalized_name = champion_name.strip()

    lore = "No lore available."
    for key, value in tft_champions.items():
        if key.lower() == normalized_name.lower():
            lore = value
            break

    return jsonify({"name": champion_name, "lore": lore})


if "DB_NAME" not in os.environ:
    app.run(debug=True, host="0.0.0.0", port=5000)
