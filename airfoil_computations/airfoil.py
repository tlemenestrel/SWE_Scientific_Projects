import glob
import os
import math
import re
import sys

class Airfoil:

    """
    A class to represent an airfoil object.

    ...

    Attributes
    ----------
    airfoil_data_dir : str
        data directory to find the files
    chord_length : float
        choard length of the airfold
    C_l : float
        age of the person

    Methods
    -------
    info(additional=""):
        Prints the person's name and age.
    """
    def __init__(self, airfoil_data_directory_path):

        # Add a trailing / if it is missing, otherwise does nothings
        self.airfoil_data_dir = os.path.join(airfoil_data_directory_path, '')
        self.chord_length = 0
        self.C_l = 0
        self.joined_string = ''
        compute_list_of_summaries(self)

    def __str__(self):

        """ Print out the joined_string value

        Parameters:
        self: airfoil object

        Returns:
        str: joined_string"""

        return self.joined_string

    def get_airfoil_dir_path(self):

        """ Get the airfoil directory path

        Parameters:
        self: airfoil object

        Returns:
        str: airfoil_data_dir

       """

        return self.airfoil_data_dir

    def set_airfoil_dir_path(self, airfoil_data_directory_path):

        self.airfoil_data_dir = airfoil_data_directory_path

    def get_joined_string(self):

        """ Get the joined string

        Parameters:
        self: airfoil object

        Returns:
        str: joined_string

       """

        return self.airfoil_data_directory_path

    def set_joined_string(self, joined_string):

        """ Set the joined_string

        Parameters:
        self: airfoil object
        joined_string: str

       """

        self.joined_string = joined_string

    def get_chord_length(self):

        """ Get the chord length

        Parameters:
        self: airfoil object

        Returns:
        float: chord_length

       """

        return self.chord_length

    def set_chord_length(self, chord_length):

        """ Set the chord length

        Parameters:
        self: airfoil object
        chord_length: float

       """

        self.chord_length = chord_length

    def get_lift_coef(self):

        """ Get the lift coefficient 

        Parameters:
        self: airfoil object

        Returns:
        float: C_l

       """

        return self.C_l

    def set_lift_coef(self, C_l):

        """ Set the lift coefficient 

        Parameters:
        self: airfoil object
        C_l: float

       """

        self.C_l = C_l

def compute_list_of_summaries(airfoil):

    dir_path = airfoil.get_airfoil_dir_path()

    if os.path.exists(dir_path):

        a_files_path, a_coeffs, a_coeffs_fl = parse_alpha_coefs(dir_path)

        # Build a list of strings with a for loop where each line
        # contains information for a specifc alpha
        list_of_summaries = []

        for i in range(len(a_coeffs_fl)):

            a = a_coeffs_fl[i]

            CP = read_alpha_cordinates_file(a_files_path[i])

            x_coord_lst, y_coord_lst = read_xy_coordinate_file(dir_path)

            x_stagn_pt,y_stagn_pt,vl=find_stag(CP, x_coord_lst, y_coord_lst)

            chord_length = compute_chord_length(x_coord_lst, y_coord_lst)

            airfoil.set_chord_length(chord_length)

            d_x_lengths,d_y_lengths=compute_delta_lengths(x_coord_lst, y_coord_lst)

            chord_length = airfoil.get_chord_length()

            C_l = cmpt_lift_coefficient(CP,d_x_lengths,d_y_lengths,chord_length,a)

            # Formatting the final strings
            string = '{:7.4f}\t\t{:7.4f}\t\t({:7.4f}, {:7.4f})\t{:7.4f}'
            smr = string.format(float(a_coeffs[i]), C_l, x_stagn_pt, y_stagn_pt, vl)

            list_of_summaries.append(smr)

        # Sorting the list to have the lowest alpha at the top
        list_of_summaries.sort(key=lambda x: float(str(x)[0:3]))
        list_of_summaries.insert(0,'-----\t\t-------\t\t--------------------------')
        list_of_summaries.insert(0,'alpha\t\tcl\t\tstagnation pt')
        joined_string = "\n".join(list_of_summaries)
        airfoil.set_joined_string(joined_string)

    else:
        raise RuntimeError("Wrong path")

