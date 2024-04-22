from flask import Flask
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
import os

load_dotenv(find_dotenv(), override=True)

def create_app():
    app = Flask(__name__)
    db_url = os.getenv("DB_URL")
    app.config["ENBINE"] = create_engine(db_url, echo=True)
    
    return app