import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import math as m

def lin_value_calc(X, Y, x_line, y_line, x_label, y_label, g_title, errors_x, errors_y, y_at_zero,x_at_zero, y_max, x_max):
    print("Plotting",g_title)
    #Reshaping x coordinates for LinearRegression()
    X_shaped = X.reshape(-1,1)
    
    #Slope calc
    model = LinearRegression().fit(X_shaped, Y)
    slope = model.coef_[0]
    
    #Intercept calc
    intercept = model.intercept_
    
    #Displaying slope and intercept
    print("Slope is: ",slope)
    print("Intercept is: ", intercept)
    
    #Mean of X coords & Y coords
    mean_x = np.mean(X_shaped)
    mean_y = np.mean(Y)
    
    #Calculating intercept error
    intercept_ols = mean_y - slope * mean_x
    intercept_error_ols = np.std(Y - (slope * X_shaped + intercept_ols))
    print("Error in intercept is: ",intercept_error_ols)
    
    #Preparing line of best fit
    a, b = np.polyfit(X, Y, 1)
    
    #Plotting Data points using X values and Y values
    plt.scatter(X, Y, color ='purple', label = 'Data Points')
    
    #Plotting Line of best fit
    plt.plot(X, a*X+b, color='steelblue', linestyle='--', linewidth=2, label = 'Line of Best Fit')
    plt.text(x_line, y_line,'y = ' + '{:.4f}'.format(b) + ' + {:.8f}'.format(a) + 'x', size=14)
    
    #Labelling title and axes
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    #plt.legend(title = 'Legend')
    plt.title(g_title)
    
    #Adding Error bars
    plt.errorbar(X, Y, xerr = errors_x, yerr = errors_y, fmt = "o")
    
    #Start Y at zero
    if y_at_zero == True:
        plt.ylim(bottom=0)
        
    #Set max Y
    if y_max != 0:
        plt.ylim(top = y_max)
        
    #Start X at zero 
    if x_at_zero == True:
        plt.xlim(left = 0)
        
    #Set max Y
    if x_max != 0:
        plt.xlim(right = x_max)
        
    #Calculating Slope error
    sum_of_y = 0.0
    sum_of_x = 0.0
    for i in range(0, len(Y)):
        yhat = b + a*X[i]
        sum_of_y = sum_of_y + ((Y[i]-yhat)**2)
        sum_of_x = sum_of_x + (m.sqrt((X[i]-mean_x)**2))
    sum_of_y = m.sqrt(sum_of_y/(len(Y)- 2))
    print("Error in slope is: ",(sum_of_y/sum_of_x))
    
    #Calculating R-squared value
    y_pred = b + a*X
    Yf = Y.flatten()
    y_pred = y_pred.flatten()

    R2 = r2_score(Yf, y_pred)
    print("The R-squared value is: ",R2)
    print("")
    plt.text(0, 0.04, "R^2 = " + "{:.4f}".format(R2), size = 14)
    
    #Showing Graph
    plt.legend(title = 'Legend')
    plt.show()
    
    
    

plt.figure(figsize=(10, 6))

v_values = [0.1, 0.7, 1.3, 1.9, 2.5, 3.1, 3.3]
I_values = [0.0001, 0.0002, 0.0003, 0.0004, 0.0005, 0.0006, 0.0007]

for i in range(0,7):
    data = np.loadtxt(f'Test_{i}.txt')
    
    VB = i
    
    VCC = data[:,0]
    VA = data[:,1]
    VB = data[:,2]
    VC = data[:,3]
    VD = data[:,4]
    
    VCE = VA - VB
    
    IC = VCE / 10
    
    VBE = VC - VD
    
    IB = VBE / 3270
    
    sumofIB = 0
    for j in range(0, len(IB)):
        sumofIB = sumofIB + IB[j]
    avg_IB = sumofIB / len(IB)
    
    plt.plot(VB, IC, label= f"$I_B$ = {I_values[i]} A")

plt.title('Collector Current vs Collector Voltage')
plt.xlabel('Collector Voltage (V)')
plt.ylabel('Collector Current (A)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()

for i in v_values:
    data = np.loadtxt(f'Sweep_Data_Voltage_{i}_2.txt')
    
    VB = i
    
    VCC = data[:,0]
    VA = data[:,1]
    VB = data[:,2]
    VC = data[:,3]
    VD = data[:,4]
    
    VCE = VA - VB
    
    IC = VCE / 10
    
    VBE = VC - VD
    
    IB = VBE / 3270
    
    '''
    sumofIB = 0
    for j in range(0, len(IB)):
        sumofIB = sumofIB + IB[j]
    avg_IB = sumofIB / len(IB)
    '''
    
    
    if i == 3.1:
        plt.scatter(IB, IC, label= f"VCC = {i} (V)")
        lin_value_calc(IB, IC, 0, 0.06, 'Base Current (A)', 'Collector Current (A)', 'Collector Current vs Base Current', 0, 0, False, False, 0, 0)
    
    #plt.plot(IB, IC, label= f"VCC = {i} (V)")
'''
plt.title('Collector Current vs Base Current')
plt.xlabel('Base Current (A)')
plt.ylabel('Collector Current (A)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()
'''

data1 = np.loadtxt("Test.txt")

VC = data1[:,3]
VD = data1[:,4]

IB = (VC - VD)/3270

avg_IB = np.mean(IB)
print(avg_IB)



