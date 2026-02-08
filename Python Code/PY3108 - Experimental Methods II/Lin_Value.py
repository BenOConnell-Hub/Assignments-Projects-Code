import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import math as m

def lin_value_calc(X = np.array([0]), #X values (List or Numpy Array)
                   Y = np.array([0]), #Y Values (List or Numpy Array)
                   x_line = 0, #X coordinate for the displayed equation of the line of best fit (Float/Integer)
                   y_line = 0, #Y coordinate for the displayed equation of the line of best fit (Float/Integer)
                   XR_line = 0, #X coordinate for the displayed R^2 value (Float/Integer)
                   YR_line = 0, #Y coordinate for the displayed R^2 value (Float/Integer)
                   x_label = '', #X label (String)
                   y_label = '', #Y label (String)
                   g_title = '', #Graph Title (String)
                   errors_x = 0, #Error values for X (List or Float/Integer)
                   errors_y = 0, #Error values for Y (List or Float/Integer)
                   y_at_zero = True, #Force graph to start at X = 0 (Boolean)
                   x_at_zero = True, #Force graph to start at Y = 0 (Boolean)
                   y_max = 0, #Max Length of Y axis, 0 means no restriction (Float/Integer)
                   x_max = 0): #Max Length of X axis, 0 means no restriction (Float/Integer)
    
    print("Plotting",g_title)
    #Reshaping x coordinates for LinearRegression()
    
    #Convert Lists to numpy arrays if needed
    if not isinstance(X, np.ndarray):
        X = np.array(X)
        
    if not isinstance(Y, np.ndarray):
        Y = np.array(Y)
    
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
    plt.text(XR_line, YR_line, "R^2 = " + "{:.4f}".format(R2), size = 14)
    
    #Showing Graph
    plt.legend(title = 'Legend')
    plt.show()

def lin_value_calc_cent(
    X, Y, x_line, y_line, XR_Line, YR_Line,
    x_label, y_label, g_title,
    errors_x, errors_y,
    y_at_zero, x_at_zero, y_max, x_max
):
    print("Plotting", g_title)

    # Convert to arrays
    X = np.asarray(X)
    Y = np.asarray(Y)

    N = len(X)

    # Re-centre X
    X_mean = np.mean(X)
    Xc = X - X_mean

    # Fit using centred X
    Xc_shaped = Xc.reshape(-1, 1)
    model = LinearRegression().fit(Xc_shaped, Y)

    slope = model.coef_[0]
    intercept = model.intercept_   # this is now ȳ

    print("Slope:", slope)
    print("Intercept (at x = mean):", intercept)

    # Predictions
    Y_pred = slope * Xc + intercept

    # Residual variance
    residuals = Y - Y_pred
    sigma2 = np.sum(residuals**2) / (N - 2)

    # Uncertainties
    slope_error = np.sqrt(sigma2 / np.sum(Xc**2))
    intercept_error = np.sqrt(sigma2 / N)

    print("Error in slope:", slope_error)
    print("Error in intercept:", intercept_error)

    # R^2
    R2 = r2_score(Y, Y_pred)
    print("R^2 =", R2)
    print("")

    # Plot
    plt.scatter(X, Y, color='purple', label='Data Points')

    xfit = np.linspace(min(X), max(X), 500)
    yfit = slope * (xfit - X_mean) + intercept
    plt.plot(xfit, yfit, '--', color='steelblue', linewidth=2, label='Line of Best Fit')

    plt.text(x_line, y_line,
             f'y = {intercept:.4f} + {slope:.6f}(x - x̄)',
             size=13)

    plt.text(XR_Line, YR_Line, f'R² = {R2:.4f}', size=13)

    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(g_title)

    plt.errorbar(X, Y, xerr=errors_x, yerr=errors_y, fmt='o')

    if y_at_zero:
        plt.ylim(bottom=0)
    if y_max != 0:
        plt.ylim(top=y_max)
    if x_at_zero:
        plt.xlim(left=0)
    if x_max != 0:
        plt.xlim(right=x_max)

    plt.legend()
    plt.show()

