import requests

def get_weather(city_name, api_key):
    # OpenWeatherMap API endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters to send with the request
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use metric units for temperature in Celsius
    }
    
    # Send a GET request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract relevant weather information
        city = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Display the weather information
        print(f"Weather in {city}, {country}:")
        print(f"  Temperature: {temperature}°C")
        print(f"  Description: {weather_description.capitalize()}")
        print(f"  Humidity: {humidity}%")
        print(f"  Wind Speed: {wind_speed} m/s")
    else:
        print("Error: Unable to fetch weather data. Please check the city name or API key.")

# Example Usage
if __name__ == "__main__":
    # Replace with your OpenWeatherMap API key
    api_key = "your_api_key_here"
    
    # Input the city name
    city_name = input("Enter the city name: ")
    
    # Fetch and display weather data
    get_weather(city_name, api_key)
