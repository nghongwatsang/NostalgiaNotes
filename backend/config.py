from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flast_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLAlCHEMY_DATABASE_URI'] = "sqlite:///mydatabase.db"
app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlcehmy(app)