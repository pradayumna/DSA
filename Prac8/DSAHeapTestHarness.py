#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:39:50 2021

@author: pradyumna agrawal
"""
from DSAHeap import DSAHeap, DSAHeapIO
import random
choice1 = input("what do you want to work with?\n1. A CSV file\n2. Abitrary Random Heap\n3. Check exceptional cases")

if choice1 == '1':
    A = DSAHeapIO()
    A.loadCSV('RandomNames7000.csv')
    A.writeSortedCSV('sorted10.csv')

if choice1 == '2':      
    length = random.randint(5, 50)  
    B = DSAHeap(length)
    for i in range(length):
        a = random.randint(1, 100)
        B.add(a, a)
    print(B)
    
    input('press enter to continue')
    print('now we will remove the priority element from the hash')
    B.remove()
    print(B)
    input('press enter to continue')
    print('now we will sort the hash')
    B = B.heapSort()
    print(B)
    
if choice1 == '3':
    B= DSAHeap(5)
    try:
        B.remove()
    except IndexError as err:
        print(err)
        
    input('press enter to check exception number 2 : adding to a full heap')
    B = DSAHeap(1)
    try:
        B.add(1, 1)
        B.add(2, 2)
    except IndexError as err:
        print(err)
    
    input('press enter to check exception number 3 : Sorting an empty heap')
    B = DSAHeap(5)
    try:
        B.heapSort()
    except IndexError as err:
        print(err)