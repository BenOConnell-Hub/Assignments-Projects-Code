import numpy as np
import matplotlib.pyplot as plt

#Given values

R = 22 #Ohms
C = 0.1E-6 #Farad
L = 0.47E-3 #Henry
'''
R = 50
C = 100E-9
L = 100
'''
# Frequency range (logarithmic spacing)
frequencies = np.logspace(1, 7, 50000)  # From 10 Hz to 10 MHz
omega = 2 * np.pi * frequencies  # Angular frequency

# Calculate gains
GR = 1/(np.sqrt(1+(((omega*L)/R) - (1/(R*omega*C)))**2))
GL = ((omega*L)/R)*(1/(np.sqrt(1+(((omega*L)/R) - (1/(R*omega*C)))**2)))
GC = (1/(omega*R*C))*(1/(np.sqrt(1+(((omega*L)/R) - (1/(R*omega*C)))**2)))

omega_0 = 1/(np.sqrt(L*C))
f_0 = omega_0/(2*np.pi)
del_w = R/L
del_f = del_w/(2*np.pi)

idx_f1 = np.where(GR >= 0.707)[0][0] 
idx_f2 = np.where(GR >= 0.707)[0][-1]  

f1 = frequencies[idx_f1]
f2 = frequencies[idx_f2]
Q = (1/R)*(np.sqrt(L/C))
#Q = 1/(omega_0 *R*C)
#Q = omega_0/(del_w)
#Q = omega_0/((f2-f1)*(2*np.pi))

print("Delta f according to the graph =",f2-f1)
print("Delta f according to theory =",del_f)
print("Quality Factor =",Q)
print("Natural Angular Frequency =",f_0)

freq = np.array([100, 1000, 8000,16000, 20000, 22500, 23500, 28000, 40000, 64000, 200000, 500000, 1500000, 5000000])

GCT = np.array([1, 1, 1.111161679, 1.57140245, 1.652270703, 1.416595563, 1.230799527, 0.806440958, 0.341408591, 0.125013333, 0.019222441, 0,0,0])
GLT = np.array([0, 0, 0.200022756, 1, 1.652270703, 1.749786689, 1.692398582, 1.548307184, 1.268731269, 1.083733333, 1, 1, 1, 1])
GRT = np.array([0, 0.019222441,0.155535328,0.42859755,0.521816563,0.5,0.461599055,0.387118084,0.19517982,0.125013333,0.038444882,0.019222441,0,0])

RL = 23.83
NGR = (R)/(np.sqrt(((R+RL)**2) + (omega*L - (1/(omega*C)))**2))
NGL = ((omega*L)/R)*((R)/(np.sqrt(((R+RL)**2) + (omega*L - (1/(omega*C)))**2)))
NGC = (1/(omega*R*C))*((R)/(np.sqrt(((R+RL)**2) + (omega*L - (1/(omega*C)))**2)))

#Plot Gains
plt.figure(figsize=(10, 6))
plt.plot(frequencies, GR, label='$G_R$ - Theoretical', color='blue')
plt.plot(frequencies, GC, label='$G_C$ - Theoretical', color='red')
plt.plot(frequencies, GL, label='$G_L$ - Theoretical', color='green')

#plt.scatter(freq, GRT, label ='$G_R$ - Experimental', color='cyan')
#plt.scatter(freq, GCT, label ='$G_C$ - Experimental', color='orange')
#plt.scatter(freq, GLT, label='$G_L$ - Experimental', color='magenta')

plt.axvline(f_0, color = 'purple', label = '$f_0$ - Theoretical', linestyle = 'dashed')
plt.axvline(f1, color = 'pink', label = '$\Delta f$ - Theoretical', linestyle = 'dashed')
plt.axvline(f2, color = 'pink', label = '$\Delta f$ - Theoretical', linestyle = 'dashed')
plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(frequencies, NGR, label='$G_R$ - New Theoretical', color='blue')
plt.scatter(freq, GRT, label ='$G_R$ - Experimental', color='cyan')

plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(frequencies, NGC, label='$G_C$ - New Theoretical', color='red')
plt.scatter(freq, GCT, label ='$G_C$ - Experimental', color='orange')

plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()

plt.figure(figsize=(10, 6))

plt.plot(frequencies, NGL, label='$G_L$ - New Theoretical', color='green')
plt.scatter(freq, GLT, label='$G_L$ - Experimental', color='magenta')

plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()


'''

RL = 23.83
NGR = (R)/(np.sqrt(((R+RL)**2) + (omega*L - (1/(omega*C)))**2))
NGL = ((omega*L)/R)*((R)/(np.sqrt(((R+RL)**2) + (omega*L - (1/(omega*C)))**2)))
NGC = (1/(omega*R*C))*((R)/(np.sqrt(((R+RL)**2) + (omega*L - (1/(omega*C)))**2)))

plt.figure(figsize=(10, 6))
plt.plot(frequencies, NGR, label='$G_R$ - Theoretical', color='blue')
plt.scatter(freq, GRT, label ='$G_R$ - Experimental', color='cyan')

plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()
'''

