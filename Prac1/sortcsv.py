#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:50:33 2021

@author: pradyumna agrawal
"""

import DSAsorts2
import sys

f = open("RandomNames7000(2).csv")
a = f.readlines()
lst = [[int(i.split(',')[0]), i.split(',')[1]] for i in a]
s_type = sys.argv[1]

if s_type == 'b':
    blst = DSAsorts2.bubbleSort(lst)
    f = open("BubbleSortedNames.csv", "w")
    for i in blst:
        f.write(str(i[0]) + ',' + str(i[1]))
    
if s_type == 'i':
    ilst = DSAsorts2.insertionSort(lst)
    f = open("InsertionSortedNames.csv", "w")
    for i in ilst:
        f.write(str(i[0]) + ',' + str(i[1]))
    
if s_type == 's':
    slst = DSAsorts2.selectionSort(lst)
    f = open("SelectionSortedNames.csv", "w")
    for i in slst:
        f.write(str(i[0]) + ',' + str(i[1]))