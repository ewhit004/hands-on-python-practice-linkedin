#csv and json imports allow us to read these types of files
import csv
import json
from pprint import pprint

#Einstein dictionary
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

#transfers Einstein dictionary into json type
einstein_json = json.dumps(EINSTEIN)
back_to_dict = json.loads(einstein_json)
print(einstein_json)
pprint(back_to_dict)

#type "read" bc this is a dictionary
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

#how to turn an entire csv file into a json file with .dump()
#type "write" bc we're rewriting the file with json type
with open("laureates.json", "w") as f:
    json.dump(laureates, f, indent=2)
