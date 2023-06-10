import csv
import re
import operator

crimes = {}
with open("Crimes.csv") as f:
    reader = csv.reader(f)

    for row in reader:
        crime = row[5]
        year = row[2]
        if re.search("......2015.+", year):
            if crimes.get(crime):
                crimes[crime] += 1
            else:
                crimes.update({crime: 1})
print(max(crimes, key=crimes.get))
