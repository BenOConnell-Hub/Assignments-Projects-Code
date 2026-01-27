using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Assignment_1__AM2060
{
    public class GaussEliminate
    {
        //Initialize variables
        private int size;
        private double[,] augmentedMatrix;
        //SetAb method
        public void SetAb(double[,] A, double[] b)
        {
            //Make sure matrix is solvable
            if (A.GetLength(0) != b.GetLength(0))
            {
                Console.WriteLine("ERROR");
                Console.WriteLine("The matrix and vector entered do not contain the same number of rows");
            }
            else
            {
                //Find the size of the matrix
                size = A.GetLength(0);
                //Create augmented matrix of same size with an additional column
                augmentedMatrix = new double[size, size + 1];

                for (int i = 0; i < size; i++)
                {
                    for (int j = 0; j < size; j++)
                    {
                        //Set each row of A equal to the corresponding row of augmentedMatrix, without including final column
                        augmentedMatrix[i, j] = A[i, j];
                    }
                    //Set the final column equal to the vector b
                    augmentedMatrix[i, size] = b[i];
                }
            }
        }
        public double[] Solve()
        {
            //Initilise n
            int n;
            //Get user input
            Console.WriteLine("Do you want to solve this problem with no pivot (0), partial pivot(1) or scaled partial pivot (2). Enter the relevant number:");
            var input = Console.ReadLine();
            //Check if input is an integer
            if (int.TryParse(input, out int value))
            {
                //If it is set n equal to that value
                n = Convert.ToInt32(input);
            }
            else
            {
                //Return an error and default to n = 1
                Console.WriteLine("Invalid input entered, defaulting to n = 1, partial pivot.");
                n = 1;
            }
            //Check if inputted n is within valid range
            if (n > 2 || n < 0)
            {
                //If it isnt return an error and default n = 1
                Console.WriteLine("n is not in the valid range of inputs, defaulting to n = 1");
                n = 1;
            }
            //Initilize solution vector
            double[] solution = new double[size];
            for (int i = 0;i < size; i++)
            {
                //User decides by entering an n as the parameter if they want to solve the SLE with no pivot, partial pivot or scaled partial pivot. 0 = No pivot, 1 = Partial pivot, 2 = Scaled Partial pivot
                NoPivotorPartialorScaled(i, n);
                //If no pivot is selected and there is a 0 in the pivot position apply partial pivoting to move 0
                if (n == 0 && augmentedMatrix[i,i] ==0)
                {
                    PartialPivot(i);
                }

                for (int j = i + 1 ; j < size; j++)
                {
                    //Determine the dividng factor to ensure the row below is 0
                    double m = augmentedMatrix[j, i] / augmentedMatrix[i,i];
                    for (int k = i; k <= size; k++)
                    {
                        //Multiply the corresponding value in the row above by the dividing factor and subtract it from the rows below
                        augmentedMatrix[j,k] -= m * augmentedMatrix[i, k];
                    }
                }
            }
            //Performing back substitution
            for (int i = size - 1; i >= 0; i--)
            {
                //Initilize solution vector equal to the final column
                solution[i] = augmentedMatrix[i,size];
                for(int j = i + 1; j < size; j++)
                {
                    //Multiply current row by the solution to the bottom row to get reduced row echelon form
                    solution[i] -= augmentedMatrix[i,j] * solution[j]; 
                }
                //Divide the solution by the value of the pivot column to ensure correct solution
                solution[i] /= augmentedMatrix[i,i];
            }
            for (int i = 0; i < solution.Length; i++)
            {
                Console.WriteLine($"x[{i}] = {solution[i]}");
            }
            return solution;

        }
        public void DisplayAugMatrix()
        {
            //Display the meaning of the following print
            Console.WriteLine("Augmented Matrix [A|b]:");
            //Print each row and column
            for (int i = 0; i < size; i++)
            {
                for (int j = 0; j <= size; j++)
                {
                    // If j reaches the size of the augmented matrix add a | for aesthetics
                    if (j == size)
                    {
                        Console.Write("|" + " ");
                    }
                    Console.Write(augmentedMatrix[i, j] + "\t");
                }
                //Go onto the next line
                Console.WriteLine();
            }
        }
        private void PartialPivot(int currentrow)
        {
            //Set current maxrow to the current row
            int maxrow = currentrow;
            for (int i = currentrow;i < size;i++)
            {
                //Check if the element 1 row lower is larger
                if (Math.Abs(augmentedMatrix[i,currentrow]) > Math.Abs(augmentedMatrix[maxrow,currentrow]))
                {
                    //If so set that row to the new largest row
                    maxrow = i;
                }
            }

            if (maxrow != currentrow)
            {
                for (int i = currentrow; i <= size;i++)
                {
                    //Temp to temporarily hold the value of the element being swapped
                    double temp = augmentedMatrix[currentrow, i];
                    //Swapping elements
                    augmentedMatrix[currentrow, i] = augmentedMatrix[maxrow, i];
                    augmentedMatrix[maxrow, i] = temp;
                }
            }
        }
        private void ScaledPivot(int currentrow)
        {
            //Making sure we arent on the last row
            if (size - currentrow > 0)
            {
                //Making a list of the largest elements equal in size to the remaining rows
                double[] LargestElement = new double[size - currentrow];
                //Setting the max row equal to the current max row
                int maxrow = currentrow;
                for (int i = currentrow; i < size;i++)
                {
                    //Setting the initial value of the largest element for that row
                    LargestElement[i - currentrow] = augmentedMatrix[i, currentrow];
                    for (int j = i; j < size; j++)
                    {
                        if (Math.Abs(augmentedMatrix[i,j]) > Math.Abs(LargestElement[i-currentrow]))
                        {
                            //If the element in the column next to it is larger than it set that to the current largest element of that row
                            LargestElement[i - currentrow] = augmentedMatrix[i, j];
                        }
                    }
                }
                for (int i = currentrow; i < size; i++)
                {
                    //Figuring out which is the largest value in the pivot column relative to the largest element in its respective row
                    if (Math.Abs(augmentedMatrix[i, currentrow] / LargestElement[i-currentrow]) > Math.Abs(augmentedMatrix[maxrow, currentrow] / LargestElement[maxrow - currentrow]))
                    {
                        maxrow = i;
                    }
                }

                if (maxrow != currentrow)
                {
                    for (int i = currentrow; i <= size; i++)
                    {
                        //Temp tp temporarily store the element being swapped
                        double temp = augmentedMatrix[currentrow, i];
                        //Swapping the elements
                        augmentedMatrix[currentrow, i] = augmentedMatrix[maxrow, i];
                        augmentedMatrix[maxrow, i] = temp;
                    }
                }

            }
        }
        //Simple method that allows the user to decide which pivot method is being used
        private void NoPivotorPartialorScaled(int currentrow, int n)
        {
            if (n == 2)
            {
                ScaledPivot(currentrow);
            }
            else if (n == 1)
            {
                PartialPivot(currentrow);
            }
        }
    }
}
