from flask import Flask
import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    response = requests.get("https://api.airvisual.com/v2/nearest_city?key=1589f34c-b54c-4647-bfe3-ecef91f56e17")
    return response.json()

if __name__ == "__main__":
    app.run(debug=True) 