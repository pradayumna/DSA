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
        
    
class DSALinkedList:
    
    def __init__(self):
        self.head = self.tail = None
        
    def isEmpty(self):
        if self.head is None: return True; return False #return true if head is pointing to nothing
        
    def insertFirst(self, value):
        newNd = DSAListNode(value)
        
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            newNd.next = self.head
            self.head = newNd
            
    def insertLast(self, value):
        
        newNd = DSAListNode(value)
        if self.isEmpty():
            self.head = self.tail = newNd
        else:
            self.tail.next = newNd
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
            return nodeValue
        
    def removeLast(self):
        
        if self.isEmpty():
            return None
            
        elif self.head.next is None:
            nodeValue = self.head.value
            self.head = None
            self.tail = None
            return nodeValue
        
        else:
            
            prevNd = None
            currNd = self.head
            while not currNd.next is None:
                prevNd = currNd
                currNd = currNd.next
            prevNd.next = None
            self.tail = prevNd
            return currNd.value

#these are just tests to check if the list is working properly. Will add them seperately in a testHarness
A = DSALinkedList()
A.insertFirst(5)
A.insertFirst(4)
print(A.peekFirst()) #should print 4
print(A.peekLast()) #should print 5
A.insertLast(6)
print(A.peekLast()) # should print 6
A.insertFirst(3)
print(A.peekFirst()) #should print 3
print(A.peekLast()) #should print 6
print(A.removeFirst()) #should print 3
print(A.peekFirst()) #should print 4
print(A.removeLast()) #should print 6
print(A.peekLast()) #should print 5

#Now checking extreme cases
B = DSALinkedList()
B.removeFirst()
B.removeLast()
print(B.peekFirst())
print(B.peekLast())
print(B.isEmpty())
B.insertFirst(2)
print(B.removeLast())
