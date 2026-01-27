#define _USE_MATH_DEFINES

#include <iostream>
#include <cmath>

//Function in Part but in c++ function form
double f(double x)
{
    return std::cos(x) - (0.25);
}

//Bisection Method Code
double bisection(double x_1, double x_2, double x_n, double (*func)(double))
{
    //Initialise variables used within the function
    double x_m;
    double a_t_e = 1;
    double a_r_e = 1;
    //Iteration counter
    int i = 1;
    //For ease of reading title for each error included
    std::cout << "Absolute True Error   |   Absolute Relative Error" << std::endl;
    //While loop to continue running until tolerance or iteration limit reached
    while (a_t_e > 0.000000001)
    {
        //Getting value of x_m
        x_m = (x_1 + x_2)/2;
        //If it is equal to zero stop the function running and the return x_m
        if (func(x_1)*func(x_m) == 0)
        {
            return x_m;
        }
        //If the product is positive set x_1 to be equal to x_m
        else if (func(x_1)*func(x_m) > 0)
        {
            x_1 = x_m;
        }
        //Otherwise set x_2 to be equal to x_m
        else
        {
            x_2 = x_m;
        }
        //Calculation for the absolute true error, real value entered when calling the function
        a_t_e = abs(x_n - x_m);
        //Calculating the absolute true relative error
        a_r_e = a_t_e/x_m;
        //For the first 20 iterations print the absolute true error and the absolute relative error
        if (i <= 20)
        {
            std::cout << a_t_e << "   |   " << a_r_e << std::endl;
        }
        //Increase the iterative counter
        i++;
        //If the iterative counter is over 100 end the loop
        if (i > 100)
        {
            break;
        }
    }
    //Return x_m as its the approximate value of the loop on the last iteration
    return x_m;
}

//Central differental function with tiny delnum to find very good approximation for the derivative at x taken from assignment 2 problem 2
double cent_diff(double num, double delnum, double (*func)(double)) {
double numerator = func(num + delnum) - func(num - delnum);
double denominator = 2 * delnum;
return numerator / denominator;
}

//Secant method
double Secant(double x_1, double x_0, double x_n, double (*func)(double))
{
    //Initialise variables used in the function
    double x_m;
    double a_t_e = 1;
    double a_r_e = 1;
    //Iterative counter
    int i = 1;
    //Used for ease of readig in the cluttered output
    std::cout << "Absolute True Error   |   Absolute Relative Error" << std::endl;
    while (a_t_e > 0.00000001)
    {
        //Calculating the numerator
        double numerator = (func(x_1)*(x_1 - x_0));
        //Calculating the denominator
        double denominator = (func(x_1) - func(x_0));
        //Calculating current best guess of root
        x_m = x_1 - (numerator/denominator);
        //Calculating the absolute true error
        a_t_e = abs(x_n - x_m);
        //Calculating the asbolute true relative error
        a_r_e = a_t_e/x_m;
        //Setting values for the next iteration
        x_0 = x_1;
        x_1 = x_m;
        //Printing the absolute true error and absolute true relative error for the first 20 iterations
        if (i <= 20)
        {
            std::cout << a_t_e << "   |   " << a_r_e << std::endl;
        }
        //Increasing iterative counter
        i++;
        //Stopping the loop if over 100 iterations reached
        if (i > 100)
        {
            break;
        }
    }
    //Returnig the current best guess of the root when loop finishes running
    return x_m;
}

//Newton-Raphson method
double Newton_Raphson(double x_0, double x_n, double (*func)(double))
{
    //Initialising the vairables used in the function
    double x_m;
    double a_t_e = 1;
    double a_r_e = 1;
    //Iterative counter
    int i = 1;
    //Used for ease of reading in cluttered output
    std::cout << "Absolute True Error   |   Absolute Relative Error" << std::endl;
    //While loop running until iterative limit is reached or tolerance is reached
    while (a_t_e > 0.000000001)
    {
        //Determining the current approximation of the root
        x_m = x_0 - (func(x_0)/cent_diff(x_0, 0.000000000001, func));
        //Determining the absolute true error
        a_t_e = abs(x_n - x_m);
        //Determining the absolute true relative error
        a_r_e = a_t_e/x_m;
        //Setting the variable for the nect iteration
        x_0 = x_m;
        //Printing the errors for the first 20 iterations
        if (i <= 20)
        {
            std::cout << a_t_e << "   |   " << a_r_e << std::endl;
        }
        //Increasing the iteration counter
        i++;
        //If over 100 iterations are reached the loop ends
        if (i > 100)
        {
            break;
        }
    }
    //Returning the current approximation of the root when the loop ends
    return x_m;
}


int main()
{   
    //Dashes are used throughout the function along with titles for ease of reading the cluttered output and cluttered code
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "Part a" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    //Printing the answers to the Part a
    std::cout << "Good starting values for the Bisection and Secant method would be x_a = 1 and x_b = 2 as they correspond to positive and negative values respectively and are relatively close to the root." << std::endl;
    std::cout << "For the Newton-Raphson method either 0 or 1 would be good values for the function to converge very quickly as they are both very close to the root. A bad value for the Newton-Raphson method would be x_a = 4.08167 as it is a point in which the derivative is equal to 0 and you would be dividing by 0." << std::endl;
    std::cout << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    std::cout << "Part b" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    //Printing the approximate root calculated by the bisection method
    std::cout << "The Bisection Method:" << std::endl;
    std::cout << "The approximate root using the Bisection method is: " << bisection(0, M_PI_2, 1.318116072, f) << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    //Printing the approximate root calculated by the Secant method
    std::cout << "The Secant Method:" << std::endl;
    std::cout << "The approximate root using the Secant Method is: " << Secant(M_PI_2, 0, 1.318116072, f) << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    //Printing the approximate root calculated by the Newton-Raphson method
    std::cout << "The Newton-Raphson Method:" << std::endl;
    std::cout << "The approxmate root using the Newton-Raphson method is: " << Newton_Raphson(M_PI_2, 1.318116072, f) << std::endl;
    std::cout << std::endl << "------------------------------------------" << std::endl;
    std::cout << "Part c" << std::endl;
    std::cout << "------------------------------------------" << std::endl;
    //Printing the answers for part c of Problem 1
    std::cout << "The Bisection method converges linearly like expected from the lectures" << std::endl;
    std::cout << "The Secant method converges super linearly like expected as it converges four times as fast as the bisection method" << std::endl;
    std::cout << "The Newton-Raphson method converges the fastest out of all the methods, although it converges too fast to tell if it converges quadratically as there is only 3 errors before the tolerance is reached" << std::endl;

}