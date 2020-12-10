import os
import imageio
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

from tuning import fileding_range


def gen_gif(img_dir, gif_path):
    images = []
    filenames = os.listdir(img_dir)
    filenames = sorted(filenames)
    for filename in filenames:
        try:
            images.append(imageio.imread(os.path.join(img_dir, filename)))
        except:
            pass
    imageio.mimsave(gif_path, images, duration=(12.0 / len(images)))


def plot_field(X, Y, fig_path, annotations=[]):
    plt.scatter(X, Y, s=1)
    for ann in annotations:
        plt.scatter(ann[0], ann[1], s=((fileding_range(ann[0], ann[1]) * 100.0)), alpha=0.5)
    plt.title('{} samples'.format(len(X)))
    plt.savefig(fig_path)
    plt.close()


def pdf_to_bin(p, bin):
    p, x = np.histogram(p, bins=bin)
    zeros = np.where(np.array(p) == 0)[0]
    for zero in zeros:
        if zero and zero != len(p)-1:
            p[zero] = (p[zero-1] + p[zero+1]) / 2.0
    return x[1:], p / np.sum(p)


def plot_distance(X, Y, fig_path):
    drops = np.transpose(np.array([X, Y]), (1, 0))
    dis = np.sqrt(drops * drops).astype('int')
    x, p = pdf_to_bin(dis, 200)
    plt.plot(x, p)
    plt.xlabel('distance')
    plt.ylabel('ratio')
    plt.savefig(fig_path)
    plt.close()


def plot_angle(X, Y, fig_path):
    angle = np.arctan2(X, Y) * 180.0 / np.pi
    x, p = pdf_to_bin(angle, 360)
    plt.xticks(np.arange(-180, 181, 30))
    plt.plot(x, p)
    plt.xlabel('degree')
    plt.ylabel('ratio')
    plt.savefig('angle.png')
    plt.close()