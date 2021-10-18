#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 10:22:11 2021

@author: pradyumna agrawal 
code for queues with linked list
CODE ORIGINALLY CREATED FOR PRAC 4 SUBMISSION FOR COURSE DATA STRUCTURE AND ALGORITHM UNIT 
AT CURTIN UNIVERSITY
"""

from linkedKList import DSALinkedList #import DSALinkedList


class queueEntry():
    
    #Queue entries are like hash entries. They are used in implementing
    #priority queue. They have a value that defines priority and they can save 
    #an object
    
    def __init__(self):
        '''
        Defalur constructor
        '''
        
        self.__value = None
        self.__path = None
        
    def addValue(self, value):
        '''
        @param1 : value (integer) -> priority
        '''
        self.__value = value #set priority
        
    def addPath(self, path):
        '''
        @param1 : path -> any object 
        '''
        self.__path = path #set object
        
    def getValue(self):
        '''
        getter function
        @return: value -> priority(int)
        '''
        return self.__value
    
    def getPath(self):
        '''
        getter function
        @return: path -> any path
        '''
        return self.__path

class queue():
    
    #this is linked list based implementation of queue (FIFO)
    def __init__(self):
        '''
        default constructor
        '''
        self.queueArray = DSALinkedList() #this implementation uses DSALinkedList
        
    def __iter__(self):
        '''
        Iterator function
        '''
        currNd = self.queueArray.head #start with queue head
        while currNd is not None: #go till end
            yield currNd.value #return the current value
            currNd = currNd.next #move to next node
    
    def __str__(self):
        '''
        printing function
        '''
        # i dont think this function is useful. I created this code in week 5 and now 
        #I dont want to mess it us by taking the risk of deleting a function
        #'dont touch if if it works' - A great coder somewhere
        return "this is a queue"
    
    def isEmpty(self):
        '''
        @return: Bool -> Yes if empty, no otherwise
        '''
        return self.queueArray.isEmpty()

    
    def enqueue(self, num):
        '''
        @param1: num -> number that you want to add to queue
        This function adds any new thing in the last of list
        '''
        self.queueArray.insertLast(num)
            
    def dequeue(self):
        '''
        @return -> first number in the list
        This function returns first number in the queue
        It also removes the number from the list
        '''
        if not self.isEmpty():
            return self.queueArray.removeFirst()
        else:
            raise IndexError('Queue is empty')
    
    def peek(self):
        '''
        @return -> first number in the list
        This function returns first number in the queue
        without removing it from list
        '''
        if not self.isEmpty():
            return self.queueArray.peekFirst()
        else:
            raise IndexError("Queue is empty")
            
class priorityQueue(queue):
    #priority queue inherits from queue
    #it basically has a different enqueing and dequeing mechanism
    #rest is same. 
    
    def enqueue(self, value, path):
        '''
        @param1: value(int) -> it define priority
        @param2: path -> any object
        '''
        
        qobj = queueEntry() #create a queue entry object
        qobj.addValue(value) #add value to it
        qobj.addPath(path) #add path to it
        self.queueArray.insertLast(qobj) #add queue entry to queue
        
    def dequeue(self):
        '''
        @return -> first number in the list
        This function returns first number in the queue
        It also removes the number from the list
        '''
        maximum = self.queueArray.head.value #start with head to be maximum
        for i in self.queueArray: #check through entire array 
            if i.getValue() > maximum.getValue(): #compare priority
                maximum = i #update priority element
        self.queueArray.deleteNode(maximum) #delete Node 
        return maximum #return priority object
        
            
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
################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########