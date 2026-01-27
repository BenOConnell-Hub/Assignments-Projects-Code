import matplotlib.pyplot as plt
import numpy as np
import math as m


#Function used in plotting the function for problem 1 part a
def g(x):
    return x**3 -6*x**2 - x + 10

#Function used in plotting the errors for all of the methods for part c
def f(x):
    return m.log(abs(x/e0))



#Part a
#Generate x values
x = np.linspace(0,5,100)

#Plotting the function g(x) above using the x values generated
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("x^3 - 6x^2 - x + 10")
plt.plot(x,g(x))
plt.show()





#Part c
#Seeting e0 using real value versus the starting value
e0 = m.pi/2-1.31811
#Vectorising f so that an array can be passed through the function f
f2 = np.vectorize(f)

#Data for the errors of the Bisection method
x1 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
y1 = np.array([0.532718, 0.140019, 0.0563307, 0.0418441, 0.00724333, 0.0173004, 0.00502852, 0.00110741, 0.00196056, 0.000426575, 0.000340415, 4.308*(10**(-5)), 0.000148668, 5.27938*(10**(-5)), 4.85689*(10**(-6)), 1.91116*(10**(-5)), 7.12733*(10**(-6)), 1.13522*(10**(-6)), 1.86083*(10**(-6)), 3.62806*(10**(-6))])

#Data for the errors of the Secant method
x2 = np.array([1,2,3,4,5])
y2 = np.array([0.140019, 0.00386278, 8.45158*(10**(-5)), 4.27203*(10**(-8)), 3.47644*(10**(-10))])

#Data for the errors of the Newton-Raphson method
x3 = np.array([1,2,3])
y3 = np.array([0.00270248, 1.17153*(10**(-6)), 2.37612*(10**(-10))])


#Plotting the log of the ratio of the errors for the Bisection method
plt.xlabel("Iterations n")
plt.ylabel("ln(En/E0)")
plt.title("Errors for Bisection Method")
plt.plot(x1, f2(y1))
plt.show()

#Plotting the log of the ratio of the errors for the Secant method
plt.xlabel("Iterations n")
plt.ylabel("ln(En/E0)")
plt.title("Errors for Secant Method")
plt.plot(x2, f2(y2))
plt.show()

#Plotting the log of the ratio of the errors for the Newton-Raphson method
plt.xlabel("Iterations n")
plt.ylabel("ln(En/E0)")
plt.title("Errors for Newton-Raphson Method")
plt.plot(x3, f2(y3))
plt.show()