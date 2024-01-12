import csv
#library that creates straightforward data structures
from datetime import datetime
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

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)


for laureate in laureates:
    if laureate["surname"] == "Einstein":
        pprint(laureate)
        print("============")
        #calculating the age he was when he received his prize: year - born
        year_date = datetime.strptime(laureate["year"], "%Y")
        born_date = datetime.strptime(laureate["born"], "%Y-%m-%d")
        print("age", year_date.year - born_date.year)
        break
