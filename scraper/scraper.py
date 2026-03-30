import requests
from bs4 import BeautifulSoup
import json
import datetime

url = "http://nextcloud_app:80"   # nom du service app dans le réseau Docker
try:
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else "No title"
    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "value": title,
        "source": "nextcloud_local"
    }
    with open("/data/scraped.json", "w") as f:
        json.dump(data, f)
    print("Scraped data saved")
except Exception as e:
    print(f"Error: {e}")
