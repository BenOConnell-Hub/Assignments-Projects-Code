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
    plt.legend(title = 'Legend')
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
    plt.text(2000, 30, "R^2 = " + "{:.4f}".format(R2), size = 14)
    #Showing Graph
    plt.show()

data = np.loadtxt('Data.txt')
x = data[:, 0]  
y = data[:, 1]

x = x*60
plt.plot(x,y)
plt.xlabel("t(s)")
plt.ylabel("T(Celcius)")
plt.title("Temperature of the water versus time")
plt.show()

def f(x):
    return m.log(x)
xpoints = data[30:, 0]
ypoints = data[30: , 1]
xpoints = xpoints*60


#lin_value_calc(X values(numpy array), Y values(numpy array), X coord for bfl eq., Y coord for bfl eq., Title of x axis, Title of y axis, Title of Graph, array of errors for x, array of errors for y, y coord Start at 0 (True or False), x coord start at 0 (True or False), maximum y value (for default enter 0), maximum x value (default enter 0)) 
lin_value_calc(xpoints, ypoints, 2000, 25, "t (s)" , "T (Celcius)", "Cooling of water and calorimeter over time", 0, 0, False, False, 0, 0)

#Adiabatic Index

periods = np.array([1.073, 1.12, 1.1267, 1.12, 1.103, 1.2167, 1.0767, 1.173, 1.1167])
'''
mass = 15.195/1000
dmass = 0.0005/1000

period = 1.125
dperiod = 0.04262953

v = 0.0115
dv = 0.00005

p = 101740.6226
dp = 1.8536

A = 2.01061E-4
dA = 5.0265E-7

gamma = 1.4


derT = (-8 * m.pi**2 * mass * v) / (period**3 * p * A**2)
derM = (4 * m.pi**2 * v) / (period**2 * p * A**2)
derV = (4 * m.pi**2 * mass) / (period**2 * p * A**2)
derP = (-4 * m.pi**2 * mass * v) / (period**2 * p**2 * A**2)
derA = (-8 * m.pi**2 * mass * v) / (period**2 * p * A**3)


dgamma = m.sqrt((dperiod**2 * derT**2) + (dmass**2 * derM**2) + (dv**2 * derV**2) + (dp**2 * derP**2) + (dA**2 * derA**2))
print(dgamma)



derM = (m.pi * m.sqrt(v)) / (m.sqrt(gamma*mass*p*A**2))
derV = (m.pi * m.sqrt(mass)) / (m.sqrt(gamma * v * p * A**2))
derP = (-m.pi * m.sqrt(v*mass)) / (p**(3/2) * m.sqrt(gamma*A**2))
derA = (-2*m.pi*m.sqrt(mass*v)) / (A**2 * m.sqrt(p*gamma))

dT = m.sqrt((dmass**2 * derM**2) + (dv**2 * derV**2) + (dp**2 * derP**2) + (dA**2 * derA**2))

print(dT)
'''


#Newtonian Cooling
'''
A = 0.00133571
dA = 5.8196984E-6

k = 0.00636
dk = 2.8773E-5

C = 482.2351
dC = 2.137896E-3

lam = 0.026

derA = (lam)/(k*C)
derk = (-lam*A)/(k**2 * C)
derC = (-lam*A)/(k*C**2)

db = m.sqrt((dA**2 * derA**2)+(dk**2 * derk**2) + (dC**2 * derC**2))
print(db)
'''
periods = periods * 3 - 0.135
periods = periods/3
print(np.mean(periods))








