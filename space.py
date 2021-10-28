import json
import matplotlib
from matplotlib import pyplot as plt

with open('space.json', encoding='ascii') as f:
    space1 = f.read()
space = json.loads(space1)

ufo = []
for i in range(len(space["people"])):
    ufo.append(space["people"][i]["craft"])

numiniss = 0
numinshen = 0

for i in range(len(ufo)):
    if ufo[i] == 'ISS':
        numiniss += 1
    else:
        numinshen += 1
final = [numiniss, numinshen]



labels = 'ISS', 'Shenzhou 13'

fig, ax = plt.subplots()
ax.pie(final, labels=labels, autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis('equal')
plt.title('Astronauts Currently in Space and their Crafts')

plt.show()