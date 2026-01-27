#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <random>
#include <memory>

//Function for Problem 1 Part b
int factorial(int num) {
    int product = 1;
    for (int i = num; i > 0; i--) {
        product *= i;
    }
    return product;
}

//Functions for Problem 2
//Central differental function for a general function
double cent_diff(double num, double delnum, double (*func)(double)) {
    double numerator = func(num + delnum) - func(num - delnum);
    double denominator = 2 * delnum;
    return numerator / denominator;
}

//Main Function for problem 2
double f(double num) {
    return std::pow(num, 2) - num;
}
//Funtions for Problem 3
//Main Function for problem 3
double g(double num)
{
    double numerator = 300 * num;
    double denominator = 1 + exp(num);
    return numerator/denominator;
}
//Function for multi-segmented trapezoidal rule for a general function
double trapezodial(double a, double b, int n, double(*func)(double))
{
    //Calculating h
    double h = (b-a)/n;
    //Calculating the sum aspect of the formula
    double sum_of_steps = 0;
    for (int i = 1; i < n; i++)
    {
        sum_of_steps += func(a+(i * h));
    }
    //Calculating the entire formula
    double lhs = ((b-a)/(2 * n));
    double rhs = ((func(a) + (2 * sum_of_steps) + func(b)));
    return lhs * rhs;
}

int main()
{
    
    //Problem 1
    //Part a


    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "Problem 1" << std::endl << "-----------------------------------------------" << std::endl << "Part a" << std::endl;
    std::cout << "-----------------------------------------------" << std::endl;
    double e_t = 0;
    double x = 0.000001;

    //Determining when small angle approximation breaks down
    while(e_t <= 0.01){
        e_t = std::abs((sin(x)-x)/sin(x));
        x += 0.000001;
    }

    //Displaying results of part a
    std::cout << "The small angle approximation breaks down at " << x << " rads" << std::endl;

    //Part b
    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "Part b" << std::endl;
    std::cout << "-----------------------------------------------" << std::endl;


    //Calculating the approx value with 2nd term
    double approx_value = x - (std::pow(x,3))/factorial(3);

    //Calculating absolute relative error
    e_t = std::abs((sin(x)-approx_value)/sin(x));

    //Displaying results
    std::cout << "Using the 2nd term of the approximation the absolute relative error is: " << e_t*100 << "%" << std::endl;

    //Part c
    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "Part c" << std::endl;
    std::cout << "-----------------------------------------------" << std::endl;

    //Determining when approximation breaks down for the 2nd term
    e_t = 0;
    approx_value = 0;
    x = 0.000001;
    while(e_t <= 0.01){
        approx_value = x - (std::pow(x,3))/factorial(3);
        e_t = std::abs((sin(x)-approx_value)/sin(x));
        x += 0.000001;
    }

    //Displaying results
    std::cout << "The new approximation breaks down at: " << x << " rads" << std::endl;
    

    //Problem 2
    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "Problem 2" << std::endl << "-----------------------------------------------" << std::endl;

    //Diff at x = 2 with delta x = 0.25
    double diff_2 = cent_diff(2.0, 0.25, f);
    std::cout << "The approximation for the differential value of the function at 2 with step size 0.25 is: " << diff_2 << std::endl;
    //Absolute true error
    std::cout << "The absolute true error with a step size of 0.25 is: " << 3 - diff_2 << std::endl;
    std::cout << "The absolute true error with a step size of 0.125 is: " << 3 - cent_diff(2.0, 0.25, f) << std::endl;
    std::cout << "It is impossible to say if the scaling of this example is reflective of the scaling seen in the lectures as there is no absolute true error." << std::endl;

    //Problem 3
    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "Problem 3" << std::endl << "-----------------------------------------------" << std::endl;
    std::cout << "Part c" << std::endl;
    std::cout << "-----------------------------------------------" << std::endl;

    //Getting user to input a value for a in the trapezium function
    double user_a;
    std::cout << "Please enter a value for a" << std::endl;
    std::cin >> user_a; 
    //Getting user to input a value for b in the trapezium function
    double user_b;
    std::cout << "Please enter a value for b (This value must be larger than the a entered previously)" << std::endl;
    std::cin >> user_b; 
    //Getting user to input a value for n in the trapezium function
    int user_n;
    std::cout << "Please enter a value for n (this value must be an integer larger than 0)" << std::endl;
    std::cin >> user_n; 
    //Printing value of the integral of the function g(x) at user_a and user_b
    std::cout<< "The value of the integral of the funtion at the entered values is: " << trapezodial(user_a,user_b,user_n,g) << std::endl;

    std::cout << "-----------------------------------------------" << std::endl;
    std::cout << "Part d" << std::endl;
    std::cout << "-----------------------------------------------" << std::endl;

    //True value for the integral between 0 and 10 of the function g(x) above from wolfram alpha
    double true_val = 246.590293505238028;
    //True error for n = 2
    std::cout << "The true error for n = 2 is: " << true_val-trapezodial(0.0,10,2,g) << std::endl << std::endl;
    //Answer as to why the error is so large in n = 2
    std::cout << "As seen in Error in n = 2.pdf the area not included with n = 2 is vast and therefore the error is big." << std::endl << std::endl;;
    //Calculating the true error for n = 4,8,16 and 32
    int counter = 2;
    for (int i = 1; i <= 4; i++)
    {
        //Counter used so I dont have to manually write the code for n = 4,8,16 and 32
        counter = counter *2;
        std::cout << "The true error for n = " << counter << " is: " << true_val-trapezodial(0,10,counter,g) << std::endl;
    }
    double ate = 1;
    int c = 1;
    while (ate > 0.01){
        ate = abs(true_val - trapezodial(0,10,c,g));
        c++;
    }
    std::cout << "Step size needed for an error of 0.01 is: " << c << std::endl;

    

    return 0;
}