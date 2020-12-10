import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
from tuning import fileding_range


def plot_field(X, Y, fig_path, annotations=[]):
    plt.scatter(X, Y, s=1)
    for ann in annotations:
        plt.scatter(ann[0], ann[1], s=((fileding_range(ann[0], ann[1]) * 100.0)), alpha=0.5)
    plt.title('{} samples'.format(len(X)))
    plt.savefig(fig_path)
    plt.close()

def plot_distance(X, Y, fig_path):
    drops = np.transpose(np.array([X, Y]), (1, 0))
    dis = np.sqrt(drops * drops).astype('int')
    p, x = np.histogram(dis, bins=1000)
    plt.plot(x[1:], p / np.sum(p))
    plt.xlabel('distance')
    plt.ylabel('ratio')
    plt.savefig(fig_path)
    plt.close()
