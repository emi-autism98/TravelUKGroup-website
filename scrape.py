import requests
from bs4 import BeautifulSoup
import json

urlTUKG = "https://www.mybustimes.cc/group/Travel%20UK%20Group/"
urlTNW = "https://www.mybustimes.cc/operator/travel-north-west/"
urlTUKC = "https://www.mybustimes.cc/operator/travel-uk-coaches/"
urlTNWR = "https://www.mybustimes.cc/operator/travel-north-west-rail/"
urlTNWM = "https://www.mybustimes.cc/operator/merseytravel-metro-travel-north-west/"

routesTUKG = None
routesTNW = None
routesTUKC = None
routesTNWR = None
routesTNWM = None
vehiclesTUKG = None
vehiclesTNW = None
vehiclesTUKC = None
vehiclesTNWR = None
vehiclesTNWM = None

responseTUKG = requests.get(urlTUKG)
responseTNW = requests.get(urlTNW)
responseTUKC = requests.get(urlTUKC)
responseTNWR = requests.get(urlTNWR)
responseTNWM = requests.get(urlTNWM)

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

soupTNWM = BeautifulSoup(responseTNWM.text, "html.parser")
itemsTNWM = soupTNWM.find_all("li")
for item in itemsTNWM:
    content = item.get_text()
    if "routes" in content:
        routesTNWM = int(content.split()[0].replace(",", ""))

vehUrlTNW = "https://www.mybustimes.cc/operator/travel-north-west/vehicles/"
vehUrlTUKC = "https://www.mybustimes.cc/operator/travel-uk-coaches/vehicles/"
vehUrlTNWR = "https://www.mybustimes.cc/operator/travel-north-west-rail/vehicles/"
vehUrlTNWM = "https://www.mybustimes.cc/operator/merseytravel-metro-travel-north-west/vehicles/"

vehResponseTNW = requests.get(vehUrlTNW)
vehResponseTUKC = requests.get(vehUrlTUKC)
vehResponseTNWR = requests.get(vehUrlTNWR)
vehResponseTNWM = requests.get(vehUrlTNWM)

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

soupVehTNWM = BeautifulSoup(vehResponseTNWM.text, "html.parser")
itemsVehTNWM = soupVehTNWM.find_all("li")
for item in itemsVehTNWM:
    content = item.get_text()
    if "vehicles" in content:
        vehiclesTNWM = int(content.split()[0].replace(",", ""))

routesTNW = int(routesTNW) + int(routesTNWM)
vehiclesTNW = int(vehiclesTNW) + int(vehiclesTNWM)

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
