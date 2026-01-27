namespace Assignment_1__AM2060
{
    internal class Program
    {
        static void Main(string[] args)
        {
            GaussEliminate g = new GaussEliminate();
            double[,] A1 = new double[4, 4] { { 10, 1, 1, 1 }, { 1, 1, 2, 3 }, { -1, 1, 2, 1 }, { 3, 2, -1, 0 } };
            double[] b1 = new double[4] { 1, 2, -10, 1 };
            g.SetAb(A1, b1);
            g.Solve();
            double[,] A2 = new double[3, 3] { { 5, 1, 2 }, { -3, 9, 4 }, { 1, 2, -7 } };
            double[] b2 = new double[3] { 10, -14, -33 };
            g.SetAb(A2, b2);
            g.Solve();
        }
    }
}
