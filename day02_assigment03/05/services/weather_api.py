# weather_api.py

import requests

# --- Configuration ---
# IMPORTANT: Replace this with your actual, active OpenWeatherMap API key
# If this key is wrong or inactive, you will still get errors (401 or 404).
API_KEY = "4893805586e199fdf05ac6ae16e5d413" 
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    """
    Fetches current weather data for a given city from OpenWeatherMap.
    Returns a dictionary of cleaned weather data or None on failure.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Get temperature in Celsius
    }

    try:
        # Send the GET request to the OpenWeatherMap API
        response = requests.get(BASE_URL, params=params)
        
        # raise_for_status() checks for bad HTTP response codes (4xx or 5xx)
        # This is where your previous error (400) would be caught gracefully
        response.raise_for_status() 
        
        data = response.json()
        
        # Extract and return only the necessary, cleaned data
        return {
            'city': data.get('name'),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'].capitalize(),
            'wind_speed': data['wind']['speed']
        }

    except requests.exceptions.HTTPError as e:
        # Handles errors like 401 (Bad Key) or 404 (City Not Found)
        status_code = e.response.status_code
        if status_code == 401:
            print(f"Error 401: Invalid or inactive API key. Please check your key.")
        elif status_code == 404:
            print(f"Error 404: City not found.")
        else:
            print(f"HTTP Error: {status_code} - {e}")
        return None
        
    except requests.exceptions.RequestException as e:
        # Handles connection errors (e.g., no internet)
        print(f"A connection error occurred: {e}")
        return None
    except Exception as e:
        # Catches any other unexpected error
        print(f"An unexpected error occurred during data processing: {e}")
        return None