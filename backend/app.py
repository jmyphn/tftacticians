import json
import os
from flask import Flask, render_template, request
from flask_cors import CORS
from helpers.MySQLDatabaseHandler import MySQLDatabaseHandler
import numpy as np

from helpers.utils import load_comatrices
from helpers.utils import (champions_lower_dict, tokenize, recommend_k_next_champions)

k = 5 # Number of champions to recommend

# ROOT_PATH for linking with all your files.
# Feel free to use a config.py or settings.py with a global export variable
os.environ["ROOT_PATH"] = os.path.abspath(os.path.join("..", os.curdir))

# These are the DB credentials for your OWN MySQL
# Don't worry about the deployment credentials, those are fixed
# You can use a different DB name if you want to
LOCAL_MYSQL_USER = "root"
LOCAL_MYSQL_USER_PASSWORD = "hiimjimmy6782"
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
def sql_search(name):
    query_sql = f"""SELECT * FROM champ_info WHERE LOWER( name ) LIKE '%%{name.lower()}%%' limit 1"""
    keys = ["name", "cost", "traits"]
    data = mysql_engine.query_selector(query_sql)[0]

    # find the description of the traits
    traits_desc = []
    for trait in data[2].split(","):
        trait_query = f"""SELECT description FROM trait_info WHERE LOWER( name ) LIKE '%%{trait.lower()}%%' limit 1"""
        trait_desc = mysql_engine.query_selector(trait_query)
        if trait_desc:
            traits_desc.append(trait_desc.fetchone()[0])
    
    return json.dumps(dict(zip(keys, i)) for i in data) + json.dumps({"traits_desc": traits_desc})


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

    # get the champion info for each recommended champion
    recommended_champions_info = []
    for champion in recommended_champions:
        champion_info = sql_search(champion)
        if champion_info:
            recommended_champions_info.append(json.loads(champion_info)[0])
    # return the recommended champions and the user's comp
    return json.dumps({
        "recommended_champions_names" : recommended_champions,
    })


if "DB_NAME" not in os.environ:
    app.run(debug=True, host="0.0.0.0", port=5000)

