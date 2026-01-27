import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import math as m
import Control_Examples

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
    plt.text(0, 70, "R^2 = " + "{:.4f}".format(R2), size = 14)
    
    #Showing Graph
    plt.legend(title = 'Legend')
    plt.show()
    return a

#Control_Examples.Linear_Sweep_V1(20, 'Characterisation.txt')

data = np.loadtxt("Characterisation.txt")

Load = 15
R1 = 1.8
Vin = data[:,0]
VIA = data[:,1]
VL = data[:,2]

I = VL/Load
ImA = I*1000

'''
print("-" * 66)
print(f"| {'Vin(V)':^10} | {'VL(V)':^10} | {'VR(V)':^10} | {'VT(V)':^10} | {'I(A)':^10} |")
print("-" * 66)
for i in range(len(Vin)):
    print(f"| {Vin[i]:^10.5f} | {VL[i]:^10.5f} | {VR[i]:^10.5f} | {VT[i]:^10.5f} | {I[i]:^10.5f} |")
print("-" * 66)
'''


K = lin_value_calc(Vin, ImA, 0, 80, 'Input Voltage (V)', 'Output Current (mA)', 'Output Current vs Input Voltage', 0, 0, False, False, 0, 0)
print("Calibration value K =",K)
KL = lin_value_calc(VIA, ImA, 0, 80, 'Feedback Voltage (Vfb)', 'Output Current (mA)', 'Output Current vs Feedback Voltage', 0, 0, False, False, 0, 0)
print("Calibration value KL =",KL)