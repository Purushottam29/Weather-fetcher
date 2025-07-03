# Weather Fetcher 🌦️

A simple Python script that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features

- Fetches current weather description, temperature (°C), and humidity.
- Saves the fetched data to a CSV file.
- Uses environment variables for API key security.

## Setup

1. **Clone the repo**

   ```bash
   git clone git@github.com:yourusername/weather-fetcher.git
   cd weather-fetcher
Create a virtual environment (optional but recommended)

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Linux/Mac
venv\Scripts\activate     # On Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Setup environment variables

Create a .env file in the root folder:

env
Copy
Edit
WEATHER_API_KEY=your_openweathermap_api_key_here
Run the script

bash
Copy
Edit
python weather.py
Example
yaml
Copy
Edit
Enter a city: London
Weather in London:
Description: light rain
Temperature: 16°C
Humidity: 82%
The weather data will be saved to weather.csv.


