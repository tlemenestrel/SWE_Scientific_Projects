#include <fstream>
#include <iostream>
#include <string>
#include <vector>

#include "COO2CSR.hpp"
#include "matvecops.hpp"
#include "CGSolver.hpp"

int main(int argc, char** argv)
{
	// Check if the command line arguments are provided
	if (argc < 3)
	{
		std::cerr << "Not enough command-line arguments provided." << std::endl
		<< " ./mazesolver <input file> <output file>" << std::endl;
		return 1;
	}

	// Store COO matrix as three vectors for i and j index and values
	std::vector<int> i_idx;
	std::vector<int> j_idx;
	std::vector<double> val;

	// Read the command-line arguments
	std::string inputFileName = argv[1];
	std::string outputFileName = argv[2];

	// Reading the input file
	std::ifstream inputFile (inputFileName.c_str());

	if (inputFile.is_open()) 
	{
		// Read matrix size
		int m, n;
		inputFile >> m >> n;

		// Check if the matrix is large enough
		if (m != n)
		{
			std::cerr << "ERROR: Matrix not square" << std::endl;
			return 1;
		}

		int i, j;
		double value;

		// Reads file values and fill  matrix with those at specified positions
		while (inputFile >> i >> j >> value) 
		{
			val.push_back(value);
			i_idx.push_back(i);
  			j_idx.push_back(j);
		}
        inputFile.close();
	}

	else 
	{
		std::cerr << "ERROR: Could not open file" << std::endl;
		return 1;
	}

	// Convert from COO to CSR
	COO2CSR(val, i_idx, j_idx);

	// Build b and x vectors in Ax=b
	std::size_t dim = i_idx.size() - 1;
	std::vector<double> x(dim, 1.);
	std::vector<double> b(dim, 0.);

	// Call CG and record number of iterations needed for convergence
	int niter = CGSolver(val, i_idx, j_idx, b, x, 1.e-5);

	// Write solution vector to file if it converged
    if (niter > 0) 
    {
    	std::ofstream outputFile;
        outputFile.open(outputFileName.c_str());

        if (outputFile.is_open()) 
        {
        	// Use 4 decimal places and scientific notatin
            std::cout.setf(std::ios::scientific, std::ios::floatfield);
            std::cout.precision(4);

            for (unsigned int i = 0; i < i_idx.size(); i++) 
            {
                outputFile << x[i] << std::endl;
            }
            outputFile.close();
        }
        std::cout << "SUCCESS: CG solver converged in " << niter 
        << " iterations." << std::endl;
    }

    else 
    {
        std::cout << "CG solver diverged." << std::endl;
    }
	return 0;
}
