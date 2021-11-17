from itertools import chain
from math import sqrt
from scipy.sparse import csr_matrix
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np 

class Truss:

    """
    A Truss class to analyse beams and joins of a truss. 

    ...

    Attributes
    ----------
    __joints_file_path : str
        data directory to find the files for the joints
    __beams_file_path : str
        data directory to find the files for the beams

    Methods
    -------
    __init__(self, joints_file_path, beams_file_path):
        Initializes a Truss object and sets the joints file path and beams file
        path as attributes

    PlotGeometry(self, save_path):
        Plots a truss and saves the plot at the save path given as argument

    __repr__(self):

    get_joints_file_path(self):
        returns the joints_file_path of a Truss object

    get_beams_file_path(self):
        returns the beams file path of an object
    """

    def __init__(self, joints_file_path, beams_file_path):

        """
        Creates a Truss object given the paths of the beams and joints files.

        Parameters:
        ------
        self: Truss object
        joints_file_path: str 
        """

        self.__joints_file_path = joints_file_path
        self.__beams_file_path = beams_file_path
        self.__final_string = ''

    def __repr__(self):

        """
        Given a Truss object, represents the Truss objects as a string

        Parameters:
        ------
        self: Truss object

        Returns:
        ------
        __output_string: str
        """
        return self.__final_string

    def compute_static_equilibrium(self):

        """
        Computes the beam forces of a truss given a Truss object. Sets the
        final string of the Truss object as the output.

        Parameters:
        ------
        self: Truss object
            the truss for which to plot the geometry
        """
        try:
            # Read the joints file
            points = []
            X_coord = []
            Y_coord = []
            F_X = []
            F_Y = []
            zero_disp = []

            with open(self.get_joints_file_path(), 'r') as joints_file:
                xy_coords = joints_file.readlines()
                for line in xy_coords:
                    line_list = line.split()
                    points.append(line_list[0])
                    X_coord.append(line_list[1])
                    Y_coord.append(line_list[2])
                    F_X.append(line_list[3])
                    F_Y.append(line_list[4])
                    zero_disp.append(line_list[5])

            # Removes the first element (to remove the first line of the file)
            points.pop(0)
            X_coord.pop(0)
            Y_coord.pop(0)
            F_X.pop(0)
            F_Y.pop(0)
            zero_disp.pop(0)

            X_coord = [float(coord) for coord in X_coord]
            Y_coord = [float(coord) for coord in Y_coord]
            F_X = [float(force) for force in F_X]
            F_Y = [float(force) for force in F_Y]
            zero_disp = [int(disp) for disp in zero_disp]

            # Save every xy pair as a list of tupples
            XY_coords = list(zip(X_coord,Y_coord, points))

            num_rigid_point = zero_disp.count(1)

            # Read beam file 
            beam_num = []
            Ja = []
            Jb = []

            with open(self.get_beams_file_path(), 'r') as beams_file:
                lines = beams_file.readlines()
                for line in lines:
                    line_list = line.split()
                    beam_num.append(line_list[0])
                    Ja.append(line_list[1])
                    Jb.append(line_list[2])

            beam_num.pop(0)
            Ja.pop(0)
            Jb.pop(0)

            Ja = [int(joint) for joint in Ja]
            Jb = [int(joint) for joint in Jb]
            beam_num = [int(beam) for beam in beam_num]

            num_beams = len(beam_num)
            num_joints = len(points)

            final_output = []

            # Iterate over each joint
            for i in range(num_joints):

                joint = i + 1
                connected_joints = []
                connected_beams = []
                rigid = zero_disp[i]

                # Find connected beams and joints for a given joint
                for i in range(num_beams):
                    if(Ja[i] == joint):
                        connected_joints.append(Jb[i])
                        connected_beams.append(beam_num[i])
                    elif(Jb[i] == joint):
                        connected_joints.append(Ja[i])
                        connected_beams.append(beam_num[i])

                output_list = []

                for j in range(len(connected_beams)):

                    # Find the xy coords of the connect joint
                    connected_joint = str(connected_joints[j])
                    match_tpl = [tp for tp in XY_coords if tp[2] == connected_joint]
                    X_connect = match_tpl[0][0]
                    Y_connect = match_tpl[0][1]

                    # Find the xy coords of the joint we are working on
                    match_tpl = [tp for tp in XY_coords if tp[2] == str(joint)]
                    X_joint = match_tpl[0][0]
                    Y_joint = match_tpl[0][1]

                    # Find the vector between two joints
                    vector = (X_joint - X_connect, Y_joint - Y_connect)

                    vector_norm = sqrt(vector[0] **2 + vector[1] ** 2)

                    # Normalize the vector
                    normalized_vector=tuple(cd/vector_norm for cd in vector)

                    # Add the beam number related to the vector
                    normalized_vector += (connected_beams[j],)
                    output_list.append(normalized_vector)

                final_output.append(output_list)        

            # Build lists to store the values to fill the csr matrix
            total_rows = []
            total_cols = []
            total_values = []

            count = 0

            # For each set of vector, build the related equations
            for i in range(len(final_output)):

                list_values = final_output[i]

                # For the first equation
                cols = []
                rows = []
                values = []

                # Build the row number
                for j in range(len(list_values)):

                    rows.append(count)
                
                count += 1

                # Build the colum numbers
                for w in range(len(list_values)):

                    col_num = (list_values[w][2] - 1)
                    cols.append(col_num)
                
                # Build the values
                for z in range(len(list_values)):

                    value = (list_values[z][0])
                    values.append(value)

                total_rows.append(rows)
                total_cols.append(cols)
                total_values.append(values)

                # For the second equation
                cols = []
                rows = []
                values = []

                for j in range(len(list_values)):

                    rows.append(count)
            
                count += 1

                for w in range(len(list_values)):

                    col_num = (list_values[w][2] - 1)
                    cols.append(col_num)
                
                for z in range(len(list_values)):

                    value = (list_values[z][1])
                    values.append(value)

                total_rows.append(rows)
                total_cols.append(cols)
                total_values.append(values)

            rows = [item for sublist in total_rows for item in sublist]
            cols = [item for sublist in total_cols for item in sublist]
            vals = [item for sublist in total_values for item in sublist]

            # Add the RF1 and RF2 forces that are missing
            points_in_static = []

            for i in range(len(zero_disp)):

                if(zero_disp[i] == 1):

                    points_in_static.append(int(points[i]))

            row_1 = [2 * points_in_static[0] - 2]
            row_2 = [2 * points_in_static[0] - 1]
            row_3 = [2 * points_in_static[1] - 2]
            row_4 = [2 * points_in_static[1] - 1]

            col_1 = [num_beams]
            col_2 = [num_beams + 1]
            col_3 = [num_beams + 2]
            col_4 = [num_beams + 3]

            value_1 = [1]
            value_2 = [1]
            value_3 = [1]
            value_4 = [1]

            Rf_row = row_1 + row_2 + row_3 + row_4
            RF_cl = col_1 + col_2 + col_3 + col_4
            RF_val = value_1 + value_2 + value_3 + value_4

            rows += Rf_row
            cols += RF_cl
            vals += RF_val

            size = 2 * num_joints

            # Build the CSR matrix using the lists built before
            A = csr_matrix((vals, (rows, cols)), shape=(size, size)).toarray()

            # Build the B vector equal to minus each F force
            B_list = list(zip(F_X, F_Y))
            B_list = list(chain(*B_list))

            B = np.array(B_list)
            B = B * -1

            # Solve the linear system of equations        
            x = np.linalg.solve(A, B)

            # Remove the RF forces too only have the beam forces
            output = x[:-4]

            output_list = list(output.tolist())

            list_of_summaries = []

            for i in range(len(output_list)):

                string = '{:3}        {:9.3f}'
                beam_num = i + 1
                force = output_list[i]
                smr = string.format(beam_num, force)
                list_of_summaries.append(smr)
            list_of_summaries.insert(0,'-----------------')
            list_of_summaries.insert(0,' Beam       Force')
            joined_string = "\n".join(list_of_summaries)

            self.__final_string = joined_string

        except ValueError:
            raise RuntimeError('Truss geometry not suitable.')
        except np.linalg.LinAlgError as err:
            raise RuntimeError('Cannot solve the linear system') 

    def plot_geometry(self, save_path):

        """
        Plots the geometry of a truss using matplotlib, given a Truss object 
        and the path to save the plot. It reads the xy coordinates of each
        joints, reads the beam file to understand which joints are connected
        by a beam and plots a line for each joints connected by a beam.

        Parameters:
        ------
        self: Truss object
            the truss for which to plot the geometry
        save_path: str
            the path to save the plot
        """

        points = []
        X_coord = []
        Y_coord = []

        with open(self.get_joints_file_path(), 'r') as joints_file:
            xy_coords = joints_file.readlines()
            for line in xy_coords:
                line_list = line.split()
                points.append(line_list[0])
                X_coord.append(line_list[1])
                Y_coord.append(line_list[2])
        # Removes the first element (to remove the first line of the file)
        points.pop(0)
        X_coord.pop(0)
        Y_coord.pop(0)
        
        X_coord = [float(coord) for coord in X_coord]
        Y_coord = [float(coord) for coord in Y_coord]

        # Save every xy pair as a list of tupples
        XY_coords = list(zip(X_coord,Y_coord, points))

        # Read beam file to compute the connections
        Ja = []
        Jb = []

        with open(self.get_beams_file_path(), 'r') as beams_file:
            lines = beams_file.readlines()
            for line in lines:
                line_list = line.split()
                Ja.append(line_list[1])
                Jb.append(line_list[2])
        # Removes the first element (to remove the first line of the file)
        Ja.pop(0)
        Jb.pop(0)

        # Create a tuple to store the connections between points
        matches = list(zip(Ja, Jb))

        for i in range(len(matches)):

            first_coord = int(matches[i][0])
            second_coord = int(matches[i][1])

            X_1 = XY_coords[first_coord - 1][0]
            Y_1 = XY_coords[first_coord - 1][1]
            X_2 = XY_coords[second_coord - 1][0]
            Y_2 = XY_coords[second_coord - 1][1]

            x_values = [X_1, X_2]
            y_values = [Y_1, Y_2]

            plt.plot(x_values, y_values, 'b')
        plt.savefig(save_path)

    def get_joints_file_path(self):

        """
        Given a Truss object, returns the joints file path.
        
        Parameters:
        ------
        self: Truss object
            the truss for which to get the joints file path

        Returns:
        ------
        __joint_file_path: str
            the path of the joints file
        """

        return self.__joints_file_path

    def get_beams_file_path(self):

        """
        Given a Truss object, returns the beams file path.
        
        Parameters:
        ------
        self: Truss object
            the truss for which to get the beams file path

        Returns:
        ------
        __beams_file_path: str
            the path of the beams file
        """
        return self.__beams_file_path

