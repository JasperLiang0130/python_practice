'''
For KIT103/KMA115 Practical 8: Euclidean Algorithm and applications
Revised: 2016-09-08
Author: James Montgomery (james.montgomery@utas.edu.au)

An implementation of Java's string hash function (both the original
and a version that wraps to a certain number of buckets) and a wrapper
for Python's hash() function can wrap its result to the number of
buckets.

Also includes a function to creating a frequency distribution of
selected buckets for a given set/list of words, number of buckets and
hash function.

Suggested usage: Download tlw.txt (or any set of words) then
>>> words = [ l.rstrip() for l in open('tlw.txt') ]
>>> from matplotlib import pyplot as plt
>>> size = 10
>>> dist = distribution(words, size, java_hash)
>>> plt.bar(range(0,size), dist)
>>> plt.show()
'''
from matplotlib import pyplot as plt

words = [ l.rstrip() for l in open('tlw.txt') ]  

def test():
    size = 31
    dist = distribution(words, size, py_hash)
    plt.bar(range(0,size), dist)
    plt.show()

from string import ascii_lowercase as alphabet
def o():
    for c in alphabet:
        print(ord(c)%31)


def java_hash_nowrap(word):
    '''A reimplemenatation of the Java String hashCode() method.
    If you're curious you can take a look at the original Java code:
    http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/8u40-b25/java/lang/String.java?av=f#1453
    '''
    h = 0
    for c in word:
        h = 31 * h + ord(c)  # if size equal 31, then 31*h doesn't work because 31*h mod 31 equal 0
    return h

def java_hash(word, size):
    return java_hash_nowrap(word) % size
    
def py_hash(word, buckets):
    return hash(word) % buckets

def distribution(words, size, h):
    '''Returns a list of frequencies with which each position is
    selected by the hash function h.'''
    table = [0] * size
    for w in words:
        i = h(w, size)
        table[i] += 1
    return table
