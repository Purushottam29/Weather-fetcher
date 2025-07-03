import requests
import csv
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        print(f"Weather in {city}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")

        # Save to CSV
        with open("weather.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["City", "Description", "Temperature (°C)", "Humidity (%)"])
            writer.writerow([city, weather_desc, temp, humidity])

    else:
        print("API Error:", response.status_code, response.text)

if __name__ == "__main__":
    city_name = input("Enter a city: ")
    get_weather(city_name)

