#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 08:42:01 2021

@author: pradyumna agrawal
"""
from linkedKList import DSALinkedList

class stack():
    
    
    def __init__(self):
        self.stackArray = DSALinkedList()
        
    def __iter__(self):
        currNd = self.stackArray.head
        while currNd is not None:
            yield currNd.value 
            currNd = currNd.next
        
    def isEmpty(self):
        return self.stackArray.isEmpty()

    
    def count(self):
        return self.size
    
    def top(self):
        if not self.isEmpty():
            return self.stackArray.peekFirst()
        else:
            raise IndexError('The stack is empty')
            
    def pop(self):
        if not self.isEmpty():
            return self.stackArray.removeFirst()
        else:
            raise IndexError('The stack is empty')
            
    def push(self, num):
        self.stackArray.insertFirst(num)
    

