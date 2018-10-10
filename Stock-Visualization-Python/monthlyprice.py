import matplotlib.pyplot as plt
import numpy as np
import csv

results = []
months = []
msft = []
ttwo = []
ea = []
atvi = []
nvda = []

with open("stockPrice.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader: #each row is a list
        months.append(row[0])
        msft.append(int(row[1]))
        ttwo.append(int(row[2]))
        ea.append(int(row[3]))
        atvi.append(int(row[4]))
        nvda.append(int(row[5]))

plt.plot(months, msft, color='#CE0404', marker='o', linestyle='solid', label='Microsoft (MSFT)')
plt.plot(months, ttwo, color='#0B8AFA', marker='o', linestyle='solid', label='Take-Two (TTWO)')
plt.plot(months, ea, color='#169F03', marker='o', linestyle='solid', label='Electronic Arts (EA)')
plt.plot(months, atvi, color='#FBFB16', marker='o', linestyle='solid', label='Activision-Blizzard (ATVI)')
plt.plot(months, nvda, color='#F2850A', marker='o', linestyle='solid', label='Nvidia (NVDA)')
plt.legend(loc='upper left')
plt.ylabel("Stock Price")
plt.xlabel("Date Range")
plt.xticks(rotation=45, ha="right")
plt.show()
