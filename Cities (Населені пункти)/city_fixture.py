import json

with open('city_filtered.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

fixture = []
for index, item in enumerate(data, start=1):
    fixture.append({
        "model": "orders.novaposhtacity",
        "pk": index,
        "fields": {
            "name": item["name"],
            "ref_city": item["ref"],
            "type": item["type"],
            "area": item["area"]
        }
    })

with open('novaposhtacity_fixtures.json', 'w', encoding='utf-8') as output_file:
    json.dump(fixture, output_file, ensure_ascii=False, indent=4)
 
print("Success!")

# Thats all with CIties
# Next are warehouses