# Weather Fetcher 

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

```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   venv\Scripts\activate     # On Windows
```
Install dependencies
```bash
pip install -r requirements.txt
```
Setup environment variables
Create a .env file in the root folder:
env
```bash
WEATHER_API_KEY=your_openweathermap_api_key_here
```
Run the script
```bash
python weather.py
```
Example
```yaml
Enter a city: Delhi
Weather in Delhi:
Description: overcast clouds
Temperature: 31.35°C
Humidity: 76%
```
The weather data will be saved to weather.csv.


