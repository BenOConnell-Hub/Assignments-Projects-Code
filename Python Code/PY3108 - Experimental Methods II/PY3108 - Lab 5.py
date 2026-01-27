import matplotlib.pyplot as plt
import numpy as np
import Control_Examples as CE


devices = ['Red', 'Amber', 'Green', 'Blue', 'Laser']
Slam = [0.434, 0.403, 0.31, 0.217, 0.465]
Rf =  13800
#For Laser Rf = 1000
#For every other device Rf = 13800

'''
for i in range(0, len(devices)):
    playing = True
    while playing == True:
        ans = input(f'Is the device = {devices[i]}, Y or N: ')
        ans = ans.upper()
        if ans == 'Y':
            playing = False
    
    filename = devices[i] + '.txt'
    CE.Current_Sweep_V1(100, filename, 0, 30, 29.8)
'''
for i in range(0, len(devices)):
    filename = devices[i] + '.txt'
    data = np.loadtxt(filename)
    
    VIA = data[:,1]
    VW2 = data[:,2]
    VW4 = data[:,3]
    Vout = data[:,4]
    
    I = VIA * 29.8     # mA
    
    # Photocurrent → mA
    if devices[i] == 'Laser':
        Iph = (Vout/1000) * 1000
    else:
        Iph = (Vout/Rf) * 1000
    
    P = Iph / Slam[i]

    # ========= LINEAR FIT SECTION =========
    N = len(I)
    half_index = N // 2

    # take only last half
    I_half = I[half_index:]
    VW4_half = VW4[half_index:]

    # linear fit: slope_mA is in units V/mA
    slope_mA, intercept = np.polyfit(I_half, VW4_half, 1)

    # Resistance in ohms (convert mA → A)
    R_device = slope_mA * 1000     # ohms

    # Create fitted line over full I-range
    fit_line = slope_mA * I + intercept

    # ========= PLOTTING =========
    fig, ax1 = plt.subplots(figsize=(7, 5))
    
    # Left Y-axis for voltages
    ax1.plot(I, VW2, label='VW2 (V)', color='tab:blue', linewidth=2)
    ax1.plot(I, VW4, label='VW4 (V)', color='tab:orange', linewidth=2)

    # Plot line of best fit
    fit_label = (f'Best Fit: V = {slope_mA:.4f}·I + {intercept:.3f}\n'
                 f'R = {R_device:.1f} Ω')
    ax1.plot(I, fit_line, '--', color='black', linewidth=2, label=fit_label)

    ax1.set_xlabel('Current, I (mA)')
    ax1.set_ylabel('Voltage (V)')
    ax1.grid(True, linestyle='--', alpha=0.6)

    # Right Y-axis for power
    ax2 = ax1.twinx()
    ax2.plot(I, P, label='Power (mW)', color='tab:red', linewidth=2, linestyle='--')
    ax2.set_ylabel('Optical Power (mW)')

    # Merge legends
    lines_1, labels_1 = ax1.get_legend_handles_labels()
    lines_2, labels_2 = ax2.get_legend_handles_labels()
    ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc='best')
    
    if devices[i] == 'Laser':
        plt.title(f'{devices[i]} Characteristics')
    else:
        plt.title(f'{devices[i]} LED Characteristics')
    plt.tight_layout()
    plt.show()
    
        
    



