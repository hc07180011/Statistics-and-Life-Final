import numpy as np


def fileding_range(X, Y):
    # 5.0 + dis / 2.0 / 30.0 * 4.5
    if not isinstance(X, list):
        dis = np.sqrt(X * X + Y * Y)
    else:
        drops = np.transpose(np.array([X, Y]), (1, 0))
        dis = np.sqrt(np.sum(drops * drops, axis=1))
    return 5.0 + 1.6 * (dis ** 1.8 / 500.0)