from flask import Flask
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456789",
    database="db_share_location"
)

