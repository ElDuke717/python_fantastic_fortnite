import requests
import datetime

# Replace with your own API key
API_KEY = ""

# Define the location and date range
latitude = "40.7128"  # New York City latitude
longitude = "-74.0060"  # New York City longitude
start_date = datetime.datetime(2021, 1, 1)
end_date = datetime.datetime(2021, 2, 1)
delta = datetime.timedelta(days=1)

# Initialize lists for storing data
temps = []
humidity = []

# Loop through each day in the date range
current_date = start_date
while current_date <= end_date:
    timestamp = int(current_date.timestamp())
    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={latitude}&lon={longitude}&dt={timestamp}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    # Assuming you want the daytime temperature and humidity
    daytime_weather = [hour for hour in data["hourly"] if 6 <= datetime.datetime.fromtimestamp(hour["dt"]).hour <= 18]
    avg_temp = sum(hour["temp"] for hour in daytime_weather) / len(daytime_weather)
    avg_humidity = sum(hour["humidity"] for hour in daytime_weather) / len(daytime_weather)

    temps.append(avg_temp - 273.15)  # Convert from Kelvin to Celsius
    humidity.append(avg_humidity)

    # Move to the next day
    current_date += delta

# Print the results
print(f"Average temperature and humidity for New York City between {start_date} and {end_date}:")
for i in range(len(temps)):
    print(f"Day {i+1}: Temperature: {temps[i]:.2f}°C, Humidity: {humidity[i]:.2f}%")
