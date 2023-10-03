import requests
from bs4 import BeautifulSoup
import re

def validate_url(url):
    return re.match(r'https?://\S+', url)

# Ask user for URL
url = input("Enter a URL in the form https://www.example.com: ")

# Validate URL
if not validate_url(url):
    print("Invalid URL. Exiting.")
    exit()

try:
    # Send a request to the webpage and get HTML response
    response = requests.get(url, timeout=10)
    
    # Check if the request was successful
    response.raise_for_status()
except requests.RequestException as e:
    print(f"An error occurred: {e}")
    exit()

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Define the regular expression you want to match
regex = r"(?i)raspberry\s+pi"

# Use the re module to find all the words that match the regex
matches = re.findall(regex, soup.text)

# Print the list of matches
print(len(matches))
