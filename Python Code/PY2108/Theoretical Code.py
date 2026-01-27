import numpy as np
import matplotlib.pyplot as plt

# Given values
R = 1000  # Resistance in Ohms
C = 4.7e-9  # Capacitance in Farads

# Frequency range (logarithmic spacing)
frequencies = np.logspace(1, 7, 50)  # From 10 Hz to 10 MHz, 500 points
omega = 2 * np.pi * frequencies  # Angular frequency

# Calculate gains and phase shifts
G_R = (omega*R*C) / np.sqrt(1 + (omega*R*C)**2)
G_C = 1 / np.sqrt(1 + ((omega * C * R))**2)

phi_R = np.arctan(1 / (omega * R * C))
phi_C = np.arctan(-1*(omega * R * C))

# Convert phase shifts to degrees
phi_R_deg = np.degrees(phi_R)
phi_C_deg = np.degrees(phi_C)

#Experimental Data
x1 = np.array([100, 1200, 4000, 12000, 28000, 48000, 95000, 180000,470000, 1E6, 2E6, 5E6])
y1 = np.array([1, 1, 0.9875, 0.9295, 0.7635, 0.5813, 0.3466, 0.2, 0.0933, 0.0373, 0.018, 0.00611])

y2 = np.array([0, -3.024, -4.608, -20.736, -40.32, -51.84, -75.24, -84.24, -87.984, -92.16, -92.16, -93.6])

p = np.array([10, 10E6])
q = np.array([0.707,0.707])
# Plot gains
plt.figure(figsize=(10, 6))
plt.plot(frequencies, G_R, label='$G_R$ - Theoretical', color='blue')
plt.plot(frequencies, G_C, label='$G_C$ - Theoretical', color='red')
plt.scatter(x1, y1, label = '$G_C$ - Experimental', color = 'orange')
plt.plot(p,q, label = 'Frequency Response', color = 'green')
plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()

# Plot phase shifts
plt.figure(figsize=(10, 6))
plt.plot(frequencies, phi_R_deg, label='$\phi_R$', color='blue')
plt.plot(frequencies, phi_C_deg, label='$\phi_C$', color='red')
plt.scatter(x1, y2, label = '$\phi_C$ - Experimental', color = 'orange')
plt.xscale('log')
plt.title('Phase Shifts vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Phase Shift (degrees)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()