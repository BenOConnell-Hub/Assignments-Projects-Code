import math as m
import numpy as np
import matplotlib.pyplot as plt

array = [[175,115.24,7],[113,145.31,8.7],[205,65.33,5],[203,108.56,7.9],
         [338,89.71,8.8],[318,77.08,7.2],[333,71.83,8.7],[185,85.92,7],
         [331,87.62,7.5],[145,62.42,6],[242,52.11,7],[489,62.69,8],
         [424,43.73,5.5],[275,74.43,7],[427,28.95,5],[247,30.62,5],
         [250,68.79,6],[250,67.78,6],[287,39.4,5],[249,61.1,5]]

q = []
sigq = []

def e(V,t,d):
    piterm = (4 * m.pi * 6 * (10 ** -3)) / 3
    sqrt = (((4.5 * (1.718 + 0.0049 * 20) * (10 ** -5))**3)/(970 * 9.8)) ** 0.5
    distance = d * 0.5 * (10 ** -3)
    dd = d * 0.05 * (10 ** -3)
    dt = 0.0005
    v = distance / t
    dv = m.sqrt((dd**2 * (1/t)**2) + (dt**2 * (distance/(t**2))**2))
    dV = 0.5
    vterm = (v**1.5) / V
    q = piterm * sqrt * vterm
    C = piterm*sqrt
    dVterm = (dV**2 * ((distance * v**(3/2) * C)/V**2)**2)
    dvterm = (dv**2 * (((distance * v**0.5 * C)/(V))* 1.5)**2)
    dq = m.sqrt(dVterm + dvterm)
    #print(v)
    n = q / (1.6 * (10 ** -19))
    #print(V, "+-", dV, "|", distance, "+-", dd , "|", t, "+-", dt, "|", v, "+-", dv, "|", q, "+-", dq)
    print(dq)
    sigq.append(dq)
    return q

for i in range(len(array)):
    q.append(e(array[i][0],array[i][1],array[i][2]))

q = np.array(q)

sigq = np.array(sigq)

diff = []
for i in range(0, len(q)):
    for j in range(0, len(q)):
        diff.append(abs(q[i] - q[j]))
        
diff.sort()
while(diff[0] == 0):
    diff.pop(0)
diff = np.array(diff)
avg = np.mean(diff)
e = []
for i in range(len(q)):
    e.append(q[i] - avg)
e = np.array(e)
print(np.mean(e))
print(np.mean(sigq))


