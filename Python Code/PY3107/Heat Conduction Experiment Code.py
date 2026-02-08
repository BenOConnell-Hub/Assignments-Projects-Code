import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from scipy.optimize import curve_fit
import math as m
import Lin_Value as LV


d =[209, 189, 169, 149, 129, 109, 89, 69]
d_err = 2
T1 = [90.0, 100.4, 102.2, 99.2, 94.6, 93.6, 83.8, 72.4]
T_err = 0.1


T2 = [38.2, 41.2, 45.4, 49.3, 49.7, 50.5, 48.2, 45.8]


T3 = [32.9, 34.2, 34.7, 35.3 ,35.2, 34.3, 34.7, 34.7]

plt.plot(d, T1, label = 'R = 38 ± 1 (mm)')
plt.errorbar(d, T1, xerr = d_err, yerr = T_err, fmt = 'o')
plt.plot(d, T2, label = 'R = 63 ± 1 (mm)')
plt.errorbar(d, T2, xerr = d_err, yerr = T_err, fmt = 'o')
plt.plot(d, T3, label = 'R = 99 ± 1 (mm)')
plt.errorbar(d, T3, xerr = d_err, yerr = T_err, fmt = 'o')

plt.title('Temperature versus Depth for three different radii')
plt.xlabel('Depth (mm)')
plt.ylabel('Temperature (C)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.legend()
plt.show()

r1 = [19, 30, 40, 50, 59, 72, 82, 92]
err_r = 3

T_1 = [106.5, 82.4, 88.7, 55.4, 69.5, 45.2, 48.1, 45.1]

plt.scatter(r1, T_1)

plt.errorbar(r1, T_1, xerr = err_r, yerr = T_err, fmt = 'o')

plt.title('Temperature versus radius')
plt.xlabel('Radius (mm)')
plt.ylabel('Temperature (C)')
plt.grid(visible=True, which="major", linestyle="-", linewidth=0.8)
plt.minorticks_on()
plt.show()

err_logr1 = [np.float64(0.15789473684210525), np.float64(0.1), np.float64(0.06), np.float64(0.041666666666666664), np.float64(0.03658536585365854), np.float64(0.03260869565217391), np.float64(0.07500000000000001), np.float64(0.05084745762711865)]
logr1 = [2.9444389791664403, 3.4011973816621555, 3.912023005428146, 4.276666119016055, 4.406719247264253, 4.5217885770490405, 3.6888794541139363, 4.07753744390572]

LV.lin_value_calc(logr1, T_1, x_line = 3, y_line = 100, XR_line = 3, YR_line = 90, x_label = 'Log of the Radius (mm)', y_label = 'Temperature (C)', g_title = 'Temperature versus the log of the Radius', errors_x = err_logr1, x_at_zero = False, y_at_zero = False, errors_y = T_err)


logr2 = [2.9444389791664403, 3.4011973816621555, 3.912023005428146, 4.276666119016055, 4.406719247264253, 4.5217885770490405]
err_logr2 = [np.float64(0.15789473684210525), np.float64(0.1), np.float64(0.06), np.float64(0.041666666666666664), np.float64(0.03658536585365854), np.float64(0.03260869565217391)]

T_2 = [106.5, 82.4, 55.4, 45.2, 48.1, 45.1]

LV.lin_value_calc(logr2, T_2, x_line = 3, y_line = 100, XR_line = 3, YR_line = 90, x_label = 'Log of the Radius (mm)', y_label = 'Temperature (C)', g_title = 'Temperature versus the log of the Radius', errors_x = err_logr2, x_at_zero = False, y_at_zero = False, errors_y = T_err)






