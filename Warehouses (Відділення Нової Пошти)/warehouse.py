import requests
import json

URL = 'https://api.novaposhta.ua/v2.0/json/'


all_settlements = []

# Open file with your cities that you've got from script earlier
with open('city_filtered.json', 'r', encoding='utf-8') as areas_file:
    areas_data = json.load(areas_file)

# make requests with all cities 
for area in areas_data:
    area_ref = area["ref"]
    PARAMS = {
        "apiKey": "", # Here paste your your token from NovaPoshta
        "modelName": "Address",
        "calledMethod": "getWarehouses",
        "methodProperties": {
            "CityRef": area_ref
        }
    }

    HEADERS = {'Content-Type': 'application/json'}


    response = requests.post(URL, data=json.dumps(PARAMS), headers=HEADERS)

    if response.status_code == 200:
        settlements = response.json().get("data", [])

        # Getting data that we need
        filtered_data = [
            {
                "ref": settlement["SettlementRef"],
                "name": settlement["Description"],
                "adress": settlement["ShortAddress"],
                "type": settlement["TypeOfWarehouse"],
                "city": settlement["CityDescription"],
                "city_ref": settlement["CityRef"],
                "region": settlement["SettlementRegionsDescription"],
                "area": settlement["SettlementAreaDescription"]
            }
            for settlement in settlements
        ]


        all_settlements.extend(filtered_data)

        print(
            f"Data for {area['name']} was successfully added")
    else:
        print(
            f"Error with {area['name']}: {response.status_code}")

# Before !running script! create file in which we will paste data
with open('warehouse.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_settlements, json_file, ensure_ascii=False,
              indent=2, separators=(',', ': '))

print("All data were added. Success!")
