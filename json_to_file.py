import json

data = {
    "Group": {
        "Name": "ABC",
        "Location": "India"
    }
}

with open("datafile.json","w") as write_file:
    json.dump(data,write_file)

with open("load_data.json") as f:
    data = json.load(f)

print(data)
