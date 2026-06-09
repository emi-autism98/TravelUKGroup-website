import requests
from bs4 import BeautifulSoup
import json

url = "https://www.mybustimes.cc/group/Travel%20UK%20Group/"
vehicles = None
routes = None

response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
items = soup.find_all("li")
for item in items:
    content = item.get_text()
    if "vehicles" in content:
        vehicles = int(content.split()[0].replace(",", ""))
    if "routes" in content:
        routes = int(content.split()[0].replace(",", ""))

data = {
    "vehicles": vehicles,
    "routes": routes
}

with open("stats.json", "w") as f:
    json.dump(data, f)

print("Stats updated successfully")
