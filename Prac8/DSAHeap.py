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
            
    def __str__(self):
        for i in self.__heapArray:
            if i.getPriority() != None:
                print(i.getPriority(), i.getValue())
        return 'heap printed'
    
    def __iter__(self):
        currIndex = 0
        while currIndex < self.__count:
            yield self.__heapArray[currIndex]
            currIndex += 1
            
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
        
        
    def add(self, *args):
        if self.__count == self.__size:
            raise IndexError("Array is full")
        else:
            index = self.__count
            self.__count += 1
            self.__heapArray[index].setPriority(args[0])
            if len(args) > 1:
                self.__heapArray[index].setValue(args[1])
            self.__trickleUp(index)
            for i in self.__heapArray:
                print(i.getPriority(), end = ' ')
            print()
            print()
            print()
            
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
            self.__heapArray[self.__count] = DSAHeapEntry()
            self.__trickleDown(0)
            return returnHE
                
        
    def heapSort(self, *args):
        if len(args) == 1:
            self.__heapArray = args[0]
            self.__size = len(args[0])  #replacing its heap with the array in argument
            self.__count = self.__size
        if self.__count == 0:
            raise IndexError('You cant sort an empty Heap')
        returnList = DSAHeap(self.__count)
        length = self.__count
        for i in range(self.__count):
            data = self.remove()
            returnList.getHeapArray()[length - i - 1] = DSAHeapEntry(data.getPriority(), data.getValue())
            # print(data.getPriority())
        return returnList
    
    def returnCount(self):
        return self.__count
    
    def getHeapArray(self):
        return self.__heapArray
        
    
class DSAHeapIO():
    
    def __init__(self):
        self.heap = DSAHeap(20)
        self.length = 0
        
    def loadCSV(self, filename):
        link = open(filename, 'r')
        data = link.readlines()
        self.length = len(data)
        self.heap = DSAHeap(self.length)
        for i in data:
            self.heap.add(i.split(',')[0], i.split(',')[1].strip())
            
    def writeSortedCSV(self, filename):
        
        data = self.heap.heapSort()
        file = open(filename, 'w')
        for i in range(self.length):
            file.write(str(data.getHeapArray()[i].getPriority()) + ',' + str(data.getHeapArray()[i].getValue()) + '\n')


A = DSAHeap(15)
for i in [50, 30, 100, 40, 60, 50, 80, 70, 60, 90]:
    A.add(i)