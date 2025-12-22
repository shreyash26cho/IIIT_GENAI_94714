# main_app.pypython main_app.py

# Import the core function from our custom module
# This line connects the two files
from services.weather_api import get_weather_data

def display_weather(data):
    """Prints the formatted weather data to the console."""
    if data:
        print("\n" + "="*40)
        print(f"Weather Report for {data['city']}:")
        print("="*40)
        print(f"Description: {data['description']}")
        print(f"Temperature: {data['temperature']} °C")
        print(f"Humidity:    {data['humidity']}%")
        print(f"Wind Speed:  {data['wind_speed']} m/s")
        print("="*40)
    else:
        print("\nFailed to retrieve weather data.")

def run_app():
    """Main function to control the application flow."""
    print("Welcome to the Modular Weather App!")
    
    city = input("Enter the city name: ")
    
    # Call the function from the weather_api module to get the data
    weather_info = get_weather_data(city)
    
    # Display the results
    display_weather(weather_info)

# This block ensures the run_app() function executes when you run this file directly
if __name__ == "__main__":
    run_app()