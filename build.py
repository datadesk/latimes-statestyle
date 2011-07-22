import csv
from pprint import pprint

data = csv.DictReader(open("./statestyle/data.csv", "r"))
print "STATES = ",
pprint (list(data))
