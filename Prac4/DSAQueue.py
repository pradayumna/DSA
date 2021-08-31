#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:22:11 2021

@author: pradyumna agrawal 
code for queues with linked list
"""

from linkedKList import DSALinkedList


class queue():
    
    
    def __init__(self):
        self.queueArray = DSALinkedList()
        
    def __iter__(self):
        currNd = self.queueArray.head
        while currNd is not None:
            yield currNd.value 
            currNd = currNd.next
    
    def isEmpty(self):
        return self.queueArray.isEmpty()

    
    def enqueue(self, num):
        self.queueArray.insertLast(num)
            
    def dequeue(self):
        if not self.isEmpty():
            return self.queueArray.removeFirst()
        else:
            raise IndexError('Queue is empty')
    
    def peek(self):
        if not self.isEmpty():
            return self.queueArray.peekFirst()
        else:
            raise IndexError("Queue is empty")
            