#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:22:11 2021

@author: prad
"""

import numpy as np


class queue():
    
    capacity = 100
    
    def __init__(self):
        self.queueArray = np.empty(self.capacity, dtype = object)
        self.count = 0
        print(self.capacity)
        
    def getCount(self):
        return self.count

class sequenceQueue(queue):
    
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity
    
    def enqueue(self, num):
        if not self.isFull():
            self.queueArray[self.count] = num
            self.count = self.count + 1
        else:
            raise IndexError('Queue is full')
            
    def dequeue(self):
        if not self.isEmpty():
            temp = self.queueArray[0]
            self.count = self.count - 1
            for i in range(self.count):
                self.queueArray[i] = self.queueArray[i+1]
            return temp
        else:
            raise IndexError('Queue is empty')
    def peek(self):
        if not self.isEmpty():
            return self.queueArray[0]
        else:
            raise IndexError("Queue is empty")
            
            
class circularQueue(queue):
    
    def __init__(self):
        super(circularQueue, self).__init__()
        self.head = -1
        self.tail = -1
    
    
    def isEmpty(self):
        return (self.head == -1)
    
    def isFull(self):
        return ((self.tail + 1) % self.capacity == self.head)
    
    def enqueue(self, num):
        if self.isFull():
            raise IndexError("the queue is already full")
        elif self.head == -1:
            self.head = self.tail = 0
            self.queueArray[self.tail] = num
            self.count +=1
        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queueArray[self.tail] = num
            self.count +=1
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("the queue is empty")
        elif(self.tail == self.head):
            temp=self.queue[self.head]
            self.head = -1
            self.tail = -1
            self.count -=1
            return temp 
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.size
            self.count -=1
            return temp
    def peek(self):
        if self.isEmpty():
            raise IndexError("the queue is empty")
        else:
            return self.queueArray[self.tail]
