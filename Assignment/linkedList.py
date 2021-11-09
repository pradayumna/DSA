#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:32:06 2021

@author: charmi
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

    # def removeNode(self, node):
    #     if not self.isEmpty():
    #         if self.head.value == node:
    #             self.head = self.head.next
    #         else:
    #             pred = self.head.next
    #             prev = self.head
    #             while pred != None:
    #                 if pred.value == node:
    #                     prev = pred.next
    #                     if pred.next != None:
    #                         pred.next.prev = prev
    #                     break
    #                 prev = pred
    #                 pred = pred.next
                    
    def removeNode(self, node):
       
        temp = self.head
 
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.value == node):
                self.head = temp.next
                if(self.head):
                    self.head.prev = None
                temp = None
                return
        while(temp is not None):
            if temp.value == node:
                temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                break
            temp = temp.next
                    
                
    #Bubble sort logic, referenced from the lecture slide
    def sortList(self):
        # Node current will point to head
        current = self.head
        index = None

        if (self.head == None):
            print('head none')
            return
        else:
            while (current != None):
                # Node index will point to node next to current
                index = current.next
                while index != None:
                    # If current node's data is greater than index's node data, swap the data between them
                    if current.value > index.value:
                        temp = current.value
                        current.value = index.value
                        index.value = temp
                    index = index.next
                current = current.next

                    
                    
    



        
