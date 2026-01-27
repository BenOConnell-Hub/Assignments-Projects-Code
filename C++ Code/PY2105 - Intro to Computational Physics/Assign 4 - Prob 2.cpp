#define _USE_MATH_DEFINES

#include <math.h>
#include <iostream>
#include <cstdlib>  
#include <ctime>    

//Generate a random number between the min and max value
double RandomNumber(double min, double max){
    //Return that
    return min + rand()/(RAND_MAX/(max-min));
}

double approxpi(int numPoints, double a){
    //Initilise variable
    int numPointsinCircle = 0;
    double radius = 0.5*a;

    for(int i = 0; i <= numPoints; i++){
        //Set the x and y coordinates for the point
        double x = RandomNumber(-radius, radius);
        double y = RandomNumber(-radius, radius);

        //Check if those x and y coordinates satisfy the circle equation
        if ((x * x + y * y) <= radius * radius){
            //If so the point is in the circle and increase the number of points in circle counter
            numPointsinCircle += 1;
        }
    }
    //Return the approximation
    return 4 * (static_cast<double>(numPointsinCircle)/static_cast<double>(numPoints));
}

int main(){
    //Generate seed for rand()
    srand(time(0));
    //Initilise the number of points to be used
    int numPoints = 100000;
    //Call the approx pi function
    double pi = approxpi(numPoints, 1);

    //Print the results
    std::cout << "Using the Monte Carlo technique at N = " << numPoints << ". Pi = " << pi << std::endl;

    //Generate data for graph using up to 100000 points
    std::cout << "Generating Data for Python Graph:" << std::endl;
    for(int i = 1000; i <= 100000; i += 1000){
        //Absolute True Error
        std::cout << i << " " << abs(M_PI - approxpi(i, 1)) << std::endl;;
    }
    //Discussion of how more samples leads to higher precision
    std::cout << "Since the Monte Carlo method is based on random numbers the absolute true error for N samples varies, however with higher N you are more likely to get a smaller error." << std::endl;

    
}