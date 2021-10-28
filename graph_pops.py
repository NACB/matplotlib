#libraries: json, matplotlib
import matplotlib
import json
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator

#load json files
with open('china_pop.json', encoding='ascii') as f:
    china1 = f.read()
china = json.loads(china1)

with open('india_pop.json', encoding='ascii') as f1:
    india1 = f1.read()
india = json.loads(india1)

#put data in lists
cyear = []
for i in range(len(china[1])):
    cyear.append(china[1][i]["date"])

iyear = []
for i in range(len(india[1])):
    iyear.append(india[1][i]["date"])

cpop = []
for i in range(len(china[1])):
    cpop.append(china[1][i]["value"])

ipop = []
for i in range(len(india[1])):
    ipop.append(india[1][i]["value"])

iyear.reverse()
cyear.reverse()
cpop.reverse()
ipop.reverse()

plt.plot(cyear, cpop, label="Population of China")
plt.plot(cyear, ipop, label="Population of India")

#make chart
plt.xticks(rotation=90, fontsize=5)
plt.xlabel('Year')
plt.ylabel('Population (in billions)')
plt.title('Population of China and India')
plt.legend()

#output
plt.show()