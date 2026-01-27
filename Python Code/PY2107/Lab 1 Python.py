import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import math as m

def f(x):
    return (3/14)*x + (11/7)

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
    plt.text(0.6, 15, "R^2 = " + "{:.4f}".format(R2), size = 14)
    
    #Showing Graph
    
    x = np.linspace(-10,10,100)
    fp = np.vectorize(f)
    plt.plot(x, fp(x), label = "Theoretical Equation")
    plt.legend(title = 'Legend')
    plt.show()
    
    

#Copy and paste comment below and change relevant fields to desired values
#lin_value_calc(X values(numpy array), Y values(numpy array), X coord for bfl eq., Y coord for bfl eq., Title of x axis, Title of y axis, Title of Graph, array of errors for x, array of errors for y, y coord Start at 0 (True or False), x coord start at 0 (True or False), maximum y value (for default enter 0), maximum x value (default enter 0)) 


#Lab 3
xpoints = np.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ypoints = np.array([-0.55, -0.34, -0.13, 0.08, 0.3, 0.5, 0.72, 0.93, 1.14, 1.35, 1.55, 1.76, 1.96, 2.18, 2.39, 2.63, 2.85, 3.06, 3.26, 3.47, 3.70])

xerrors = 0
yerrors = 0

lin_value_calc(xpoints, ypoints, -9, 2 , 'Vin (V)', 'Vout (V)', 'Output Voltage versus the Input Voltage', xerrors, yerrors, False, False, 0, 0)










