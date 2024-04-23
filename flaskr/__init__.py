from flask import Flask
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
import os

load_dotenv(find_dotenv(), override=True)

def create_app():
    app = Flask(__name__)
    #db_url = "sqlite:///data.db"
    #app.config["ENGINE"] = create_engine(db_url, echo=True)
    return app
