import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
years = []
harrison_pops = []
jackson_pops = []

with open("msCensus.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader: #each row is a list
        years.append(row[0])
        harrison_pops.append(int(row[1]))
        jackson_pops.append(int(row[2]))

plt.scatter(years, harrison_pops, c='r', marker='^', label='Harrison County')
plt.scatter(years, jackson_pops, c='b', marker='o', label='Jackson County')
plt.legend(loc='upper left')
plt.ylabel("Population")
plt.xlabel("Date Range")
plt.xticks(rotation=45, ha="right")
plt.show()
