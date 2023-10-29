import json,requests
import os
from dotenv import load_dotenv

load_dotenv()
# Get the JSON response for Gurugram
gurugram_response = requests.get(f"https://api.airvisual.com/v2/nearest_city?key={os.getenv('API_KEY')}&city=Gurugram")
gurugram_data = gurugram_response.json()

# Get the city name, country, and current AQI
city_name = gurugram_data["data"]["city"]
country = gurugram_data["data"]["country"]
current_aqi = gurugram_data["data"]["current"]["pollution"]["aqicn"]

# Print the data
print(f"City name: {city_name}")
print(f"Country: {country}")
print(f"Current AQI: {current_aqi}")
