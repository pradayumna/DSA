#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:21:21 2021

@author: pradyumna agrawal
CODE ORIGINALLY CREATED FOR PRAC 4 SUBMISSION FOR COURSE DATA STRUCTURE AND ALGORITHM UNIT 
AT CURTIN UNIVERSITY

"""

class DSAListNode:
    
    def __init__(self, value):
        '''
        Default constructor
        @param1: value (object)
        @param2: prev (DSAlistNode)
        @param3: next (DSAlistNode)
        '''
        self.value = value
        self.next = None
        self.prev = None
        
    
class DSALinkedList:
    
    def __init__(self):
        '''
        Default constructor
        '''
        
        self.head = self.tail = None
        self.count = 0
    
        #ITERATOR
    def __iter__(self):
        '''
        Iterator
        '''
        
        currNd = self.head #start with head as current value
        while currNd is not None: #go till None
            yield currNd.value #return and hold current value
            currNd = currNd.next #change current value
            
    def __str__(self):
        '''
        Function to print
        '''
        string = ''
        for i in self:
            string = string + str(i)
        return string
        
    def isEmpty(self):
        '''
        @return: Bool -> True if empty
        '''
        
        if self.head is None: return True; return False #return true if head is pointing to nothing
        
    def insertFirst(self, value):
        '''
        @param: value -> object that has to be inserted
        This function inserts the new node in the beginning
        '''
        newNd = DSAListNode(value)
        
        self.count = self.count + 1
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            newNd.next = self.head
            self.head.prev = newNd
            self.head = newNd
            
    def insertLast(self, value):
        '''
        @param: value -> object that has to be inserted
        This function inserts the new node in the beginning
        '''
        self.count = self.count + 1
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            self.tail.next = newNd
            newNd.prev = self.tail
            self.tail = newNd
            
    def peekFirst(self):
        '''
        @return: value -> Value of the head
        This function return the nvalue of the head. 
        '''
        if self.isEmpty(): 
            return None
        else:
            return self.head.value
        
    def peekLast(self):
        '''
        @return: value -> Value of the tail
        This function return the value of the tail. 
        '''
        if self.isEmpty(): 
            return None
        else:
            return self.tail.value
        
        
    def removeFirst(self):
        '''
        @return: value -> Value of the head
        This function removes and returns the value of the head. 
        '''
        
        if not self.isEmpty():
            nodeValue = self.head.value
            self.head = self.head.next
            if not self.head is None:
                self.head.prev = None
            else:
                self.tail = None
            self.count = self.count - 1
            return nodeValue
        
    def removeLast(self):
        '''
        @return: value -> Value of the tail
        This function removes and returns the value of the tail. 
        '''
        
        if not self.isEmpty():
            nodeValue = self.tail.value
            self.tail = self.tail.prev
            if not self.tail is None:
                self.tail.next = None
            else:
                self.head = None
            self.count = self.count - 1
            return nodeValue
    
    def deleteNode(self, node):
        '''
        @param node -> DSAListNode to be deleted.
        @return: value -> Value of the tail
        This function removes and returns the value of the node in parameter. 
        '''
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == node):
                self.head = temp.next
                if(self.head):
                    self.head.prev = None
                temp = None
                self.count = self.count - 1
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.value == node:
                self.count = self.count - 1
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                break
            temp = temp.next
            
    def getCount(self):
        '''
        return: int -> number of nodes in the list
        '''
        return self.count
 
################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########