import os
from flask import Flask
from dotenv import load_dotenv
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

def create_connection():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )