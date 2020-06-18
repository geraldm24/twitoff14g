# twitoff
## Installation
Install packages
dev-packages]

[packages]
flask = "*"
flask-sqlalchemy = "*"
flask-migrate = "*"
basilica = "*"
tweepy = "*"
python-dotenv = "*"
requests = "*"
scikit-learn = {extras = ["alldeps"],version = "*"}
scipy = "*"
matplotlib = "*"
gunicorn = "*"
psycopg2-binary = "*"

[requires]
python_version = "3.7"

## Setup
set up a pipeline for files to link to one another
check out documentation
[flask](https://flask.palletsprojects.com/en/1.1.x/)

Migrate the db:

```sh
On windows
set FLASK_APP=web_app2 flask db init
set FLASK_APP=web_app2 flask db migrate
set FLASK_APP=web_app2 flask db upgrade

Deploy ro heroku
create a postgres account
under addons
add database credentials to your postgressql I used Tableplus
download heroku cli
the run heroku run bash
FLASK_APP=web_app2 flask db init
FLASK_APP=web_app2 flask db migrate
FLASK_APP=web_app2 flask db upgrade``

## Usage

```sh
Insert a twitter handle to enter into the database 
```
