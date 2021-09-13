#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 17:10:42 2021

@author: pradyumna agrawal
"""
from DSAHeapEntry import DSAHeapEntry
import numpy as np

class DSAHeap():
    
    def __init__(self, size):
        self.__heapArray = np.empty(size, dtype = DSAHeapEntry)
        self.__size = size
        self.__count = 0
        for i in range(size):
            self.__heapArray[i] = DSAHeapEntry()
            
    def __leftChildIndex(self, index):
        return (index * 2) + 1
    
    def __rightChildIndex(self, index):
        return (index * 2) + 2
    
    def __parentIndex(self, index):
        return int((index - 1)/2)
    
    
    def __trickleUp(self, index):
        currIndex = index
        parentIndex = self.__parentIndex(index)
        if currIndex > 0:
            if self.__heapArray[currIndex].getPriority() > self.__heapArray[parentIndex].getPriority():
                self.__heapArray[currIndex], self.__heapArray[parentIndex] = self.__heapArray[parentIndex], self.__heapArray[currIndex]
                index = self.__parentIndex(index)
                self.__trickleUp(index)
        
    def __trickleDown(self, index):
        lChild = self.__leftChildIndex(index)
        rChild = self.__rightChildIndex(index)
        
        if lChild < self.__count:
            largeIndex = lChild
            if rChild < self.__count:
                if self.__heapArray[lChild].getPriority() < self.__heapArray[rChild].getPriority():
                    largeIndex = rChild
            if self.__heapArray[largeIndex].getPriority() > self.__heapArray[index].getPriority():
                self.__heapArray[largeIndex], self.__heapArray[index] = self.__heapArray[index], self.__heapArray[largeIndex]
                self.__trickleDown(largeIndex)
        
        
    def add(self, priority, value):
        if self.__count == self.__size:
            raise IndexError("Array is full")
        else:
            index = self.__count
            self.__count += 1
            self.__heapArray[index].setPriority(priority)
            self.__heapArray[index].setValue(value)
            self.__trickleUp(index)
            
    def remove(self):
        if self.__count == 0:
            raise IndexError("Heap is Empty")
        else:
            returnHE = self.__heapArray[0]
            self.__count -= 1
            if self.__count == 0:
                self.__heapArray[0] = DSAHeapEntry()
                return returnHE
            self.__heapArray[0] = self.__heapArray[self.__count]
            self.__trickleDown(0)
            return returnHE
                
        
    def printHeap(self):
        for i in range(self.__count):
            print(self.__heapArray[i].getPriority())
        
    def heapSort(self, *args):
        if len(args) == 1:
            self.heapArray = args[0]
            self.__size = len(args[0])  #replacing its heap with the array in argument
            self.__count = self.__size
        returnList = []
        for i in range(self.__count):
            data = self.remove()
            returnList.append([data.getPriority(), data.getValue()])
        return returnList
        
    
class DSAHeapIO():
    
    def __init__(self):
        self.heap = DSAHeap(20)
        
    def loadCSV(self, filename):
        link = open(filename, 'r')
        data = link.readlines()
        self.heap = DSAHeap(len(data))
        for i in data:
            self.heap.add(i.split(',')[0], i.split(',')[1].strip())
            
    def writeSortedCSV(self, filename, order):
        
        data = self.heap.heapSort()
        file = open(filename, 'w')
        if order == 'a':
            data = data[::-1]
        for i in data:
            file.write(str(i[0]) + ',' + str(i[1]) + '\n')
        
A = DSAHeapIO()
A.loadCSV('RandomNames7000.csv')
A.writeSortedCSV('sorted.csv', 'a')        

