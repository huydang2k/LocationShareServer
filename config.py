from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1o0n720@@localhost/db_share_location'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
