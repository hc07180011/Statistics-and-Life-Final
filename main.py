import os
import numpy as np

from pybaseball_handler import get_history_data
from plot_statistics import plot_field, plot_distance, plot_angle
from simulation import do_simulation

def clear_nan(arr):
    arr = arr.to_numpy()
    return arr[np.logical_not(np.isnan(arr))]


def do_homework(img_dir, pybaseball_data):

    X, Y = clear_nan(pybaseball_data['hc_x']), clear_nan(pybaseball_data['hc_y'])

    plot_field(X, Y, os.path.join(img_dir, 'slides', 'drops.png'))
    plot_distance(X, Y, os.path.join(img_dir, 'slides', 'distance.png'))
    plot_angle(X, Y, os.path.join(img_dir, 'slides', 'angle.png'))

    do_simulation(X, Y, img_dir)

if __name__ == '__main__':

    img_dir, pybaseball_data = get_history_data('2000-01-01', '2017-01-01', batter='David Ortiz') # 左打
    do_homework(img_dir, pybaseball_data)

    img_dir, pybaseball_data = get_history_data('2000-01-01', '2021-01-01', pitcher='Clayton Kershaw') # 左投
    do_homework(img_dir, pybaseball_data)

    img_dir, pybaseball_data = get_history_data('2000-01-01', '2021-01-01', pitcher='Jacob deGrom') # 右投
    do_homework(img_dir, pybaseball_data)

    img_dir, pybaseball_data = get_history_data('2017-06-01', '2017-07-01')
    do_homework(img_dir, pybaseball_data)