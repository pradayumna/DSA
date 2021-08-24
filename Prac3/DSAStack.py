#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:42:01 2021

@author: pradyumna agrawal
"""
import numpy as np

class stack():
    
    maxSize = 100
    
    def __init__(self):
        self.stackArray = np.empty(self.maxSize, dtype = object)
        self.size = 0
        print(len(self.stackArray))
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == 100
    
    def count(self):
        return self.size
    
    def top(self):
        if not self.isEmpty():
            return self.stackArray[self.size-1]
        else:
            raise IndexError('The stack is empty')
            
    def pop(self):
        if not self.isEmpty():
            self.size = self.size-1
            return self.stackArray[self.size]
        else:
            raise IndexError('The stack is empty')
            
    def push(self, num):
        if not self.isFull():
            self.stackArray[self.size] = num
            self.size = self.size + 1
        else:
            raise IndexError('The stack is full')
    

