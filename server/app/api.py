from flask import request, jsonify
from app import app
from .search import searchText
from .summary import getSummary
from .recommendation import myRec
from .category import myCategory
from .feed import get_all
from .random import getRandomNews
from flask_cors import CORS

CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

@app.route('/search', methods=['POST'])
def get_search():
    data = request.get_json()
    searched_data = searchText(data['query'])
    return jsonify({'output': searched_data})

@app.route('/summary', methods=['POST'])
def get_summary():
    data = request.get_json()
    getSum = getSummary(data.get('bigText', ''))
    return jsonify({'output': getSum})

@app.route('/recommendation', methods=['POST'])
def get_recc():
    data = request.get_json()
    getRec = myRec(data['keys'])
    return jsonify({'output': getRec})

@app.route('/category', methods=['POST'])
def get_cat():
    data = request.get_json()
    getCat = myCategory(data['catList'])
    return jsonify({'output': getCat})

@app.route('/all', methods=['GET'])
def all_api():
    newsList = get_all()
    return jsonify({'output': newsList})

@app.route('/random', methods=['POST'])
def random_api():
    data = request.get_json()
    randomList = getRandomNews(data['random'])
    return jsonify({'output': randomList})
