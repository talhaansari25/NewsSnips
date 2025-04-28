
from app import app

if __name__ == "__main__":
    app.run(debug=True, port=5000)

# For Vercel to recognize the app
def handler(environ, start_response):
    return app(environ, start_response)