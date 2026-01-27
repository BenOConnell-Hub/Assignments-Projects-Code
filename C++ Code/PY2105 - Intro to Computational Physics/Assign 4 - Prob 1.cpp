
#include <iostream>
#include <cstdlib>
#include <iomanip>

//Initilise A
double matrix[4][4] = {
    {13,4,7,9},
    {10,6,5,12},
    {1,8,2,16},
    {3,14,15,11}
};

//Initilise b
double vector[4] = {111,118,114,163};

//Initilise used matrices and constants
const int rows = sizeof(matrix) / sizeof(matrix[0]);
const int columns = sizeof(matrix[0]) / sizeof(double);
bool PivotingUsed = false;
double AugMat[rows][columns + 1];
double U[rows][columns];
double L[rows][columns];

//Partial pivoting function used within GaussianElimination
void PartialPivoting(int currentrow){
    //Set the max row to the currentrow
    int maxrow = currentrow;
    //Check if the absolute value of the element in the same column the row below is larger than the current largest value
    for(int i = currentrow; i< rows; i++){
        if((std::abs(AugMat[i][currentrow])) > std::abs(AugMat[maxrow][currentrow])){
            //If so set that row to the new max row
            maxrow = i;
        }
    }
    //If the max row is not equal to the current row then swap them
    if (maxrow != currentrow){
        PivotingUsed = true;
        for(int i = currentrow; i <= columns; i++){
            //Temp used to temporarily hold the current element in the current position of the matrix
            double temp = AugMat[currentrow][i];
            //Swap the elements 
            AugMat[currentrow][i] = AugMat[maxrow][i];
            AugMat[maxrow][i] = temp;
        }
    }
}

//Function used specifically for augmented matrices
void PrintAugMat(){
    //Print the line below for ease of reading the output
    std::cout << "A | b" << std::endl;
    //Print the rows and columns adding a | before the last element in each row
    for(int i = 0; i < rows; i++){
        for(int j = 0; j <= columns; j++){
            if(j == columns){
                std::cout << "|" << " ";
            }
            //setw(11) used for formatting
            std::cout << std::setw(11) << AugMat[i][j] << " ";
        }
        std::cout << std::endl;
    }
}
//Main function used in problem 1 part a
void GaussianElimination(double A[][columns], double b[]){
    //Creating the augmented matrix
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            //Adding the values from the matrix a
            AugMat[i][j] = A[i][j];
        }
        //Adding the vector b as the last column
        AugMat[i][columns] = b[i];
    }
    //Forward elimination
    for(int i = 0; i < rows; i++){
        //Call the partial pivoting function
        PartialPivoting(i);

        //Performing the forward elimination
        for(int j = i + 1; j < rows; j++){
            //Determining the dividing factor
            double m = AugMat[j][i] / AugMat[i][i];
            for(int k = i; k <= columns; k++){
                //Using the dividing factor to change each element of the row
                AugMat[j][k] -= m * AugMat[i][k];
            }
        }
    }
    //Print the augmented matrix using the function
    std::cout << "After forward Gaussian elimination the A matrix and b vector are:" << std::endl;
    PrintAugMat();

    //Determining the determinant of A
    double detOfA = 1;
    for(int i = 0; i < rows; i++){
        detOfA *= AugMat[i][i];
    }
    //Check if pivoting was used
    if (PivotingUsed == true){
        //If so multiply the determinant by -1
        detOfA *= -1;
    }

    //Initilising the solution vector
    double solution[columns];
    for(int i = rows -1; i >= 0; i--){
        //Setting the solution vector to the modified b vector
        solution[i] = AugMat[i][columns];
        for(int j = i + 1; j < columns; j++){
            //Using the previous solutions to modify the value of the solution vector at i appropriately
            solution[i] -= AugMat[i][j] * solution[j];
        }
        //Dividing the solution for each variable by the coefficient of that variable
        solution[i] /= AugMat[i][i];
    }
    //Printing the solution for the Gaussian elimination 
    std::cout<< "The solution using Gaussian elimination is: " << std::endl;
    for(int i = 0; i < rows; i++){
        //Used for formatting
        std::cout << "x" << i << " = " << solution[i] << std::endl;
    }

    //Print the determinant of A
    std::cout << "The determinant of the matrix A is: " << detOfA << std::endl;
}

//Print a generic square matrix
void PrintMat(double mat[][columns]){
    //Print each row and column
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < columns; j++){
            //setw is used for formatting
            std::cout << std::setw(11) << mat[i][j] << " ";
        }
        std::cout << std::endl;
    }
}

