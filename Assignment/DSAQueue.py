#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:22:11 2021

@author: pradyumna agrawal 
code for queues with linked list
"""

from linkedKList import DSALinkedList
#change name to list

class queueEntry():
    
    def __init__(self):
        self.__value = None
        self.__path = None
        
    def addValue(self, value):
        self.__value = value
        
    def addPath(self, path):
        self.__path = path
        
    def getValue(self):
        return self.__value
    
    def getPath(self):
        return self.__path

class queue():
    
    
    def __init__(self):
        self.queueArray = DSALinkedList()
        
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
            
class priorityQueue(queue):
    
    def enqueue(self, value, path):
        qobj = queueEntry()
        qobj.addValue(value)
        qobj.addPath(path)
        self.queueArray.insertLast(qobj)
        
    def dequeue(self):
        maximum = self.queueArray.head.value
        for i in self.queueArray:
            if i.getValue() > maximum.getValue():
                maximum = i
        self.queueArray.deleteNode(maximum)
        return maximum
        
            
A = priorityQueue()
A.enqueue(10, "A")
A.enqueue(20, 'H')
A.enqueue(5, 'M')
A.enqueue(50, 'B')
A.enqueue(15, 'E')

B = A.dequeue()
print(B.getValue(), B.getPath())
B = A.dequeue()
print(B.getValue(), B.getPath())
B = A.dequeue()
print(B.getValue(), B.getPath()) 
B = A.dequeue()
print(B.getValue(), B.getPath()) 
B = A.dequeue()
print(B.getValue(), B.getPath())             