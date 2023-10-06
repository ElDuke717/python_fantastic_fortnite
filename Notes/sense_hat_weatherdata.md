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

## Running the script continuously

If you want the script to run continuously, especially for long durations such as years, you'll need to consider a few additional steps to ensure reliability and continuity:

1. **Using Screen or Tmux**:

   - If you're running the script on a remote server or a Raspberry Pi through SSH, you can use tools like `screen` or `tmux`. These tools allow the script to continue running even after you've closed your terminal session.

   For instance, with `screen`:

   ```bash
   sudo apt-get install screen
   screen
   python3 sensehat_logger.py
   ```

   Press `CTRL + A` followed by `D` to detach from the screen session. To reattach, use `screen -r`.

2. **Automate the Start with Cron**:

   - You can set up the script to run on boot using a cron job with `@reboot`. This ensures the script restarts if the Raspberry Pi reboots for some reason.

   ```bash
   crontab -e
   ```

   Add the following line to run the script on boot:

   ```
   @reboot /usr/bin/python3 /path/to/sensehat_logger.py &
   ```

3. **Error Handling**:

   - Add error handling in the script to manage occasional failures, such as sensor read failures or temporary issues.

4. **Monitoring & Notifications**:

   - Consider adding some form of monitoring or notification system, so you're alerted if the script stops for any reason.

5. **Backup Your Data**:
   - Since you're collecting data over years, it's important to regularly back up your CSV file to prevent any data loss.
6. **Data Storage Considerations**:

   - Depending on the frequency of logging, logging data for years might lead to a very large CSV file. Periodically archiving or splitting the data could be useful. You might also want to consider using databases for more efficient and structured long-term storage.

7. **Optimize the Power Source**:

   - Ensure the Raspberry Pi has a stable power source. Consider using an Uninterrupted Power Supply (UPS) to protect against power outages.

8. **Keep System Updated and Secure**:
   - Regularly update the operating system and packages to keep everything secure and running smoothly.

With these considerations in place, you can have the script run continuously and gather hourly data for extended periods without any issues. Remember, though, that like all devices, the Raspberry Pi and Sense HAT have lifetimes, so periodic maintenance and checks will still be necessary.

## Displaying Data on a Webpage

Displaying hourly sensor data on your weather.html page requires a few steps. I'll guide you through the process:

1. **Data Storage**:
   First, we need a way to store hourly data. We'll continue using the CSV for this example, but for more complex setups, databases like SQLite might be more appropriate.

2. **Hourly Data Collection**:
   You can modify the previous script to save data hourly:

   ```python
   ...
   INTERVAL = 3600  # 1 hour in seconds
   ...
   ```

3. **Web Server**:
   Ensure you have a web server installed on your Raspberry Pi. Apache or Nginx are common choices:

   ```bash
   sudo apt-get install apache2
   ```

4. **Python CGI Script**:
   You can use a Python CGI script to read the CSV file and return the data as JSON, which can then be fetched and displayed on your webpage.

   Install CGI module:

   ```bash
   sudo apt-get install python3-cgi
   ```

   Create a Python script `weather_data.py` to serve the data:

   ```python
   #!/usr/bin/env python3

   import csv
   import json

   print("Content-Type: application/json\n\n")

   with open('weather_data.csv', 'r') as file:
       data = [row for row in csv.DictReader(file)]
       print(json.dumps(data[-24:]))  # get the last 24 records for hourly data of the past day
   ```

   Make it executable:

   ```bash
   chmod +x weather_data.py
   ```

5. **Update weather.html**:
   You'll need to fetch the data from the CGI script and display it. Here's a simple example using JavaScript:

   ```html
   ...
   <script>
     fetch("/cgi-bin/weather_data.py")
       .then((response) => response.json())
       .then((data) => {
         // Here you can update the DOM with the data
         // For example:
         const weatherContainer = document.querySelector(".weather-container");
         data.forEach((entry) => {
           weatherContainer.innerHTML += `<p>Time: ${entry.Timestamp}, Temp: ${entry.Temperature}</p>`;
         });
       });
   </script>
   ...
   ```

6. **Apache Configuration**:
   You'll need to enable CGI and serve your Python script:

   ```bash
   sudo a2enmod cgi
   sudo systemctl restart apache2
   ```

   Move the `weather_data.py` script to `/usr/lib/cgi-bin/` (which is Apache's default CGI directory).

   Ensure that the directory `/usr/lib/cgi-bin/` has the correct permissions. The Apache user should be able to execute scripts there.

7. **Hourly Update**:
   Your website will be updated whenever someone accesses it. If you want the displayed data to auto-refresh at regular intervals, you can use JavaScript's `setInterval()` function.

Remember that hosting a web service on your Raspberry Pi, especially if exposed to the internet, presents security concerns. Make sure you take necessary precautions, such as regularly updating software, setting up firewalls, and minimizing exposed services.

This setup will allow your weather.html page to fetch the latest 24 hours of data from your sensor whenever it's accessed. If you'd like a more dynamic display (e.g., charts, graphs), you can integrate with libraries like Chart.js. Let me know if you want to dive into more advanced visualizations or have other questions!
