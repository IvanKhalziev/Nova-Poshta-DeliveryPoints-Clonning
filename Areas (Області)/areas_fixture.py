import json

# Take data from file in which we have all data about areas
with open('areas.json', 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

index = 1
fixture = []
for item in data.get('data', []):
    fixture.append({
        "model": "orders.novaposhtaarea",
        "pk": index,
        "fields": {
            'name': f"{item['Description']} {item['RegionType']}",
            'ref': item['Ref']
        }
    })
    index += 1

# Create file !before running script! in which u want to store fixtures
with open('novaposhtaareas_fixtures.json', 'w', encoding='utf-8') as output_file:
    json.dump(fixture, output_file, ensure_ascii=False, indent=4)
