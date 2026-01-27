import matplotlib.pyplot as plt
import numpy as np


#Problem 2 graphing
#Read data from file "data1.dat"
data = np.loadtxt('data1.dat')
x = data[:, 0]  
y = data[:, 1]  

#Assume uncertainty sigma = 1.0 for all measurements
sigma = np.ones_like(y)

#Values from c++ code - Assign 3- Prob 2
a = 0.514102
b = 0.0202415

#Generate data for the fitted line to plot
x_fit = np.linspace(min(x), max(x), 100)
y_fit = a + b * x_fit

#Plotting the data points and the fitted line
plt.figure(figsize=(8, 6))
plt.errorbar(x, y, yerr=sigma, fmt='o', label='Measured data', capsize=5)
plt.plot(x_fit, y_fit, label=f'Fitted line: f(x) = {a:.4f} + {b:.4f}x', color='red')
plt.xlabel('Position along the wire (cm)')
plt.ylabel('Voltage (V)')
plt.title('Least-Squares Fit of Voltage vs Position')
plt.legend()
plt.show()