import numpy as np
import matplotlib.pyplot as plt

freq = np.array([10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 12800, 25600, 51200, 102400, 204800, 409600, 819200, 1638400, 3276800, 5000000])
data = np.array([0.01074078, 0.010883706, 0.011125284, 0.010242896, 0.011523616, 0.011072384, 0.012787557, 0.017902611, 0.023017655, 0.035805624, 0.061380766, 0.107416893, 0.181234232, 0.300546656, 0.668804469, 0.948148601, 1, 0.990655898, 0.984124136])

plt.figure(figsize=(10, 6))
plt.scatter(freq, data, label='$G_L$ - Experimental', color='magenta')

plt.xscale('log')
plt.title('Gains vs Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()