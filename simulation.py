import os
import time
import itertools
import numpy as np
from scipy.spatial import distance

from tuning import fileding_range
from plot_statistics import plot_field, gen_gif

def do_simulation(X, Y):

    drops = np.transpose(np.array([X, Y]), (1, 0))
    trial_points = np.array(list(itertools.product(np.arange(-100, 101, 1), np.arange(0, 200, 1))))
    fielder_num = 9

    #ans = [[151, 152], [112, 155], [156, 168], [131, 85], [106, 166], [184, 104], [78, 101]]

    results = [[0, 0]]
    for _ in range(fielder_num - 2):
        try:
            distances = distance.cdist(trial_points, drops)
        except:
            break
        fielding = fileding_range([x[0] for x in drops], [y[1] for y in drops])
        catchable = np.array([np.count_nonzero(dis < fielding) for dis in distances])
        max_catch_player = np.argmax(catchable)
        
        results.append([trial_points[max_catch_player][0], trial_points[max_catch_player][1]])
        drops = [drops[i] for i, elem in enumerate(distances[max_catch_player] < fielding) if elem == False]

    plot_field(X, Y, os.path.join('img', 'frames', '{}.png'.format(time.time())), annotations=results)
    gen_gif(os.path.join('img', 'frames'), os.path.join('img', 'slides', 'tmp.gif'))