import matplotlib.pyplot as plt
import sys
import truss

if len(sys.argv) < 3:
    print('Usage: Please provide the required argumentss')

joints_file_path = sys.argv[1]
beams_file_path = sys.argv[2]
save_path = ''

if (len(sys.argv)) == 4:

    save_path == sys.argv[3]

try:
    truss = truss.Truss(joints_file_path,beams_file_path)
    truss.compute_static_equilibrium()
    print(truss)
    if (len(sys.argv)) == 4:
        truss.plot_geometry(save_path)
except RuntimeError as e:
    print('ERROR: {}'.format(e))
    sys.exit(2)

