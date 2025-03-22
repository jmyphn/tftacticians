import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
import numpy as np

from helpers.utils import (champions_lower_dict, tokenize, recommend_k_next_champions)

k = 5 # Number of champions to recommend

# ROOT_PATH for linking with all your files.
# Feel free to use a config.py or settings.py with a global export variable
os.environ["ROOT_PATH"] = os.path.abspath(os.path.join("..", os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
LOCAL_MYSQL_USER = "root"
LOCAL_MYSQL_USER_PASSWORD = "admin"
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

# Sample search, the LIKE operator in this case is hard-coded,
# but if you decide to use SQLAlchemy ORM framework,
# there's a much better and cleaner way to do this
def sql_search_champions(champions):
    champion_info = []
    for champion in champions:
        query_sql = f"""SELECT * FROM champ_info WHERE LOWER( name ) LIKE '%%{champion.lower()}%%' limit 1"""
        result = mysql_engine.query_selector(query_sql)
        keys = ["name", "cost", "traits"]
        champion_info = champion_info + [dict(zip(keys, row)) for row in result]
    
    # trait info
    keys = ["name", "description"]
    for champion in champion_info:
        # Split the traits string into a list
        traits = champion["traits"].split(",")
        # Remove any leading/trailing whitespace from each trait
        traits = [trait.strip() for trait in traits]
        champion["traits"] = []
        for trait in traits:
            print(trait)
            query_sql = f"""SELECT * FROM trait_info WHERE LOWER( name ) LIKE '%%{trait.lower()}%%' limit 1"""
            result = mysql_engine.query_selector(query_sql)
            
            trait_info = [dict(zip(keys, row)) for row in result]
            if len(trait_info) > 0:
                champion["traits"].append(trait_info[0])
            else:
                champion["traits"].append({"name": trait, "description": "No description found."})
    print(champion_info)
    # Convert the champion_info list to JSON
    # and return it as a response
    res = json.dumps(champion_info)
    print(res)
    return res


@app.route("/")
def home():
    return render_template("base.html", title="TFTacticians")


@app.route("/champions")
def champions_search():
    text = request.args.get("query")
    tokenized_text = tokenize(text)

    # now we find the champions in the text that the user queried.
    # TODO: we can probably use text similarity to find the closest match
    # to the champions in the database (using edit distance metrics)
    champions_to_find = []
    for token in tokenized_text:
        if token in champions_lower_dict:
            champions_to_find.append(token.lower())
    if len(champions_to_find) == 0:
        return json.dumps([])
    
    champions_csv = ",".join(champions_to_find)

    # get the recommended units for the user's comp
    recommended_champions = recommend_k_next_champions(champions_csv, k)

    # return recommended champions
    return sql_search_champions(recommended_champions)


if "DB_NAME" not in os.environ:
    app.run(debug=True, host="0.0.0.0", port=5000)