# Function to compute the lift coefficient for a particular alpha
def cmpt_lift_coefficient(CP_list, d_x_lengths, d_y_lengths,chord_length,alpha):

    delta_C_x_components = []
    delta_C_y_components = []
    C_x = 0
    C_y = 0
    C_l = 0

    for i in range(len(CP_list)):
     
        delta_C_x = -1 * (CP_list[i] * d_y_lengths[i] / chord_length)
        delta_C_y = CP_list[i] * d_x_lengths[i] / chord_length
        delta_C_x_components.append(delta_C_x)
        delta_C_y_components.append(delta_C_y)

    degrees = alpha

    alpha_in_radians = math.radians(degrees)

    C_x = sum(delta_C_x_components)
    C_y = sum(delta_C_y_components)
    C_l = C_y * math.cos(alpha_in_radians) - C_x * math.cos(alpha_in_radians)
    return C_l


def parse_alpha_coefs(airfoil_data_directory_path):

    try:
        # Open and read 
        alpha_files_path_list = glob.glob(airfoil_data_directory_path+'alpha*.dat')

        alpha_coeffs = []

        # Get the list of alpha coefficients
        for path in alpha_files_path_list:

            alpha_coef = re.search('alpha(.*).dat', path)
            alpha_coeffs.append(alpha_coef.group(1))

        alpha_coeffs_fl = [float(alpha) for alpha in alpha_coeffs]

        return alpha_files_path_list, alpha_coeffs, alpha_coeffs_fl

    except RuntimeError:
        print('Unvalid path')

def read_alpha_cordinates_file(alpha_file_path):

    CP_list = []

    with open(alpha_file_path, 'r') as alpha_coordinates_file:
        alpha_coordinates = alpha_coordinates_file.readlines()
        for line in alpha_coordinates:
             as_list = line.split()
             CP_list.append(as_list[0])

    # Remove the top element to only have the coordinates
    CP_list.pop(0)

    CP_list = [float(coordinate) for coordinate in CP_list]

    return CP_list

def read_xy_coordinate_file(airfoil_data_directory_path):

    # Open and read xy coordinates file
    xy_coordinates_file_path = airfoil_data_directory_path + 'xy.dat'

    x_coord_list = []
    y_coord_list = []

    with open(xy_coordinates_file_path, 'r') as xy_coordinates_file:
        xy_coordinates = xy_coordinates_file.readlines()
        for line in xy_coordinates:
             as_list = line.split()
             x_coord_list.append(as_list[0])
             y_coord_list.append(as_list[1])

    # Remove the name of the airfoil and only have the coordinates
    x_coord_list.pop(0)
    y_coord_list.pop(0)

    x_coord_list = [float(coordinate) for coordinate in x_coord_list]
    y_coord_list = [float(coordinate) for coordinate in y_coord_list]

    return x_coord_list, y_coord_list

def find_stag(CP_list, x_coord_list, y_coord_list):

    # Define a target and find the point closest to that target
    value = 1

    absolute_difference_function = lambda list_value : abs(list_value - value)

    vl = min(CP_list, key=absolute_difference_function)
    vl_ix = CP_list.index(vl)

    avg_x_stagn_pt = (x_coord_list[vl_ix + 1] + x_coord_list[vl_ix]) / 2
    avg_y_stagn_pt = (y_coord_list[vl_ix + 1] + y_coord_list[vl_ix]) / 2 

    return avg_x_stagn_pt, avg_y_stagn_pt, vl

def compute_chord_length(x_coord_list, y_coord_list):

    ldg_edge_x = x_coord_list[0]
    ldg_edge_y = y_coord_list[0]

    # Find the index of the smallest point, i.e. the coords of the trailing edge
    index_min = min(range(len(x_coord_list)), key=x_coord_list.__getitem__)

    trl_edge_x = x_coord_list[index_min]
    trl_edge_y = y_coord_list[index_min]

    chord_length = ((trl_edge_x - ldg_edge_x )**2 + (trl_edge_y-ldg_edge_y)**2 )
    chord_length = chord_length**0.5
    
    return chord_length

def compute_delta_lengths(x_coord_list, y_coord_list):

    delta_x_lengths = []
    delta_y_lengths = []

    for i in range(len(x_coord_list) - 1):

        delta_x = x_coord_list[i + 1] - x_coord_list[i] 
        delta_y = y_coord_list[i + 1] - y_coord_list[i] 
        delta_x_lengths.append(delta_x)
        delta_y_lengths.append(delta_y)

    return delta_x_lengths, delta_y_lengths

