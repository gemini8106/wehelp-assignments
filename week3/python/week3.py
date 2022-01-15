
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
clist= data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
    for sample in clist:
        link = sample["file"].replace("JPG","jpg")
        site = str(link.split("jpg")[0])
        final = sample["stitle"]+","+sample["address"][4:8]+","+sample["longitude"]+","+sample["latitude"]+","+site+"jpg"+"\n"
        file.write(final)