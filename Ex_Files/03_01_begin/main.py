import csv
from pprint import pprint

#csv data about Einstein
EINSTEIN_CSV = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'

#Einstein dictionary
EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}

#instantiate DictReader and list laureates
with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

#for loop that iterates through laureates finding "Einstein" as laureate and
#prints a dictionary for that laureate
for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        break
