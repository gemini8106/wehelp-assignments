
import urllib.request as request
import json
src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data = json.load(response)
attractions_list= data["result"]["results"]
with open("data.csv","w",encoding="utf-8") as file:
    for attraction in attractions_list:
        link = attraction["file"].replace("JPG","jpg")
        site = str(link.split("jpg")[0])
        final = attraction["stitle"]+","+attraction["address"][4:8]+","+attraction["longitude"]+","+attraction["latitude"]+","+site+"jpg"+"\n"
        file.write(final)