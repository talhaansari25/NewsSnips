from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from app.search import *
from app.api import *
from app.summary import *
from app.feed import *
from app.recommendation import *
from app.category import *
from app.random import *