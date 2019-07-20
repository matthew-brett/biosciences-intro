import math
from itertools import cycle
from random import shuffle

import numpy as np

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


class Logo:

    def __init__(self, start_x, start_y, **kwargs):
        self.x = start_x
        self.y = start_y
        self.kwargs = kwargs.copy()

    def move_to(self, x, y):
        plt.plot([self.x, x], [self.y, y],
                  **self.kwargs)
        self.x = x
        self.y = y

    def move_relative(self, rel_x, rel_y):
        self.move_to(self.x + rel_x, self.y + rel_y)


class BallShower:

    def __init__(self, n_balls1, n_balls2,
                ball_txt_fontsize=16,
                ball_txt_color='white'):
        self.n_balls1 = n_balls1
        self.n_balls2 = n_balls2
        self.ball_txt_fontsize=ball_txt_fontsize
        self.ball_txt_color=ball_txt_color
        self.n_balls = n_balls1 + n_balls2
        self.rows = self.cols = math.ceil(math.sqrt(self.n_balls))
        diameter = 1 / self.rows
        self.radius = diameter / 2
        self.centers_x = np.arange(self.rows) * diameter + self.radius
        self.centers_y = (np.arange(self.cols) * diameter + self.radius)[::-1]

    def ball_center(self, ball_no):
        ball_row = ball_no // self.cols
        ball_col = ball_no % self.cols
        return self.centers_x[ball_col], self.centers_y[ball_row]

    def ball_figure(self, balls):
        fig = plt.figure()
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
        return ax


def show_balls(balls1, balls2, border_color='red'):
    plt.figure()
    ax = plt.gca()
    balls = balls1 + balls2
    n_balls = len(balls)
    # Put into square box
    rows = cols = math.ceil(math.sqrt(n_balls))
    diameter = 1 / rows
    radius = diameter / 2
    centers_x = np.arange(rows) * diameter + radius
    centers_y = (np.arange(cols) * diameter + radius)[::-1]
    b_no = 0
    for c_y in centers_y:
        for c_x in centers_x:
            bugs, color = balls[b_no]
            p = mpatches.Circle((c_x, c_y), radius, color=color)
            plt.text(c_x, c_y,
                     bugs,
                     horizontalalignment='center',
                     verticalalignment='center',
                     fontsize=16,
                     color='white')
            ax.add_patch(p)
            b_no += 1
            if b_no == n_balls:
                break
    # Draw box around first set of balls
    last_balls1 = len(balls1) - 1
    row_last_first = last_balls1 // cols
    col_last_first = last_balls1 % cols
    row_pos = 1 - (row_last_first + 1) * diameter
    col_pos = (col_last_first + 1) * diameter
    logo = Logo(0, 1, color=border_color, linewidth=4)
    logo.move_to(0, row_pos)
    logo.move_to(col_pos, row_pos)
    if col_last_first != cols:
        logo.move_relative(0, diameter)
        logo.move_relative(1 - col_pos, 0)
    logo.move_to(1, 1)
    logo.move_to(0, 1)
    ax.axis('off')


beer_attract = [27, 20, 21, 26, 27, 31, 24, 21, 20,
                19, 23, 24, 28, 19, 24, 29, 18,
                20, 17, 31, 20, 25, 28, 21, 27]
beer_balls = list(zip(beer_attract, cycle(['#cc9900'])))

water_attract = [21, 22, 15, 12, 21, 16,
                 19, 15, 22, 24, 19, 23,
                 13, 22, 20, 24, 18, 20]
water_balls = list(zip(water_attract, cycle(['#33bbff'])))
balls = beer_balls + water_balls

bshower = BallShower(len(beer_balls), len(water_balls))
bshower.ball_figure(balls)
plt.show()
