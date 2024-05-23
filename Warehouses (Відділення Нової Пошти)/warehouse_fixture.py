import json

with open('warehouse.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

fixture = []
for index, item in enumerate(data, start=1):
    fixture.append({
        "model": "orders.novaposhtawarehouse",
        "pk": index,
        "fields": {
            "name": item["name"],
            "ref_warehouse": item["ref"],
            "adress": item["adress"],
            "type": item["type"],
            "city": item["city"],
            "city_ref": item["city_ref"],
            "region": item["region"],
            "area": item["area"]
        }
    })

with open('novaposhtawarehouse_fixture.json', 'w', encoding='utf-8') as output_file:
    json.dump(fixture, output_file, ensure_ascii=False, indent=4)
