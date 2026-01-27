#include <iostream>
#include <cstdlib>  
#include <ctime>  
#include <cmath>  

//Generate a random number between the min and max value
double RandomNumber(double min, double max){
    //Return that
    return min + rand()/(RAND_MAX/(max-min));
}
//Function to be integreated
double f(double x){
    return (300*x) / (1 + std::exp(x));
}
//Using Monte Carlo Technique
double approxIntegral(int numPoints){
    //Initilise the number of points under the curve
    int numPointsUnderCurve = 0;

    for(int i = 0; i <= numPoints; i++){
        //Generate a random x and y value
        double x = RandomNumber(0,10);
        double y = RandomNumber(0, 83.5);

        //Check if that y is under the curve at x
        if(f(x) > y){
            //If so add 1 to the numPointsUnderCurve
            numPointsUnderCurve++;
        }
    }
    //Return the approximate integral value
    return 83.5 * 10 * (static_cast<double>(numPointsUnderCurve)/static_cast<double>(numPoints));
}

int main(){
    //Generate seed for rand()
    srand(time(0));

    //True value determined using wolfram alpha
    double true_val = 246.590293505238028;
    double sumofcounter = 0;
    //Generating 10000 data points to get an accurate average for the number of points needed for an accuracy of 0.01
    for(int i = 0; i < 10000; i++)
    {
        //Initilise variable
        double ate = 1;
        int counter = 1;
        //While the absolute relative error is larger than 0.01 continue
        while(ate > 0.01){
            //Determine the absolute relative error
            ate = abs(true_val - approxIntegral(counter))/true_val;
            counter++;
        }
        //Add the counter value once the desired error is reached 
        sumofcounter += counter;
    }
    //Divide the sumofcounter by the number of data points taken
    double avgN = sumofcounter/10000;
    //Print results along with corresponding stepsize for the trapezium rule
    std::cout << "To get an absolute relative error less than 0.01, the number of samples needed on average is: " << avgN << std::endl;
    std::cout << "To get a similar result with the trapezium rule, a step size of 0.416667 is needed." << std::endl;

    double sumofcounter2 = 0;
    //Generate 100 data points for true error. 100 used instead of 10000 as it takes while to even do 100
    for(int i = 0; i < 100; i++)
    {
        double ate = 1;
        int counter = 1;
        while(ate > 0.01){
            //Determine true error
            ate = abs(true_val - approxIntegral(counter));
            counter++;
        }
        //Once less than desired error add counter to sumofcounter
        sumofcounter2 += counter;
    }
    //Determine the average N
    double avgN2 = sumofcounter2/100;
    //Print the average N along with corresponding stepsize for the trapezium rule. This may take awhile
    std::cout << "To get an absolute true error less than 0.01, the number of samples needed on average is: " << avgN2 << std::endl;
    std::cout << "To get a similar result with the trapezium rule, a step size of 0.028169 is needed." << std::endl;

}