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
    plt.text(1, 3.25E-6, "R^2 = " + "{:.4f}".format(R2), size = 14)
    #Showing Graph
    plt.show()


#numOfPixs1 = 27/8650
numOfPixs1 = 3.24/1076

pixLeft1 = [510, 438, 380, 333, 292, 257, 222, 191, 162, 133, 106, 80, 52, 30]
pixRight1 = [887, 961, 1020, 1070, 1115, 1158, 1195, 1232, 1267, 1299, 1331, 1361, 1388, 1416]
pixErrLeft1 = [505, 958, 1019, 1067, 1113, 1151, 1191, 189, 1262, 131, 1328, 75, 1383, 26]
pixErrRight1 = [516, 965, 1024, 1074, 1119, 1161, 1199, 194, 1270, 137, 1334, 83, 1391, 33]
n1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
pixDia1 = []
Dia1 = []
ErrDiaPix1 = []
ErrDia1 = []
ypoints = []
yerr =[]


for i in range(0, len(pixLeft1)):
    pixDia1.append(pixRight1[i] - pixLeft1[i])
    Dia1.append((pixDia1[i] * numOfPixs1)/1000)
    ErrDiaPix1.append(abs(pixErrLeft1[i] - pixErrRight1[i]))
    ErrDia1.append((ErrDiaPix1[i] * numOfPixs1)/1000)
    print(Dia1[i], "+-", ErrDia1[i])
    ypoints.append(Dia1[i]**2)
    yerr.append(ErrDia1[i]**2)
xpoint = np.array(n1)
ypoint = np.array(ypoints)
yerrs = np.array(yerr)

lin_value_calc(xpoint, ypoint, 2, 1.5E-5, "Order of Interference", "Diameter^2 of the Rings (m^2)", "Diameter^2 versus Order of Interference Without Water", 0, yerrs, False, False,0,0)

numOfPixs2 = 299/102900

pixLeft2 = [557, 497, 444, 403, 368]
pixRight2 = [898, 969, 1023, 1071, 1112]
pixErrLeft2 = [893, 964, 1017, 1063, 1105]
pixErrRight2 = [900, 970, 1024, 1076, 1113]
n2 = [1, 2, 3, 4, 5]
pixDia2 = []
Dia2 = []
ErrDiaPix2 = []
ErrDia2 = []
ypoints2 = []
yerr2 =[]


for i in range(0, len(pixLeft2)):
    pixDia2.append(abs(pixRight2[i] - pixLeft2[i]))
    Dia2.append((pixDia2[i] * numOfPixs2)/1000)
    ErrDiaPix2.append(abs(pixErrLeft2[i] - pixErrRight2[i]))
    ErrDia2.append((ErrDiaPix2[i] * numOfPixs2)/1000)
    print(Dia2[i], "+-", ErrDia2[i])
    ypoints2.append(Dia2[i]**2)
    yerr2.append(ErrDia2[i]**2)
xpoint2 = np.array(n2)
ypoint2 = np.array(ypoints2)
yerrs2 = np.array(yerr2)

lin_value_calc(xpoint2, ypoint2, 1, 3.5E-6, "Order of Interference", "Diameter^2 of the Rings (m^2)", "Diameter^2 versus Order of Interference With Water", 0, yerrs2, False, False,0,0)

l = 6.3056-7
dl = 3.0263487E-8

R = 0.529
dR = 0.0253

s = 9.2703086E-7
ds = 2.52469E-9

derR = (4*l) / (s)
derL = (4*R) / (s)
derS = (4*R*l) / (s**2)

dn = m.sqrt((dR**2 * derR**2) + (dl**2 * derL**2) + (ds**2 * derS**2))
print(dn)





