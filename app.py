'''simple website to check AQI'''
import os
from dotenv import load_dotenv
from flask import Flask
import requests

load_dotenv()


# from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """API calling here"""
    response = requests.get(f"https://api.airvisual.com/v2/nearest_city?key={os.getenv('API_KEY')}")
    return response.json()

if __name__ == "__main__":
    app.run(debug=True) 


    """https://dev.to/bluepaperbirds/get-all-keys-and-values-from-json-object-in-python-1b2d visit this website"""