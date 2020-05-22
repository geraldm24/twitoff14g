
# web_app/__init__.py
import os
import sys
from dotenv import load_dotenv
from flask import Flask

from web_app2.routes.models import db, migrate
#from web_app.routes.admin_routes import admin_routes
from web_app2.routes.home_routes import home_routes
from web_app2.routes.book_routes import book_routes
from web_app2.routes.twitter_routes import twitter_routes
from web_app2.routes.stats_routes import stats_routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

def create_app():
    app = Flask(__name__)
    #app.config["SECRET_KEY"] = SECRET_KEY # required for flash messaging

    # configure the database:
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    migrate.init_app(app, db)

    # configure routes:
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(twitter_routes)
    #app.register_blueprint(admin_routes)
    app.register_blueprint(stats_routes)

    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)
  