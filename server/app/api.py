from flask import Flask, request, jsonify
from app import app
from .search import searchText
from .summary import getSummary
from .recommendation import myRec
from .category import myCategory
from .feed import get_all
from .random import getRandomNews
from flask_cors import CORS


# app = Flask(__name__)

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


@app.route('/all', methods = ['GET'])
def all_api():
    newsList = get_all()
    return jsonify({'output': newsList})

@app.route('/random', methods = ['POST'])
def random_api():
    data = request.get_json()
    randomList = getRandomNews(data['random'])
    # return newsList
    return jsonify({'output': randomList})


# @app.route('/category', methods=['POST'])
# def get_cat():
#     try:
#         # Get the JSON payload from the request
#         data = request.get_json()

#         # Ensure 'catList' is present in the request
#         if 'catList' not in data:
#             return jsonify({'error': 'catList not provided in the request body'}), 400

#         # Call the myCategory function from the imported file
#         getCat = myCategory(data['catList'])

#         # Return the response as JSON
#         return jsonify({'output': getCat}), 200

#     except Exception as e:
#         # Return any exception message with 500 error
#         return jsonify({'error': str(e)}), 500

# if __name__ == '__main__':
#     app.run(debug=True)