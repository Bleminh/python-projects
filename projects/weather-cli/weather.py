import sys
import requests

# 1. Check if they typed a city name
if len(sys.argv) < 2:
    print("Usage: python weather.py <CityName>")
    sys.exit()

city_name = sys.argv[1]
geocode_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"

# 2. Try to get the coordinates
try:
    print(f"Looking up coordinates for {city_name}...")
    response = requests.get(geocode_url)
    response.raise_for_status() # This triggers the except block if the website is down
    
    data = response.json()
    
    # Extract the data from the JSON dictionary
    lat = data["results"][0]["latitude"]
    lon = data["results"][0]["longitude"]
    
    print(f"Found coordinates: Lat {lat}, Lon {lon}")

# 3. If the network drops, or the website is down, it jumps here
except requests.exceptions.RequestException as e:
    print("Error: Could not connect to the geocoding service. Check your Wi-Fi.")
    sys.exit() # Stop the script so it doesn't try to get the weather with no coordinates
    
# 4. If the city doesn't exist, the JSON won't have a "results" key
except KeyError:
    print(f"Error: Could not find a city named '{city_name}'.")
    sys.exit()

weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,wind_speed_10m"

try:
    print("Fetching weather...")
    weather_response = requests.get(weather_url)
    weather_response.raise_for_status() 
    
    weather_data = weather_response.json()
    
    # Drill into the JSON to get the numbers
    temp = weather_data["current"]["temperature_2m"]
    wind = weather_data["current"]["wind_speed_10m"]
    
    # Print a clean, terminal-friendly output
    print("\n==============================")
    print(f"   WEATHER FOR {city_name.upper()}")
    print("==============================")
    print(f"🌡️  Temperature: {temp}°C")
    print(f"💨 Wind Speed:  {wind} km/h")
    print("==============================\n")

except requests.exceptions.RequestException:
    print("Error: Reached the coordinates, but the weather service failed.")
except KeyError:
    print("Error: Could not parse the weather data correctly.")