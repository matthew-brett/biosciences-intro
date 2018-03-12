""" Make a fake Otter dataset
"""
from __future__ import division

import numpy as np

import pandas as pd

names = ['activity', 'grass', 'herb', 'bush', 'humans', 'coverage']

N, P = 21, len(names)

df = pd.DataFrame(columns=names)

def stdize(vec, lo=0, hi=4):
    vec = vec - np.min(vec)
    vec = vec / np.max(vec)
    vec = vec * (hi - lo + 1) + lo
    return np.floor(vec).astype(int)


df['activity'] = np.random.randint(0, 5, size=(N,))
df['grass'] = np.random.normal(10, 5, size=(N,)) + 0.5 * df['activity']
bushy = np.random.randint(0, 5, size=(N,))
df['grass'] = stdize(np.random.randint(0, 5, size=(N,)) + 0.8 * bushy)
df['herb'] = stdize(np.random.randint(0, 5, size=(N,)) + 0.8 * bushy)
df['bush'] = stdize(np.random.randint(0, 5, size=(N,)) + 0.8 * bushy)
df['coverage'] = stdize(np.random.randint(0, 5, size=(N,)) + 0.8 * bushy)
df['humans'] = np.random.randint(0, 5, size=(N,))

df.to_csv('fake_scat.csv', index=False)

df2 = pd.read_csv('fake_scat.csv')
