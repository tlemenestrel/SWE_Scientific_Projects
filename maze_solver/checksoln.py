from numpy import sqrt, array
from scipy import sparse
import sys

# Exit system if command line args are not provided
if len(sys.argv) != 3:
    print('Usage:')
    print('  python3 {} <maze file> <solution file>'.format(sys.argv[0]))
    sys.exit(0)

if len(sys.argv) == 3:
    maze_file = sys.argv[1]
    solution_file = sys.argv[2]

    with open(maze_file) as maze_file:
        # Store file header as the dimensions of the maze
        maze_dim = next(maze_file)
        lines = maze_file.readlines()

    row_l = []
    col_l = []
    data_l = []

    for line in lines:
        (row, col) = line.split()
        row_l.append(int(row))
        col_l.append(int(col))
        data_l.append(1) 

    rows = array(row_l)
    cols = array(col_l)
    data = array(data_l)

    # Store the dimensions of the maze
    (n_rows, n_cols) = maze_dim.split()
    n_rows = int(n_rows)
    n_cols = int(n_cols)

    # Use a csr matrix to store the maze
    maze=sparse.csr_matrix((data,(rows,cols)),shape=(n_rows,n_cols)).toarray()

    # Open solution file
    with open(solution_file) as solution_file:
        lines = solution_file.readlines()

    # Get solution path for each line in lines
    for line in lines:
        (row, col) = line.split()
        row = int(row)
        col = int(col)
        # Exit if solution goes through a wall
        if maze[row][col] != 0:
            print('Solution is invalid!')
            sys.exit(0)
        # Exit if solution is out of bounds
        elif row > n_rows - 1:
            print('Solution is invalid!')
            sys.exit(0)
        # Exit if solution is out of bounds
        elif col > n_cols - 1:
            print('Solution is invalid!')
            sys.exit(0)

    # Verify the step size is always 1 in the solution
    for i in range(1, len(lines)):
        line1 = lines[i - 1]
        (row1, col1) = line1.split()

        line2 = lines[i]
        (row2, col2) = line2.split()

        row1 = int(row1)
        row2 = int(row2)
        col1 = int(col1)
        col2 = int(col2)

        # Define the step length
        step_length = sqrt((row1-row2)**2 + (col1-col2)**2)
        
        # Check step length is 1
        if step_length != 1:
            print('Solution is invalid!')
            sys.exit(0)

    # Get rows of entry and exit
    first_line = lines[0]
    last_line = lines[-1]

    (first_row, first_col) = first_line.split()
    (last_row, last_col) = last_line.split()

    first_row = int(first_row)
    last_row = int(last_row)

    # Exit if maze is not entered by first row
    if first_row != 0:
        print('Solution is invalid!')
        sys.exit(0)

    # Exit if maze is not exited by last row
    elif last_row != n_rows - 1:
        print('Solution is invalid!')
        sys.exit(0)

    # Solution is valid if it passes all the previous test cases
    else:
        print('Solution is valid!')
        sys.exit(0)
        