import json


def remove_duplicates(data):
    unique_items = []
    seen_items = set()

    for item in data:
        item_tuple = tuple(sorted(item.items()))
        if item_tuple not in seen_items:
            unique_items.append(item)
            seen_items.add(item_tuple)

    return unique_items


# Taking data from file with all data from requests
with open("city.json", "r") as file:
    json_data = json.load(file)

# Deliting duplicates
filtered_data = remove_duplicates(json_data)

# The sum of deleted duplicates
num_removed_duplicates = len(json_data) - len(filtered_data)

# Info about script work
if num_removed_duplicates > 0:
    print(
        f"{num_removed_duplicates} Duplicates were deleted")
else:
    print("Duplicates weren't found")

# Store data in file that we've created !before running script!
with open("city_filtered", "w") as new_file:
    json.dump(filtered_data, new_file, indent=2, ensure_ascii=False)

print("Success!")

# Going in next py file (fixtures setter)
# We will make fixtures then