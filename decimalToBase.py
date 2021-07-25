# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 14:27:42 2018

@author: 育誠
"""

def dec2smaller(d, base):
    q, r = divmod(d, base)
    if q == 0:
        return str(r)
    return dec2smaller(q, base) + str(r)


import string
digits = string.digits + string.ascii_uppercase

def dec2other(q, base):
    n = ''
    while q != 0:
        q, r = divmod(q, base)
        n = digits[r] + n
    return n if len(n) > 0 else '0'