//Determining the L and U matrix of A
void LUDecomposition(double A[][columns]){
    for(int i = 0; i < rows; i++){
        //Setting the row and column for L at i to be 1
        L[i][i] = 1;
        for(int j = 0; j < columns; j++){
            //Setting U equal to A
            U[i][j] = A[i][j];
            //Setting the upper triangle of L to be 0
            if (j > i){
                L[i][j] = 0;
            }
        }
    }

    //Performing forward elimination of U
    for(int i = 0; i < rows; i++){
        for(int j = i + 1; j < columns; j++){
            //Dividing factor
            double m = U[j][i] / U[i][i];
            //Adding the dividing factor to the lower triangle of L
            L[j][i] = m;
            for(int k = i; k < columns; k++){
                //Using the dividing factor to change the values of U and perform the forward elimination
                U[j][k] -= m * U[i][k];
            }
        }
    }
    //Printing the L and U matrix
    std::cout << "The L matrix is: " << std::endl;
    PrintMat(L);
    std::cout << std::endl;
    std::cout << "The U matrix is: " << std::endl;
    PrintMat(U);
    std::cout<< std::endl;
    
}

//Main function for Problem 1 Part b
void SolveLUandInverseofA(double A[][columns], double b[]){
    //Using previous function to determine L and U
    LUDecomposition(A);
    //Setting the Z vector
    double Z[rows];
    //Forward substitution
    for (int i = 0; i < rows; i++){
        //Putting it equal to the b vector
        Z[i] = b[i];
        for(int j = 0; j < i; j++){
            //Using the previous values and the elements of the L matrix to find the solution to the Z vector
            Z[i] -= L[i][j]*Z[j];
        }
    }
    //Setting the solution vector
    double solution[rows];
    for(int i = rows - 1; i >= 0; i--){
        //Setting the solution vector to the Z vector
        solution[i] = Z[i];
        //Using the previous value of the solution vector and the U matrix to determine the solution
        for(int j = i + 1; j < columns; j++){
            solution[i] -= U[i][j] * solution[j];
        }
        solution[i] /= U[i][i];
    }
    //Printing the solution to for LU composition of a matrix A
    std::cout << "The solution using LU composition is: " << std::endl;
    for(int i = 0; i < columns; i++){
        //Used for formatting
        std::cout << "x" << i << " = " << solution[i] << std::endl;
    }
    
    //Initilise the Inverse and B matrix
    double Inverse[rows][columns];
    double B[rows][columns];
    for(int i = 0; i < rows; i++){
        //Setting the diagonal to 1
        B[i][i] = 1;
        //Setting the rest to 0
        for(int j = 0; j < rows; j++){
            if (j != i){
                B[i][j] = 0;
            }
        }
    }
    //This uses the same procedure as the LU solution above but for each column of B
    for(int k = 0; k < columns; k++){
        //Initilise generic N vector
        double N[rows];
        for (int i = 0; i < rows; i++){
            //Set the N vector to the kth column of B
            N[i] = B[i][k];
            for(int j = 0; j < i; j++){
                //Solving the N vector with forward elimination using the same method as solving the Z vector
                N[i] -= L[i][j]*N[j];
            }
        }
        //Initilise the solution to the column
        double soltocol[rows];
        for(int i = rows - 1; i >= 0; i--){
            //Set it equal to the N vector
            soltocol[i] = N[i];
            //Determining the solution to that column
            for(int j = i + 1; j < columns; j++){
                soltocol[i] -= U[i][j] * soltocol[j];
            }
            soltocol[i] /= U[i][i];
        }
        //Adding the solution to the column to the kth column of the Inverse matrix
        for(int i = 0; i < rows; i++){
            Inverse[i][k] = soltocol[i];
        }
    }
    //Printing the Inverse matrix
    std::cout << "The inverse of the matrix A is: " << std::endl;
    PrintMat(Inverse);
}

int main()
{
    //Calling the GaussianElimination function for part a
    std::cout << "-------------------------" << std::endl << "Part a" << std::endl << "-------------------------" << std::endl;
    GaussianElimination(matrix, vector);

    //Calling the SolveLUandInverseofA function
    std::cout << "-------------------------" << std::endl << "Part b" << std::endl << "-------------------------" << std::endl;
    SolveLUandInverseofA(matrix, vector);
    return 0;
}