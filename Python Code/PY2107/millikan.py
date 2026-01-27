import math
import numpy as np

array = [[175,115.24,7],[113,145.31,8.7],[205,65.33,5],[203,108.56,7.9],
         [338,89.71,8.8],[318,77.08,7.2],[333,71.83,8.7],[185,85.92,7],
         [331,87.62,7.5],[145,62.42,6],[242,52.11,7],[489,62.69,8],
         [424,43.73,5.5],[275,74.43,7],[427,28.95,5],[247,30.62,5],
         [250,68.79,6],[250,67.78,6],[287,39.4,5],[249,61.1,5]]

q = []

def e(V,t,d):
    piterm = (4 * math.pi * 6 * (10 ** -3)) / 3
    sqrt = (((4.5 * (1.718 + 0.0049 * 20) * (10 ** -5))**3)/(970 * 9.8)) ** 0.5
    distance = d * 0.5 * (10 ** -3)
    v = distance / t
    vterm = (v**1.5) / V
    q = piterm * sqrt * vterm
    n = q / (1.60217663E-19)
    print(n)
    return q

for i in range(len(array)):
    q.append(e(array[i][0],array[i][1],array[i][2]))


q.sort()
print(np.array(q))

'''
e =[]
for i in range(0, len(q)):
    for j in range(i, len(q)):
        e.append(abs(q[i] - q[j]))
e.sort()

while(e[0] < 1E-19):
    e.pop(0)
e2 = []

while(e[0] < 2E-19):
    e2.append(e.pop(0))
temp = []
counter = 0
while(len(e) != 0):
    for i in range(0, len(e)):
        for j in range(0, len(e2)):
            temp.append(abs(e[i] - e2[j]))
    temp.sort()
    while(temp[0] < 1E-19):
        temp.pop(0)
    while(temp[0] < 2E-19):
        e2.append(temp.pop(0))
    e.clear()
    for i in range(0, len(temp)):
        e.append(temp[i])
    counter += 1
    if(counter >= 1):
        break
    temp.clear()
    print(counter)
print(np.mean(e2))
print(np.std(e2))
print(len(e2))
'''
    
