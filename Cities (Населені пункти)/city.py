import requests
import json

URL = 'https://api.novaposhta.ua/v2.0/json/'


all_settlements = []

# Take area name from file that u've setteled before
with open('areas_sorted.json', 'r', encoding='utf-8') as areas_file:
    areas_data = json.load(areas_file)

# Going through all the areas and making request
for area in areas_data:
    area_name = area["name"]
    PARAMS = {
        "apiKey": "",  #Set your own Token from NovaPoshta
        "modelName": "Address",
        "calledMethod": "getCities",
        "methodProperties": {
            "FindByString": area_name
        }
    }

    HEADERS = {'Content-Type': 'application/json'}

    # Sending request here
    response = requests.post(URL, data=json.dumps(PARAMS), headers=HEADERS)

    if response.status_code == 200:
        settlements = response.json().get("data", [])

        # Getting only data that we need
        filtered_data = [
            {
                "ref": settlement["Ref"],
                "name": settlement["Description"],
                "type": settlement["SettlementTypeDescription"],
                "area": settlement["AreaDescription"] + " область"
            }
            for settlement in settlements
        ]

        
        all_settlements.extend(filtered_data)

        print(
            f"Data in {area['name']} were added successfully!")
    else:
        print(
            f"Error with {area['name']}: {response.status_code}")

# Store data in file thatwe created !before running script!
with open('city.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_settlements, json_file, ensure_ascii=False,
              indent=2, separators=(',', ': '))

print("Success!")

# We also need to filter the output file because a lot of duplicates were stored in it
# Next go to filter.py  