#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:39:08 2021

@author: pradyumna agrawal
@student ID: 20046165
"""
def moveDisk(src, dest, level):
    print("\t" * (level) + "moving one disc from disc " + str(src) + "to " + str(dest))


#_towerOfHanoi is a private metho

def _towerOfHanoi(n, src, dest, level):
    print("\t" * level + "towerOfHanoi(" + str(n) + "," + str(src) + "," + str(dest) + ')')
    if n == 1:
        moveDisk(src, dest, level)
    else:
        tmp = 6 - src - dest
        _towerOfHanoi(n-1, src, tmp, level+1)
        moveDisk(src, dest, level+1)
        _towerOfHanoi(n-1, tmp, dest, level+1)

#wrapper method
def towerOfHanoi(rings, deck1, deck2):
    if rings < 1:
        raise ValueError(str(rings) + " is not a valid input.") #raising exception
    else:
        return _towerOfHanoi(rings, deck1, deck2, 0)

#main method        
def main():
    num = input("How many rings you want in the the game")
    try:
        towerOfHanoi(int(num), 1, 3)
    except ValueError as err:
        print(err, "enter an INTEGER greater than 1.") #catching exception
        
if __name__ == "__main__":
    main()
