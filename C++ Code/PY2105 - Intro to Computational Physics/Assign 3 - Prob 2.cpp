#include <iostream>
#include <cmath>
#include <fstream>

//Least Square Fit function
void least_square_fit(double x[], double y[], double sigma[], int size, double return_array[])
{
    //Initisilise variables
    double S, Sx, Sy, Sxx, Sxy;
    //Set all vairables equal to 0
    S = Sx = Sy = Sxx = Sxy = 0;
    //For loop used as arrays are involved
    for(int i = 0; i < size; i++)
    {
        //Calculate the value of all the variables
        S = S + (1/std::pow(sigma[i],2));
        Sx = Sx + (x[i]/std::pow(sigma[i], 2));
        Sy = Sy + (y[i]/std::pow(sigma[i],2));
        Sxx = Sxx + (std::pow(x[i],2)/std::pow(sigma[i],2));
        Sxy = Sxy + ((x[i]*y[i])/std::pow(sigma[i],2));
    }
    //Calculate the value of the denominator
    double denominator = S * Sxx - std::pow(Sx,2);
    //Use the values calculated above along with the denominator to determine a and b
    double a = (Sy * Sxx - Sx * Sxy) / denominator;
    double b = (S * Sxy - Sx * Sy) / denominator;
    
    //Return array used to return more than 1 value
    return_array[0] = a;
    return_array[1] = b;
}
int main()
{
    //Reading data file
    std::ifstream my_data("data1.dat");
    //Declaring necessary variables
    double x[21];
    double y[21];
    double sigma[21];
    double ab[2];
    int nr;
    double leftie, rightie;
    //Adding left and right column from data1.dat into arrays
    nr = 0;
    while(my_data >> leftie >> rightie){
        x[nr] = leftie;
        y[nr] = rightie;
        //Assuming sigma is equal to 1 for all values of y
        sigma[nr] = 1;
        //Increase the counter by 1
        nr++;
    }
    //Use the function to determine a and b of the data
    least_square_fit(x, y, sigma, 21, ab);
    //Set the values of a and b from the return array
    double a = ab[0];
    double b  = ab[1];
    //Print the values
    std::cout << "a: " << a << std::endl << "b: " << b << std::endl;
    
    return 0;
}