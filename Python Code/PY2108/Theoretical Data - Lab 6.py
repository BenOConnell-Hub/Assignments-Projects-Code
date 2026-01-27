import numpy as np
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

# Read data from the file
data1 = np.loadtxt("Linear Sweep Data.txt")  # Load text file

# Extract columns
v1_values = data1[:, 0]  # First column
x1_axis = data1[:, 1]  # Second column

y1_axis = (v1_values - x1_axis) / 33

data2 = np.loadtxt("Reverse Biased Data.txt")

v2_values = data2[:,0]
x2_axis = data2[:,1]

y2_axis = (v2_values - x2_axis) / 10E6

#x2_axis = x2_axis*(-1)

sumofI = 0
for i in range(0, len(y2_axis)):
    sumofI = sumofI + y2_axis[i]
average = sumofI/len(y2_axis)
print(average)





# Given Constants
q = 1.603E-19  # Charge of an electron (C)
kb = 1.38E-23  # Boltzmann constant (J/K)

#I0 = 0.25E-5  # Reverse saturation current (A)
T = 300  # Temperature (K)
VD = np.linspace(-0.2, 3.3, 1000)  # Voltage range

I0_values = [1E-14, 0.2E-9, 0.25E-7,0.51E-6, 0.4E-5]
b_values = [1, 1.5, 2, 2.5, 3]  # Ideality factors

x1 = np.array(x1_axis)
y1 = np.array(y1_axis)
x2 = np.array(x2_axis)
y2 = np.array(y2_axis)

x = np.concatenate((x1, x2))
y = np.concatenate((y1, y2))
I0 = 1.1025E-9
def Current(x, B, C):
    return C*(np.exp((q*x)/(B * kb *T))-1)

parameters, covariance = curve_fit(Current, x1_axis, y1_axis, bounds = [[1.0, -np.inf],[np.inf, np.inf]])
beta = parameters[0]
I0 = parameters[1]
#T = parameters[2]


print("The ideality factor that fits the data best is:", beta)
print(I0)

plt.figure(figsize=(10, 6))

# Loop through different ideality factors
'''
for i in range(0,len(b_values)):
    # Avoid overflow by limiting exponent argument
    exp_argument = np.clip((q * VD) / (b_values[i] * kb * T), -100, 100)

    # Compute diode current with overflow protection
    I = I0_values[i] * (np.exp(exp_argument) - 1)

    # Find the index where I exceeds 0.08 A
    max_I_index = np.argmax(I > 0.08)  # First occurrence where I > 0.08

    # Trim the data arrays to remove the flat line effect
    VD_trimmed = VD[:max_I_index]
    I_trimmed = I[:max_I_index]

    # Plot the IV curve for this ideality factor
    plt.plot(VD_trimmed, I_trimmed, label=f'b = {b_values[i]} & $I_0$ = {I0_values[i]}')
'''
#I0 = I0*-1

#beta = 4.5
#I0 = 2.8025E-5

I = I0*(np.exp((q*VD)/(beta * kb* T))-1)
max_I_index = np.argmax(I > 0.08)
VD_trimmed = VD[:max_I_index]
I_trimmed = I[:max_I_index]
plt.plot(VD_trimmed, I_trimmed, label ='Fitted Equation')

# Plot formatting
plt.title('Voltage across the Diode vs Current for Different Ideality Factors')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.scatter(x1_axis, y1_axis, label="Experimental Data", color="pink")
#plt.scatter(x2_axis, y2_axis, label = "Experimental Data")
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()
'''

plt.figure(figsize=(10, 6))
#plt.scatter(x2_axis, y2_axis, label = "Experimental Data")
plt.title('Voltage across the Diode vs Current')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.scatter(x2_axis, y2_axis, label = "Experimental Data")
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()
'''
