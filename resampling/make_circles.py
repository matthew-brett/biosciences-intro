from itertools import cycle
from collections import Counter
from random import shuffle, seed

import numpy as np

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt



class BallShower:

    def __init__(self, rows, cols,
                 ball_txt_fontsize=16,
                 ball_txt_color='white'):
        self.rows = rows
        self.cols = cols
        self.ball_txt_fontsize=ball_txt_fontsize
        self.ball_txt_color=ball_txt_color
        diameter = 1 / self.rows
        self.radius = diameter / 2
        self.centers_x = np.arange(self.rows) * diameter + self.radius
        self.centers_y = (np.arange(self.cols) * diameter + self.radius)[::-1]
        self._ax = None
        self._balls = []

    def ball_center(self, ball_no):
        ball_row = ball_no // self.cols
        ball_col = ball_no % self.cols
        return self.centers_x[ball_col], self.centers_y[ball_row]

    def ball_edges(self, ball_no):
        c_x, c_y = self.ball_center(ball_no)
        r = self.radius
        return (((c_x - r,  c_x - r), (c_y - r, c_y + r)),
                ((c_x - r,  c_x + r), (c_y + r, c_y + r)),
                ((c_x - r,  c_x + r), (c_y - r, c_y - r)),
                ((c_x + r,  c_x + r), (c_y - r, c_y + r)),
               )

    def _round_edge(self, edge, precision):
        return tuple(tuple(np.round(cs, precision)) for cs in edge)

    def bounding_edges(self, ball_nos, precision=6):
        all_edges = sum([self.ball_edges(b) for b in ball_nos], ())
        all_edges = [self._round_edge(es, precision) for es in all_edges]
        edge_counts = Counter(all_edges)
        return tuple(e for e, c in edge_counts.items() if c == 1)

    def ball_figure(self, balls, ax=None):
        if ax is None:
            plt.figure()
            ax = plt.gca()
        for ball_no, ball in enumerate(balls):
            c_x, c_y = self.ball_center(ball_no)
            bugs, color = balls[ball_no]
            p = mpatches.Circle((c_x, c_y), self.radius, color=color)
            plt.text(c_x, c_y,
                    bugs,
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=self.ball_txt_fontsize,
                    color=self.ball_txt_color)
            ax.add_patch(p)
        ax.axis('off')
        self._balls = balls
        self._ax = ax

    def plot_bb(self, ball_nos, color='red', linewidth=4):
        for xs, ys in self.bounding_edges(ball_nos):
            self._ax.plot(xs, ys, color=color, linewidth=linewidth)

    def mean_for(self, ball_nos, plot_ball, color='black'):
        values = [self._balls[i][0] for i in ball_nos]
        mu = np.mean(values)
        c_x, c_y = self.ball_center(plot_ball)
        self._ax.text(c_x, c_y,
                      'mean = {:.2f}'.format(mu),
                      horizontalalignment='center',
                      verticalalignment='center',
                      fontsize=self.ball_txt_fontsize,
                      color=color)
        return mu


beer_attract = [27, 20, 21, 26, 27, 31, 24, 21, 20,
                19, 23, 24, 28, 19, 24, 29, 18,
                20, 17, 31, 20, 25, 28, 21, 27]
n_beer = len(beer_attract)
beer_balls = list(zip(beer_attract, cycle(['#cc9900'])))

water_attract = [21, 22, 15, 12, 21, 16,
                 19, 15, 22, 24, 19, 23,
                 13, 22, 20, 24, 18, 20]
water_balls = list(zip(water_attract, cycle(['#33bbff'])))
balls = beer_balls + water_balls
n_balls = len(balls)

bshower = BallShower(7, 7)
beer_nos = range(n_beer)
water_nos = range(n_beer, n_balls)
empty_ball = n_balls + 2

bshower.ball_figure(balls)
plt.savefig('just_balls.png')

bshower.plot_bb(beer_nos)
beer_m = bshower.mean_for(beer_nos, empty_ball)
plt.savefig('beer_mean.png')

bshower.ball_figure(balls)
bshower.plot_bb(water_nos)
water_m = bshower.mean_for(water_nos, empty_ball)
plt.savefig('water_mean.png')
print(f'Actual difference: {beer_m - water_m:0.2f}')

seed(42)
shuffled = balls[:]

for i in range(3):
    shuffle(shuffled)
    bshower.ball_figure(shuffled)
    plt.savefig(f'fake_balls{i}.png')
    bshower.plot_bb(beer_nos)
    fb_m = bshower.mean_for(beer_nos, empty_ball)
    plt.savefig(f'fake_beer_mean{i}.png')

    bshower.ball_figure(shuffled)
    bshower.plot_bb(water_nos)
    fw_m = bshower.mean_for(water_nos, empty_ball)
    plt.savefig(f'fake_water_mean{i}.png')

    print(f'Fake difference {i}: {fb_m - fw_m:0.2f}')
