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

with open("stockPrice18.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    next(reader, None)
    for row in reader: #each row is a list
        months.append(row[0])
        msft.append(int(row[1]))
        ttwo.append(int(row[2]))
        ea.append(int(row[3]))
        atvi.append(int(row[4]))
        nvda.append(int(row[5]))

msft_d = (msft[9] - msft[0])
ttwo_d = (ttwo[9] - ttwo[0])
ea_d = (ea[9] - ea[0])
atvi_d = (atvi[9] - atvi[0])
nvda_d = (nvda[9] - nvda[0])

msft_f = round(((msft_d / msft[0]) * 100))
ttwo_f = round(((ttwo_d / ttwo[0]) * 100))
ea_f = round(((ea_d / ea[0]) * 100))
atvi_f = round(((atvi_d / atvi[0]) * 100))
nvda_f = round(((nvda_d / nvda[0]) * 100))

msft_n = ('MSFT' + ' (' + str(msft_d) + ')')
ttwo_n = ('TTWO' + ' (' + str(ttwo_d) + ')')
ea_n = ('EA' + ' (' + str(ea_d) + ')')
atvi_n = ('ATVI' + ' (' + str(atvi_d) + ')')
nvda_n = ('NVDA' + ' (' + str(nvda_d) + ')')


plt.bar(msft_n, msft_f, color='#CE0404', align='center')
plt.bar(ttwo_n, ttwo_f, color='#0B8AFA', align='center')
plt.bar(ea_n, ea_f, color='#169F03', align='center')
plt.bar(atvi_n, atvi_f, color='#FBFB16',align='center')
plt.bar(nvda_n, nvda_f, color='#F2850A', align='center')
plt.ylabel("% of Variability YTD 2018")
plt.xlabel("Commodity Symbol and YTD Difference")
plt.xticks(rotation=45, ha="right")
plt.show()
