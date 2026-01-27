import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import math as m
import Control_Examples

names = ['Resistor 1', ' Resistor 01', ' Resistor 001', 'Diode']
K = 29.8

'''
for i in range(0,len(names)):
    current = names[i]
    filename = current + '.txt'
    
    running = True
    while running == True:
        pre = input(f'Is your load = {current} \n')
        pre = pre.upper()
        if pre == 'Y':
            Control_Examples.Current_Sweep_V1(40, filename, 0, 80, 29.8)
            running = False
'''


for i in range(0,len(names)):
    current = names[i]
    filename = current + '.txt'
    data = np.loadtxt(filename)

    
    VIA = data[:,1]
    VLW2 = data[:,2]
    VLW4 = data[:,3]
    VP = data[:,4]
    
    I = VIA * K
    
    VLW2 = VLW2 - VP
    VLW4 = VLW4 - VP


    plt.scatter(I, VLW2, label= "2 Point")
    plt.scatter(I, VLW4, label= "4 Point")
    
    if current == 'Diode':
        a1, b1 = np.polyfit(I[20:], VLW2[20:], 1)
        a2, b2 = np.polyfit(I[20:], VLW4[20:], 1)
        
        
        plt.plot(I, a1*I+b1, linestyle='--', linewidth=2, label = f'LOBF - W2 - Resistance = {a1*1000}')
        plt.plot(I, a2*I+b2, linestyle='--', linewidth=2, label = f'LOBF - W4 - Resistance = {a2*1000}')
        
        
    else:
        a1, b1 = np.polyfit(I, VLW2, 1)
        a2, b2 = np.polyfit(I, VLW4, 1)
        
        
        plt.plot(I, a1*I+b1, linestyle='--', linewidth=2, label = f'LOBF - W2 - Resistance = {a1*1000}')
        plt.plot(I, a2*I+b2, linestyle='--', linewidth=2, label = f'LOBF - W4 - Resistance = {a2*1000}')

    title = 'Voltage Across Load against Current (' + current + ')'
    
    if current == ' Resistor 001':
        print(VLW4)
    plt.title(title)
    plt.xlabel('Current (mA)')
    plt.ylabel('Voltage Across Load (V)')
    plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
    plt.minorticks_on()
    plt.legend()
    plt.show()
    


#Testing for Extra Mark
Resistors = ['10','22', '56', '100', '510', '1000','5000','10000', '56000', '100000','1000000']

'''
for i in range(0,len(Resistors)):
    current = Resistors[i]
    filename = 'Test Resistor ' + current + '.txt'
    
    running = True
    while running == True:
        pre = input(f'Is your resistor = {current} \n')
        pre = pre.upper()
        if pre == 'Y':
            Control_Examples.Current_Sweep_V1(40, filename, 0, 80, 29.8)
            running = False
  '''   
for i in range(0,len(Resistors)):
    current = Resistors[i]
    filename = 'Test Resistor ' + current + '.txt'
    data = np.loadtxt(filename)

    
    VIA = data[:,1]
    VLW2 = data[:,2]
    VLW4 = data[:,3]
    VP = data[:,4]
    
    I = VIA * K
    
    VLW4 = VLW4 - VP
    
    if Resistors[i] == '10':
        plt.plot(I, VLW4, label = 'Original Resistor')
    else:
        plt.plot(I, VLW4, label= f'4 Point - Resistor = {Resistors[i]}')
    
title = 'Testing different 4 Point Resistor Values'

plt.title(title)
plt.xlabel('Current (mA)')
plt.ylabel('Voltage Across Load (V)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()



