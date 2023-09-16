# Import necessary modules
import requests
import datetime
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Retrieve API key from environment variable
API_KEY = os.environ['API_KEY']

# Set latitude and longitude coordinates for location
latitude = "37.3852339"
longitude = "-77.699888"

# Get the current date and time, and set the range for data collection
current_date = datetime.datetime.now()
end_date = current_date
start_date = end_date - datetime.timedelta(days=5)

# Initialize empty lists to store temperature and humidity data
temps = []
humidity = []

# Set the time delta to move one day at a time
delta = datetime.timedelta(days=1)

# Initialize the loop to cycle through the date range
current_date = start_date
while current_date <= end_date:
    # Convert current datetime to Unix timestamp
    timestamp = int(current_date.timestamp())
    
    # Build the API request URL
    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={timestamp}&appid={API_KEY}"
    
    # Make the API request
    response = requests.get(url)
    
    # Check if the API request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if "hourly" data is available in the response
        if "hourly" in data:
            # Filter out daytime hours (6 AM to 6 PM)
            daytime_weather = [hour for hour in data["hourly"] if 6 <= datetime.datetime.fromtimestamp(hour["dt"]).hour <= 18]
            
            # Calculate average temperature and humidity for daytime hours
            avg_temp = sum(hour["temp"] for hour in daytime_weather) / len(daytime_weather)
            avg_humidity = sum(hour["humidity"] for hour in daytime_weather) / len(daytime_weather)

            # Convert temperatures from Kelvin to Fahrenheit
            celsius_temp = avg_temp - 273.15
            fahrenheit_temp = (celsius_temp * 9/5) + 32
            
            # Store the calculated values in lists
            temps.append(fahrenheit_temp)
            humidity.append(avg_humidity)
        else:
            print(f"Hourly data not available for {current_date}")
    else:
        print(f"Failed to get data for {current_date}. Status code: {response.status_code}")
        
    # Move to the next day in the date range
    current_date += delta

# Output the collected data
print(f"Average temperature and humidity for Richmond between {start_date} and {end_date}:")
for i in range(len(temps)):
    print(f"Day {i+1}: Temperature: {temps[i]:.2f}°F/{(temps[i] - 32) * 5/9:.2f}°C, Humidity: {humidity[i]:.2f}%")
