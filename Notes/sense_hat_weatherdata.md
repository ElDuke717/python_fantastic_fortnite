# GET WEATHER DATA FROM SENSE HAT

To do this, we'll be using the `sense-hat` library for Raspberry Pi and Python's `csv` module.

Here's a step-by-step breakdown:

1. **Setup**:

   - Install the sense-hat library if you haven't already:
     ```bash
     sudo apt-get install sense-hat
     sudo pip3 install sense-hat
     ```
   - Make sure your Sense HAT is properly attached to your Raspberry Pi.

2. **Python Script**:

```python
import csv
import time
from sense_hat import SenseHat

sense = SenseHat()

def get_weather_data():
    # Get temperature, humidity, and pressure data
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()
    pressure = sense.get_pressure()

    return temperature, humidity, pressure

def write_to_csv(data):
    with open("weather_data.csv", mode="a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

def main():
    # Set this to the interval you want, e.g., 60 for 1 minute
    INTERVAL = 60

    # If file doesn't exist, write headers
    try:
        with open("weather_data.csv", "x", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Temperature", "Humidity", "Pressure", "Timestamp"])
    except FileExistsError:
        pass

    while True:
        temperature, humidity, pressure = get_weather_data()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Logging data at {timestamp}")
        write_to_csv([temperature, humidity, pressure, timestamp])
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
```

3. **How it Works**:

   - `get_weather_data` fetches the current temperature, humidity, and pressure from the Sense HAT.
   - `write_to_csv` appends the data to the CSV file.
   - The `main` function:
     - First checks if the CSV file exists. If it doesn't, it creates one with headers.
     - Fetches the weather data at set intervals (e.g., every minute) and appends it to the CSV file.

4. **Running the Script**:

   - Save the Python script, for example, as `sensehat_logger.py`.
   - Run it using:
     ```bash
     python3 sensehat_logger.py
     ```
   - The script will continuously log the weather data to `weather_data.csv` at your set interval.

5. **Stopping the Script**:
   - Press `CTRL + C` to stop the script when you want to.


