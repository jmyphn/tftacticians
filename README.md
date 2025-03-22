# TFTacticians
Recommending team compositions (...for Set 3)!
## File structure
```
.
├── README.md
├── SETUP.md
├── __init__.py
├── backend
│   ├── app.py
│   ├── data
│   │   ├── comatrix.npy
│   │   └── comatrix_normalized.npy
│   ├── env
│   │   └── environment files
│   ├── helpers
│   │   ├── MySQLDatabaseHandler.py
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── MySQLDatabaseHandler.cpython-312.pyc
│   │   │   ├── __init__.cpython-312.pyc
│   │   │   └── utils.cpython-312.pyc
│   │   └── utils.py
│   ├── model.py
│   ├── requirements.txt
│   ├── static
│   │   ├── images
│   │   │   ├── mag.png
│   │   │   └── search.png
│   │   └── style.css
│   └── templates
│       └── base.html
├── data_processing
│   └── tft_data_processing.ipynb
└── init.sql
```

## Summary
This is the repository for **TFTacticians**, a project being created for [*CS/INFO 4300 at Cornell University*](https://4300-hall-of-fame.infosci.cornell.edu/) for Spring 2025.

Currently, the app only supports recommendations with Set 3 champions as input.

## Setting up locally

You will need to have `python` version 3.10 or above. You will also need to have MySQL set up locally (specifically, you need [MySQL Community Server](https://dev.mysql.com/downloads/mysql/)) to execute the commands in the `init.sql` file locally. Optionally, you can use [MySQL Workbench](https://dev.mysql.com/downloads/workbench/) as an alternative to the command-line interface.

### Setting up environment variables
In the root directory, create a `.env` file. Inside, include the following:
```
DB_PASSWORD = <your local mysql server password here>
```

### Setting up the virtual environment
You can setup the virtual environment from the command line. Navigate to the root directory of this project and run the following command:
```bash
python -m venv <your virtual environment name here>
```

### Installing required packages
You can install the requirements by running
```bash
python -m pip install -r backend/requirements.txt
```

### Running the application
From the `backend/` directory, run
```bash
flask run --host=0.0.0.0 --port=5000
```
You can then access the app from `localhost`.

## Credits
This project was created using [a template created for CS/INFO 4300 at Cornell University](https://github.com/CornellNLP/4300-Flask-Template-SQL). We thank everyone who helped put this template together.

We also used a public [Kaggle dataset](https://www.kaggle.com/datasets/gyejr95/tft-match-data/data?select=TFT_Platinum_MatchData.csv) for Set 3 matches. We also plan to query high-elo ranked games for the current set (13) via the [Riot's Developer API](https://developer.riotgames.com/apis#tft-match-v1).

TFTacticians was created under Riot Games' "Legal Jibber Jabber" policy using assets owned by Riot Games. Riot Games does not endorse or sponsor this project.