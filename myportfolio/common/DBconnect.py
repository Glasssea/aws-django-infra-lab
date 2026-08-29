import pandas as pd
import mysql.connector
import os, json
from pathlib import Path
from django.core.exceptions import ImproperlyConfigured
from sqlalchemy import create_engine

# 서버 오픈하고 한 번만 하면 되는 파일임

with open('secrets.json') as f:
    secrets = json.load(f)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = secrets["SECRET_KEY"]
db_username = secrets['db_username']
db_password = secrets['db_password']


df = pd.read_csv('sunny/common/mastery.csv')

conn = mysql.connector.connect(
    host='127.0.0.1',
    user=db_username,
    password=db_password,
    database='portfolio'
)
engine = create_engine(f"mysql+mysqlconnector://{db_username}:{db_password}@127.0.0.1/portfolio")
df.to_sql('search_mastery', con=engine, if_exists='replace', index=False)

