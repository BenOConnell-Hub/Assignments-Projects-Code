import matplotlib.pyplot as plt
import numpy as np

data1 = np.loadtxt("Circuit 1 Sweep.txt")
data2 = np.loadtxt("Circuit 3 Sweep.txt")

I1 = data1[:,1]/100
I2 = (data1[:,1]*0.6188)/10


Vin1 = data1[:,0]


plt.plot(Vin1, I1, label = 'Circuit 1')
plt.plot(Vin1, I2, label = 'Circuit 3')

plt.title('Input Voltage versus Current')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()
