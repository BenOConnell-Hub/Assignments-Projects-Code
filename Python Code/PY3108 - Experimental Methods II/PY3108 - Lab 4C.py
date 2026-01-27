import matplotlib.pyplot as plt
import numpy as np
import Control_Examples as CE

Colours = ['Red', 'Amber', 'Green', 'Blue']
#Colours = ['Blue']
Slam = [0.434, 0.403, 0.31, 0.217]
Currents = [0, 5, 10, 15, 20, 25, 30]
Gain = [0.5, 1]
Rph = [6900, 13800]
RGain = [2, 1]

'''
for j in range(0, len(Colours)):
    playing = True
    while playing == True:
        ans = input(f'Is the current LEDs colour = {Colours[j]}, Y or N: ')
        ans = ans.upper()
        if ans == 'Y':
            playing = False
    if  Colours[j] == 'Red':
        for k in range(0, len(Gain)):
            running = True
            while running == True:
                inp = input(f'Is your resistor = {Rph[k]}, Y or N: ')
                inp = inp.upper()
                if inp == 'Y':
                    running = False
            for i in range(0, len(Currents)):
                filename = Colours[j] + ' ' + 'Current_' + str(Currents[i]) + ' ' + str(Gain[k]) + '.txt'
                CE.Linear_Sweep_V3(-3, 1.3, Currents[i], 75, filename)
        
    else:
        for i in range(0, len(Currents)):
            filename = Colours[j] + ' ' + 'Current_' + str(Currents[i]) + '.txt'
            CE.Linear_Sweep_V3(-3, 1.3, Currents[i], 75, filename)

'''
for j in range(0, len(Colours)):
        
        if Colours[j] == 'Red':
            for k in range(0, len(Gain)):
                for i in range(0, len(Currents)):
                    filename = Colours[j] + ' ' + 'Current_' + str(Currents[i]) + ' ' + str(Gain[k]) + '.txt'
                    data = np.loadtxt(filename)
                    
                    Vbias = data[:,0]
                    Vout = data[:,1]
                    VIA = data[:,2]
                    
                    Iph = Vout/Rph[k] * 1000 * -1
                    I = VIA * 29.8
                    IL = round(np.sum(I)/len(I),2)
                    
                    Op = round(abs(Iph[-1])/Slam[j],2)
                    
                    plt.plot(Vbias, Iph, label= f"$I_L$ = {IL} mA, $O_P$ = {Op} mW")
                
                plt.title(f'Vbias versus Photocurrent - {Colours[j]} - Gain = {RGain[k]}')
                plt.xlabel('Vbias (V)')
                plt.ylabel('Photocurrent (mA)')
                plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
                plt.minorticks_on()
                plt.legend()
                plt.show()
            
        else:
            for i in range(0, len(Currents)):
                filename = Colours[j] + ' ' + 'Current_' + str(Currents[i]) + '.txt'
                data = np.loadtxt(filename)
                
                Vbias = data[:,0]
                Vout = data[:,1]
                VIA = data[:,2]
                
                Iph = Vout/Rph[0] * 1000 * -1
                I = VIA * 29.8
                IL = round(np.sum(I)/len(I),2)
                
                Op = round(abs(Iph[-1])/Slam[j],2)
                
                plt.plot(Vbias, Iph, label= f"$I_L$ = {IL} mA, $O_P$ = {Op} mW")
            
            plt.title(f'Vbias versus Photocurrent - {Colours[j]}')
            plt.xlabel('Vbias (V)')
            plt.ylabel('Photocurrent (mA)')
            plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
            plt.minorticks_on()
            plt.legend()
            plt.show()
