'''simple website to check AQI'''
from flask import Flask
import requests

# from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """API calling here"""
    response = requests.get("https://api.airvisual.com/v2/nearest_city?key=1589f34c-b54c-4647-bfe3-ecef91f56e17")
    return response.json()

if __name__ == "__main__":
    app.run(debug=True) 


    """https://dev.to/bluepaperbirds/get-all-keys-and-values-from-json-object-in-python-1b2d visit this website"""