//Ben O'Connell, 123463236, Assignment 1, PY2105

#include <iostream>
#include <cmath>
#include <stack>
#include <cmath>
#include <fstream>
#include <stdlib.h>
#include <string>
#include <stdio.h>
#include <math.h>
#include <assert.h>
#include <algorithm>

double user_Input1, user_Input2, user_Input3, dec_Num;
int whole_Num;

//Problem 2 Stack Declaration
std::stack<int> list_of_numbers;
std::stack<int> list_of_dec;
std::stack<int> list_of_binary;
//Problem 3 Stack Declaration
std::stack<int> list_of_binaryDec;
std::stack<int> temp_list_binaryDec;

std::ifstream my_data("dice.dat");


int main()
{
    // Problem 1
    std::cout << "------------------------------------" << "\n";
    std::cout << "Problem 1" <<"\n" << "\n";
    
    std::cout<<"Please enter your first number: ";
    std::cin>> user_Input1;
    std::cout<<"Please enter your second number: ";
    std::cin>> user_Input2;
    std::cout<<"Please enter your third number: ";
    std::cin>> user_Input3;
    
    std::cout << "The sum of the three numbers entered is: " << user_Input3 + user_Input2 + user_Input1 << "\n";
    std::cout << "The product of the three numbers entered is: " << user_Input1*user_Input2*user_Input3 << "\n";
    
    //Problem 2
    std::cout << "------------------------------------" << "\n";
    std::cout << "Problem 2" <<"\n" << "\n";
    
    
    std::cout << "Please enter a decimal number: ";
    std::cin>> dec_Num;
    
    whole_Num = floor(dec_Num);
    double dec = dec_Num - whole_Num;
    do{
        list_of_numbers.push(whole_Num%2);
        whole_Num = whole_Num/2;
    }
    while (whole_Num != 0);
    do{
        dec = dec*2;
        if(dec > 1){
            list_of_dec.push(1);
            dec = dec-1;
        }
        else if(dec == 1){
            list_of_dec.push(1);
            dec = 0;
        }
        else{
            list_of_dec.push(0);
        }
    }
    while (dec != 0);
    
    for(int x = list_of_numbers.size(); x >0; x = x -1){ 
        std::cout << list_of_numbers.top();
        list_of_numbers.pop();
    }
    int y;
    std::stack<int> tempStack;
    std::cout << ".";
    for(int y = list_of_dec.size(); y>0; y = y - 1){
        tempStack.push(list_of_dec.top());
        list_of_dec.pop();
    }
    int z;
    for(int z = tempStack.size(); z>0; z = z - 1){
        std::cout << tempStack.top();
        tempStack.pop();
    }
    std::cout << "\n";
    //Problem 3
    std::cout << "------------------------------------" << "\n";
    std::cout << "Problem 3" <<"\n" << "\n";
    
    char arr[10];
    std::cout << "Please enter your binary number: ";
    std::cin.ignore();
    std::cin.getline(arr,10);
    
    for (int f = 0; f < sizeof(arr); f++){
        if(arr[f] == '1'){
            list_of_binary.push(1);
            std::cout << arr[f] <<"\n";
            arr[f] = ' ';
        }
        else if (arr[f] == '0') {
            list_of_binary.push(0);
            std::cout << arr[f] <<"\n";
            arr[f] = ' ';
        }
        else if (arr[f] == '.'){
            break;
        }
        else{
            continue;
        }
    }
    for (int f = 0; f < sizeof(arr); f++){
        if(arr[f] == '1'){
            temp_list_binaryDec.push(1);
        }
        else if (arr[f] == '0') {
            temp_list_binaryDec.push(0);
        }
        else{
            continue;
        }
    }
    int sum = 0;
    int counter = 0;
    while(!list_of_binary.empty()){
        if(list_of_binary.top() == 1){
            sum = sum + pow(2,counter);
        }
        list_of_binary.pop();
        counter++;
    }
    int counterBin = -1;
    double sumDec = 0;
    while(!temp_list_binaryDec.empty()){
        list_of_binaryDec.push(temp_list_binaryDec.top());
        temp_list_binaryDec.pop();
    }
    while (!list_of_binaryDec.empty()){
        if(list_of_binaryDec.top() == 1){
            sumDec = sumDec + pow(2,counterBin);
        }
        list_of_binaryDec.pop();
        counterBin--;
    }
    std::cout << "The decimal conversion of the provided binary number is: " << sum + sumDec <<"\n";
    
    //Problem 4
    std::cout << "------------------------------------" << "\n";
    std::cout << "Problem 4" <<"\n" << "\n";
    
    
    int delays[10] = {4,10,6,5,12,5,8,7,2,55};
    int sum_of_delays = 0;
    for(int number:delays){
        sum_of_delays += number;


    }
    float size_delay = sizeof(delays)/sizeof(int);
    float mean_delay = sum_of_delays/size_delay;
    std::cout << "The mean delay is: " << mean_delay << "\n";
    float sum_for_SD = 0;
    for(int number:delays){
        sum_for_SD += pow(number - mean_delay,2);
    }
    float stand_dev = pow(sum_for_SD/(size_delay-1), 0.5);
    std::cout << "The standard deviation is: " << stand_dev << "\n";
    float mean_no_outlier = (sum_of_delays - 55)/(size_delay-1);
    std::cout << "The mean with no outlier is: " << mean_no_outlier << "\n";
    std::cout << "This is a difference of: " << mean_delay-mean_no_outlier << "\n";
    //Problem 5
    std::cout << "------------------------------------" << "\n";
    std::cout << "Problem 5" <<"\n" << "\n";
    
    int dice_result[40];
    int nr, ny, a, b, size_of_dr;
    double sum_dr = 0;
    double mean_dice_result, median_dr;
    std::string tempS;

    nr = 0;
    while(my_data >> a >> b){
        dice_result[nr] = b;
        nr++;
    }
    size_of_dr = sizeof(dice_result)/sizeof(int);
    nr = 0;
    std::sort(dice_result, dice_result + size_of_dr);
    while(nr < size_of_dr){
        sum_dr += dice_result[nr];
        nr++;
    }
    mean_dice_result = sum_dr/size_of_dr;
    std::cout << "The mean dice result is: " << mean_dice_result << "\n";
    if(floor(size_of_dr/2) == ceil(size_of_dr/2)){
        median_dr = dice_result[size_of_dr/2];
    }
    else{
        int temp1, temp2, temp3;
        temp1 = floor(size_of_dr/2);
        temp2 = dice_result[temp1];
        temp3 = dice_result[temp1+1];
        median_dr = (temp2 + temp3)/2;
    }
    std::cout << "The median dice result is: " << median_dr << "\n";
    double sum_dr_sd = 0;
    for(int entry:dice_result){
        sum_dr_sd += pow(entry - mean_dice_result,2);
    }
    float st_dev_dr = pow(sum_dr_sd/(size_of_dr-1),0.5);
    std::cout << "The standard deviation of the dice results is: " << st_dev_dr << "\n";
    std::cout << "The difference between the median and the mean is : " << median_dr - mean_dice_result << "\n";

    std::cout << "------------------------------------" << "\n";
    return 0;
}   
