import time
import sys
import Control_Examples as CE
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def Temp(R):

    A_1 = 0.00335401643468053

    B_1 = 0.00025698501802

    C_1 = 0.0000026201306709

    D_1 = 0.000000063830907998

    R_25 = 15000

    LR = math.log(R / R_25)

    iT = A_1 + B_1 * LR + C_1 * LR**2 + D_1 * LR**3

    return 1 / iT - 273.15

def RT_Calc(Vout, G):
    nominator = G*5.0 -2*float(Vout)
    denominator = G*5.0 + 2*float(Vout)
    
    return float((nominator/denominator)*15000)

'''
Task 1:
In order to take a measurement and display that measurement continuously the following code should be used:

while True:
    print(f"\rCurrent value: {x}", end="", flush=True)
    
Need the \r to return the cursor to the start of the same line, end = '' to remain on the same line and flush = True  to clear the console or:

for i in range(0,10):
    sys.stdout.write(f"\rYour mom: {i}")
    sys.stdout.flush()
    time.sleep(0.1)
But using print(\r, end ='', flush = True)
Is probably easier

Can place this into any existing code. Will only need to run the measurement taking aspect of the code multiple times
such as:
the_dev.ReadSingleVoltage('A3')

Task 2:
To measure the way a parameter changes with time use:
start = time.time()

Measurement code such as:
the_dev.ReadSingleVoltage('A3')

end = time.time()
deltaT = end - start

To create a series of measurements based on time the following code can be used. This is for Fast

start = time.time()
voltage_data = []
count = 0
while True:
    val = the_dev.ReadSingleVoltage('A3')
    deltaT = time.time() - start
    voltage_data.append([deltaT, val])
voltage_data = numpy.array(voltage_data)

For slow:
start = time.time()
voltage_data = []
count = 0
while True:
    val = the_dev.ReadSingleVoltage('A3')
    deltaT = time.time() - start
    voltage_data.append([deltaT, val])
    time.sleep(0.5)
voltage_data = numpy.array(voltage_data)

This code can be used to loop for as long as youd like and stop whenever using Ctrl + C

try:
    x = 0
    while True:
        print(f'\rCounter {x :.3f}', end = '', flush = True)
        x += 1
        time.sleep(0.1)
        
except KeyboardInterrupt:
    print('\nLooping Stopped')
    
Time is always in seconds unless converted to something else. 

'''

#With LED
#CE.Multiple_Readings_V2()


#Without LED
#CE.Multiple_Readings_V3()

CE.Testing_LED()

filename = 'Data.txt'
#CE.Slow_Time_Measurement('A3', 0.1, filename)


data = np.loadtxt(filename)

t = data[:,0]
Vout = data[:,1]

Temperature = []
for i in range(0,len(Vout)):
    RT = RT_Calc(Vout[i], 4.03)
    Hot = Temp(RT)
    Temperature.append(Hot)
Temperature = np.array(Temperature)

# ----------------------------------------------------------------------
# Exponential Decay Fit for t >= 25 s
# ----------------------------------------------------------------------

# Model function
def exp_decay(t, A, k, C):
    return A * np.exp(-k * t) + C

# Extract fitting region
mask = t >= 25
t_fit = t[mask]
T_fit = Temperature[mask]

# Initial guesses for A, k, C
A0 = T_fit[0] - T_fit[-1]
k0 = 0.05
C0 = T_fit[-1]

popt, pcov = curve_fit(exp_decay, t_fit, T_fit, p0=[A0, k0, C0])
A, k, C = popt

# Generate smooth curve for plotting
t_smooth = np.linspace(t_fit[0], t_fit[-1], 300)
T_smooth = exp_decay(t_smooth, A, k, C)

tau = 1/k
print(f"Time constant τ = {tau:.3f} s")

# ----------------------------------------------------------------------
# Plotting
# ----------------------------------------------------------------------

plt.plot(t, Temperature, label='Measured Temperature')
plt.plot(t_smooth, T_smooth, 'r--', linewidth=2,
         label=f'Fit: T(t) = {A:.2f}·e^(-{k:.3f}t) + {C:.2f}')

plt.title('Temperature versus Time')
plt.xlabel('Time (s)')
plt.ylabel('Temperature (°C)')
plt.grid(True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()
