#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 21:21:21 2021

@author: pradyumna agrawl

"""

class DSAListNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
    
class DSALinkedList:
    
    def __init__(self):
        self.head = self.tail = None
    
        #ITERATOR
    def __iter__(self):
        currNd = self.head
        while currNd is not None:
            yield currNd.value 
            currNd = currNd.next
            
    def __str__(self):
        string = ''
        for i in self:
            string = string + str(i)
        return string
        
    def isEmpty(self):
        if self.head is None: return True; return False #return true if head is pointing to nothing
        
    def insertFirst(self, value):
        newNd = DSAListNode(value)
        
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            newNd.next = self.head
            self.head.prev = newNd
            self.head = newNd
            
    def insertLast(self, value):
        
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            self.tail.next = newNd
            newNd.prev = self.tail
            self.tail = newNd
            
    def peekFirst(self):
        if self.isEmpty(): 
            return None
        else:
            return self.head.value
        
    def peekLast(self):
        if self.isEmpty(): 
            return None
        else:
            return self.tail.value
        
        
    def removeFirst(self):
        
        if not self.isEmpty():
            nodeValue = self.head.value
            self.head = self.head.next
            if not self.head is None:
                self.head.prev = None
            else:
                self.tail = None
            return nodeValue
        
    def removeLast(self):
        
        if not self.isEmpty():
            nodeValue = self.tail.value
            self.tail = self.tail.prev
            if not self.tail is None:
                self.tail.next = None
            else:
                self.head = None
            return nodeValue
    
    def deleteNode(self, node):
         
        # Store head node
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == node):
                self.head = temp.next
                self.head.prev = None
                temp = None
                return
 
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.value == node:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                break
            temp = temp.next
 

        
        
        
