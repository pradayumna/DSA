#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:22:11 2021

@author: pradyumna agrawal 
code for queues with linked list
"""

from linkedKList import DSALinkedList
#change name to list

class queue():
    
    
    def __init__(self):
        self.queueArray = DSALinkedList()
        self._count = 0
        
    def __iter__(self):
        currNd = self.queueArray.head
        while currNd is not None:
            yield currNd.value 
            currNd = currNd.next
    
    def __str__(self):
        return "this is a queue"
    
    def isEmpty(self):
        return self.queueArray.isEmpty()

    
    def enqueue(self, num):
        self.queueArray.insertLast(num)
        self._count += 1
            
    def dequeue(self):
        if not self.isEmpty():
            self._count -= 1
            return self.queueArray.removeFirst()
        else:
            raise IndexError('Queue is empty')
    
    def peek(self):
        if not self.isEmpty():
            return self.queueArray.peekFirst()
        else:
            raise IndexError("Queue is empty")
    def count(self):
        return self._count
            