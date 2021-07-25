# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 16:29:50 2018

@author: 育誠
"""

from string import ascii_lowercase as alphabet
from itertools import product
from math import factorial

def permutation(n,k):
    return { ''.join(p) for p in product(n, repeat=k) }