# A script to scrape the amount of routes and vehicles because I can't be arsed doing it myself
print("Behold, the one, the only scrape script-a-tron-o-matic 5000 (website will likely be broken - holding your breath, crossing your fingers and touching wood recommended)")

# Import libraries (duh)
import requests
from bs4 import BeautifulSoup
import json

# Routes and all that jazz
print("Part 1: Scraping routes (if the website doesn't break again, which is a big if)")
urlTUKG = "https://www.mybustimes.cc/group/Travel%20UK%20Group/"
urlTNW = "https://www.mybustimes.cc/operator/travel-north-west/"
urlTUKC = "https://www.mybustimes.cc/operator/travel-uk-coaches/"
urlTNWR = "https://www.mybustimes.cc/operator/travel-north-west-rail/"

routesTUKG = None
routesTNW = None
routesTUKC = None
routesTNWR = None
vehiclesTUKG = None
vehiclesTNW = None
vehiclesTUKC = None
vehiclesTNWR = None

responseTUKG = requests.get(urlTUKG)
responseTNW = requests.get(urlTNW)
responseTUKC = requests.get(urlTUKC)
responseTNWR = requests.get(urlTNWR)

if responseTUKG.status_code == 200:
    print("Travel UK Group response (both pages): ", responseTUKG.status_code, "(that's good)")
elif responseTUKG.status_code != 200:
    print("Travel UK Group response (both pages): ", responseTUKG.status_code, "(that's not good - MBT has probably shat itself again - as booked)")

if responseTNW.status_code == 200:
    print("Travel North West response (routes): ", responseTNW.status_code, "(that's good)")
elif responseTNW.status_code != 200:
    print("Travel North West response (routes): ", responseTNW.status_code, "(that's not good - MBT has probably shat itself again - as booked)")

if responseTUKC.status_code == 200:
    print("Travel UK Coaches response (routes): ", responseTUKC.status_code, "(that's good)")
elif responseTUKC.status_code != 200:
    print("Travel UK Coaches response (routes): ", responseTUKC.status_code, "(that's not good - MBT has probably shat itself again - as booked)")

if responseTNWR.status_code == 200:
    print("Travel North West Rail response (routes): ", responseTNWR.status_code, "(that's good)")
elif responseTNWR.status_code != 200:
    print("Travel North West Rail response (routes): ", responseTNWR.status_code, "(that's not good - MBT has probably shat itself again - as booked)")

soupTUKG = BeautifulSoup(responseTUKG.text, "html.parser")
itemsTUKG = soupTUKG.find_all("li")
for item in itemsTUKG:
    content = item.get_text()
    if "routes" in content:
        routesTUKG = int(content.split()[0].replace(",", ""))
    if "vehicles" in content:
        vehiclesTUKG = int(content.split()[0].replace(",", ""))

soupTNW = BeautifulSoup(responseTNW.text, "html.parser")
itemsTNW = soupTNW.find_all("li")
for item in itemsTNW:
    content = item.get_text()
    if "routes" in content:
        routesTNW = int(content.split()[0].replace(",", ""))

soupTUKC = BeautifulSoup(responseTUKC.text, "html.parser")
itemsTUKC = soupTUKC.find_all("li")
for item in itemsTUKC:
    content = item.get_text()
    if "routes" in content:
        routesTUKC = int(content.split()[0].replace(",", ""))

soupTNWR = BeautifulSoup(responseTNWR.text, "html.parser")
itemsTNWR = soupTNWR.find_all("li")
for item in itemsTNWR:
    content = item.get_text()
    if "routes" in content:
        routesTNWR = int(content.split()[0].replace(",", ""))

# Vehicles that use a separate page for whatever reason
print("Part 2: Exactly the same but with vehicles/ at the end because why wouldn't it be? (You can probably breathe now)")

vehUrlTNW = "https://www.mybustimes.cc/operator/travel-north-west/vehicles/"
vehUrlTUKC = "https://www.mybustimes.cc/operator/travel-uk-coaches/vehicles/"
vehUrlTNWR = "https://www.mybustimes.cc/operator/travel-north-west-rail/vehicles/"

vehResponseTNW = requests.get(vehUrlTNW)
vehResponseTUKC = requests.get(vehUrlTUKC)
vehResponseTNWR = requests.get(vehUrlTNWR)

soupVehTNW = BeautifulSoup(vehResponseTNW.text, "html.parser")
itemsVehTNW = soupVehTNW.find_all("li")
for item in itemsVehTNW:
    content = item.get_text()
    if "vehicles" in content:
        vehiclesTNW = int(content.split()[0].replace(",", ""))

soupVehTUKC = BeautifulSoup(vehResponseTUKC.text, "html.parser")
itemsVehTUKC = soupVehTUKC.find_all("li")
for item in itemsVehTUKC:
    content = item.get_text()
    if "vehicles" in content:
        vehiclesTUKC = int(content.split()[0].replace(",", ""))

soupVehTNWR = BeautifulSoup(vehResponseTNWR.text, "html.parser")
itemsVehTNWR = soupVehTNWR.find_all("li")
for item in itemsVehTNWR:
    content = item.get_text()
    if "vehicles" in content:
        vehiclesTNWR = int(content.split()[0].replace(",", ""))

# Last but not least, save all the blah-dee-blah to the whatchamacallit, and we (should) be good to go
data = {
    "routes_TUKG": routesTUKG,
    "routes_TNW": routesTNW,
    "routes_TUKC": routesTUKC,
    "routes_TNWR": routesTNWR,
    "vehicles_TUKG": vehiclesTUKG,
    "vehicles_TNW": vehiclesTNW,
    "vehicles_TUKC": vehiclesTUKC,
    "vehicles_TNWR": vehiclesTNWR,
    "towns": 20 # Not really scrapable unless I add a directory of every single town which is NOT happening, I'll just count this part whenever I remember
}

with open("stats.json", "w") as f:
    json.dump(data, f)

print("Stats (hopefully) updated successfully")

# That was way too much effort but now it's automated so that's a win
# 5 hours once > 5 minutes every day. Sound logic
