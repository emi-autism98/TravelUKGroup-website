import requests
from bs4 import BeautifulSoup
import json

# Setup URLs
urls = {
    "TUKG": "https://mybustimes.cc",
    "TNW": "https://mybustimes.cc",
    "TUKC": "https://mybustimes.cc",
    "TNWR": "https://mybustimes.cc",
    "TNWM": "https://mybustimes.cc"
}

veh_urls = {
    "TNW": "https://mybustimes.ccvehicles/",
    "TUKC": "https://mybustimes.ccvehicles/",
    "TNWR": "https://mybustimes.ccvehicles/",
    "TNWM": "https://mybustimes.ccvehicles/"
}

# Helper function to scrape a single metric safely
def get_metric(url, keyword):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            return 0
        
        soup = BeautifulSoup(response.text, "html.parser")
        for item in soup.find_all("li"):
            content = item.get_text().lower()
            if keyword in content:
                # Extract only digits from the item string
                num_str = "".join([c for c in content.split()[0] if c.isdigit() or c == ','])
                return int(num_str.replace(",", "")) if num_str else 0
    except Exception as e:
        print(f"Error scraping {url} for {keyword}: {e}")
    return 0

# Extract data with safe defaults (0 instead of None)
routes_TUKG = get_metric(urls["TUKG"], "routes")
vehicles_TUKG = get_metric(urls["TUKG"], "vehicles")

routes_TNW = get_metric(urls["TNW"], "routes")
routes_TUKC = get_metric(urls["TUKC"], "routes")
routes_TNWR = get_metric(urls["TNWR"], "routes")
routes_TNWM = get_metric(urls["TNWM"], "routes")

vehicles_TNW = get_metric(veh_urls["TNW"], "vehicles")
vehicles_TUKC = get_metric(veh_urls["TUKC"], "vehicles")
vehicles_TNWR = get_metric(veh_urls["TNWR"], "vehicles")
vehicles_TNWM = get_metric(veh_urls["TNWM"], "vehicles")

# Add combined regional metrics safely
routes_TNW += routes_TNWM
vehicles_TNW += vehicles_TNWM

# Construct final payload
data = {
    "routes_TUKG": routes_TUKG,
    "routes_TNW": routes_TNW,
    "routes_TUKC": routes_TUKC,
    "routes_TNWR": routes_TNWR,
    "vehicles_TUKG": vehicles_TUKG,
    "vehicles_TNW": vehicles_TNW,
    "vehicles_TUKC": vehicles_TUKC,
    "vehicles_TNWR": vehicles_TNWR,
    "towns": 20 
}

with open("stats.json", "w") as f:
    json.dump(data, f, indent=4)

print("Scraping completed and stats.json saved.")
