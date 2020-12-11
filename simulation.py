import os
import time
import itertools
import numpy as np
from scipy.spatial import distance

from tuning import fileding_range
from plot_statistics import plot_field, gen_gif

def do_simulation(X, Y, img_dir, delete_frames=True, window=100, only_last=False, make_gif=True):

    if delete_frames:
        for f in os.listdir(os.path.join(img_dir, 'frames')):
            os.remove(os.path.join(img_dir, 'frames', f))

    if not only_last:
        start, end = window, len(X)
    else:
        start, end = len(X), len(X)+1

    for i in range(start, end, window):

        drops = np.transpose(np.array([X[:i], Y[:i]]), (1, 0))
        catched = [[], []]
        fielder_num = 9

        results = [[0, 25], [0, 0]]
        for idx in range(fielder_num - 2):
            if idx < 4:
                trial_points = np.array(list(itertools.product(np.arange(-30, 31, 1), np.arange(0, 70, 1))))
                trial_points = trial_points[np.transpose(distance.cdist(trial_points, [[0, 0]]), (1, 0))[0] > 25]
            else:
                trial_points = np.array(list(itertools.product(np.arange(-60, 60, 1), np.arange(0, 110, 1))))
                trial_points = trial_points[np.transpose(distance.cdist(trial_points, [[0, 0]]), (1, 0))[0] < 110]
            try:
                distances = distance.cdist(trial_points, drops)
            except:
                break
            fielding = fileding_range([x[0] for x in drops], [y[1] for y in drops])
            catchable = np.array([np.count_nonzero(dis < fielding) for dis in distances])
            max_catch_player = np.argmax(catchable)
            
            results.append([trial_points[max_catch_player][0], trial_points[max_catch_player][1]])

            for x, y in [drops[i] for i, elem in enumerate(distances[max_catch_player] >= fielding) if elem == False]:
                catched[0].append(x), catched[1].append(y)

            drops = [drops[i] for i, elem in enumerate(distances[max_catch_player] < fielding) if elem == False]

        plot_field([x[0] for x in drops],
                   [y[1] for y in drops],
                   os.path.join(img_dir, 'frames', '{}.png'.format(time.time())),
                   catched[0],
                   catched[1],
                   annotations=results)

    gen_gif(os.path.join(img_dir, 'frames'), os.path.join(img_dir, 'slides', 'plot.gif'))