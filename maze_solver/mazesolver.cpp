#include <iostream>
#include <fstream>

#define ni 201
#define nj 201

enum direction
{
    left,
    right,
    up,
    down
};

int main(int argc, char** argv) {
	// Check if the command line arguments are provided
	if (argc < 3)
	{
		std::cerr << "Not enough command-line arguments provided." << std::endl
		<< " ./mazesolver <maze file> <solution file>" << std::endl;
		return 1;
	}

	// Read the command-line arguments
	std::string inputFileName = argv[1];
	std::string outputFileName = argv[2];

	int maze[ni][nj];

	// Reading the input file
	std::ifstream inputFile (inputFileName);
	std::ofstream outputFile(outputFileName);

	if (inputFile.is_open()) 
	{	
		// Read the size of the array
		int nif, njf;
		inputFile >> nif >> njf;
		if (nif > ni or njf > nj) {

	    	std::cerr << "Not enough storage available" << std::endl;
	    	return 1; // Quit the program if not enough storage available
	}

		// Read the data and populate the array
		for (int i = 0; i < nif; i++) 
		{
		    for (int j = 0; j < njf; j++) 
		    {
		      maze[i][j] = 0;
		    }
		}

		int i,j;

		while(inputFile >> i >> j) 
		{
			maze[i][j] = 1;
		}

        int current_row;
        int current_col;

        // Find the entry in the first row 
        for (j = 0; j < njf; j++)
        {
            // Search the first row
            current_row = 0;

            if (maze[0][j] == 0)
            {
                // Define the first column as the entry of the maze
                current_col = j;
            }
        }

        outputFile << current_row << " " << current_col << std::endl;

        /*
        The while loop is used to iterate over the maze and find the way out.
        It runs until the maze is exited. It will switch between left, right,
        up and down directions and try to find the exit.

        At each step, it will:

        -try to go right. If not possible:
        -try to go forward. If not possible
        -try to go left. If not possible:
        -try to go backward.

		At each step, the code will:

		-update the current row column position
		-write the current postion to the output
        */

        // Setting the initial direction
        direction d = down;

		while (current_row != nif - 1)

        {
            switch(d)

            {
                case left:

                    if (maze[current_row - 1][current_col] == 0)
                    {
                        current_row--;
                        d = up;
                    }

                    else if (maze[current_row][current_col - 1] == 0)
                    {
                        current_col--;
                        d = left;
                    }

                    else if (maze[current_row + 1][current_col] == 0)
                    {
                        current_row++;
                        d = down;
                    }

                    else
                    {
                        current_col++;
                        d = right;
                    }
                    outputFile << current_row << " " <<current_col<< std::endl;
                    break;

                case down:

                    if (maze[current_row][current_col - 1] == 0)
                    {
                        current_col--;
                        d = left;
                    }
                    else if (maze[current_row + 1][current_col] == 0)
                    {
                        current_row++;
                        d = down;
                    }
                    else if (maze[current_row][current_col + 1] == 0)
                    {
                        current_col++;
                        d = right;
                    }
                    else
                    {
                        current_row--;
                        d = up;
                    }
                    outputFile << current_row << " " <<current_col<< std::endl;
                    break;

                case right:

                    if (maze[current_row + 1][current_col] == 0)
                    {
                        current_row++;
                        d = down;
                    }
                    else if (maze[current_row][current_col + 1] == 0)
                    {
                        current_col++;
                        d = right;
                    }
                    else if (maze[current_row - 1][current_col] == 0)
                    {
                        current_row--;
                        d = up;
                    }
                    else
                    {
                        current_col--;
                        d = left;
                    }
                    outputFile << current_row << " " << current_col<<std::endl;
                    break;

                case up:

                    if (maze[current_row][current_col + 1] == 0)
                    {
                        current_col++;
                        d = right;
                    }
                    else if (maze[current_row - 1][current_col] == 0)
                    {
                        current_row--;
                        d = up;
                    }
                    else if (maze[current_row][current_col - 1] == 0)
                    {
                        current_col--;
                        d = left;
                    }
                    else
                    {
                        current_row++;
                        d = down;
                    }
                    outputFile << current_row << " " <<current_col<< std::endl;
                    break;
            }
        }
    }
    return 0;
}
