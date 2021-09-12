#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:10:42 2021

@author: pradyumna agrawal
"""
from DSAHeapEntry import DSAHeapEntry
import numpy as np

class DSAHeap():
    
    def __init__(self, size):
        self.__heapArray = np.empty(size, dtype = DSAHeapEntry)
        self.__size = size
        self.__count = 0
        for i in range(size):
            self.__heapArray[i] = DSAHeapEntry()
    
    def __trickleUp(self, index):
        ...
        
    def __trickleDown(self, index):
        ...
        
    def add(self, priority, value):
        ...
        
    def remove(self):
        ...
        
    def heapSort(self, array):
        ...
        
    

