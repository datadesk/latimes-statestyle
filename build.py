import csv
from pprint import pprint

# Get the source data
data = list(csv.DictReader(open("./statestyle/data.csv", "r")))

# Create the normalizer
crosswalk = {}
for row in data:
    for key, value in row.items():
        if value and key != 'type':
            crosswalk[value] = row
            crosswalk[value.lower()] = row

print "CROSSWALK = ",
pprint(crosswalk)
