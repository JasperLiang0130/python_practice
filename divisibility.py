# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def divisible_by_2(s):
    #s = str(n)
    if int(s[-1]) % 2==0:
        return True
    return False


def divisible_by_3(n):
    s = str(n)
    l = len(s)
    sum = 0
    while(l>0):
        sum = int(s[l-1])+sum
        l = l-1
    if sum%3==0:
        return True
    return False


def divisible_by_7(s):
    #s = str(n)
     # no greater than 2 digit
    while(len(s[:-1])>2):
       s =str(int(s[:-1]) - 2*int(s[-1]))     
    if int(s) % 7==0:
        return True
    return False

def primes1(n):
    '''Generates a list of prime numbers up to n'''
    primes = [] #list of primes
    for k in range(2, n+1):
        is_prime = True
        for p in primes: #Add code to test if k is prime
            if k%p==0: #If it is then call the following to add it to the list:
                is_prime = False
                print(k) #is checking which one is calculating now
        if is_prime:
            primes.append(k)
    return primes

def is_primes(n):
    if n in primes2(n):
        return True
    return False

def compound(n):
    compound = []
    primes = primes2(n)
    i = 0
    while n != 1:
        p = primes[i]
        if n % p==0:
            compound.append(p)
            n=n/p
        else:
            i = i + 1
    return compound

def factors(n):
    primes = sorted( primes2(n) )
    factors = []
    i = 0 #note we could also use an iterator rather than directly indexing primes 
    while n > 1:
        p = primes[i] 
        while n % p == 0:
            n = n // p
            factors.append(p)
        i += 1
    return factors




def primes2(n):
    '''Generates a list of prime numbers up to n'''
    primes = [] #list of primes
    for k in range(2, n+1):
        is_prime = True
        for p in primes: #Add code to test if k is prime
            if k%p==0: #If it is then call the following to add it to the list:
                is_prime = False
                #print(k) #is checking which one is calculating now
                break
        if is_prime:
            primes.append(k)
    return primes
 
import time
       
def time_primes1(n, show_msg=True):
    start = time.clock()
    total = len(primes1(n))
    elapsed = time.clock() - start
    if show_msg:
        print('Took {0:g} seconds to produce the {1} primes up to {2}'.format(elapsed, total, n))
    return elapsed
def time_primes2(n, show_msg=True):
    start = time.clock()
    total = len(primes2(n))
    elapsed = time.clock() - start
    if show_msg:
        print('Took {0:g} seconds to produce the {1} primes up to {2}'.format(elapsed, total, n))
    return elapsed



def time_function(pf, n, show_msg=True):
    start = time.clock()
    total = len(pf(n))
    elapsed = time.clock() - start
    if show_msg:
        print('Took {0:g} seconds to produce the {1} primes up to {2}'.format(elapsed, total, n))
    return elapsed