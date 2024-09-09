import requests
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://mongo:27017/")
db = client.weather_db
weather_collection = db.weather

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'Please provide a city name'}), 400

    # Check if the weather data is already in the database
    weather_data = weather_collection.find_one({"city": city})
    if weather_data:
        return jsonify(weather_data)

    # If not, fetch from the API
    api_key = "your_openweathermap_api_key"
    api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    
    if response.status_code != 200:
        return jsonify({'error': 'Could not fetch weather data'}), response.status_code

    weather_data = response.json()
    weather_info = {
        "city": city,
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"]
    }

    # Store the data in MongoDB
    weather_collection.insert_one(weather_info)

    return jsonify(weather_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
