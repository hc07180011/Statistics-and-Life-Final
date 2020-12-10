import numpy as np
from pybaseball_handler import find_player_by_id, get_history_data
from plot_statistics import plot_field, plot_distance


def clear_nan(arr):
    arr = arr.to_numpy()
    return arr[np.logical_not(np.isnan(arr))]

if __name__ == '__main__':
    pybaseball_data = get_history_data('2000-01-01', '2017-01-01', batter=find_player_by_id('David Ortiz'))
    X, Y = clear_nan(pybaseball_data['hc_x']), clear_nan(pybaseball_data['hc_y'])
    plot_field(X, Y, 'drops.png')
    plot_distance(X, Y, 'distance.png')