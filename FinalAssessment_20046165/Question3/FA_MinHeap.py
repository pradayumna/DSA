#
# DSA Final Assessment Question 3 - Q3MaxHeap.py
#
# Name : Pradumna Arawal
# ID   : 20046165
#
# 
import numpy as np
from PracExamException import PracExamException #importing exception class

class FA_MinHeap():
    # Inner class HeapEntry
    class HeapEntry(    ):
        def __init__(self, priority, value):
            self.priority = priority
            self.value = value
    # End Inner class
    MAXSIZE = 11 #changed it as per the data. 
    
    def __init__(self):
        self.heap = np.zeros(self.MAXSIZE, dtype=object)
        self.count = 0

    def add(self, priority, value):
        if self.count == self.MAXSIZE: #checking if the heap array is full
            raise PracExamException('Heap is already full') #raising exception
        else:
            self.heap[self.count] = self.HeapEntry(priority, value)
            self.count = self.count+1
            self.trickleUp(self.count-1)

    def remove(self): 
        if self.count == 0: #checking if heap is empty
            raise PracExamException('Heap is Empty') #raising exception
        else:
            entry = self.heap[0]
            retValue = entry.value
            self.heap[0] = self.heap[self.count-1]
            self.heap[self.count-1] = None
            self.count = self.count - 1
            self.trickleDown(0)
            return retValue

    def trickleDown(self, index):
        leftIdx = index * 2 + 1
        rightIdx = leftIdx + 1

        if (leftIdx < self.count):
            smallIdx = leftIdx  #largeIdx changed to smallIdx (not a logical change.
            if (rightIdx < self.count):
                if (self.heap[leftIdx].priority > self.heap[rightIdx].priority): #comparison sign changed
                    smallIdx = rightIdx
            if (self.heap[smallIdx].priority < self.heap[index].priority): #comparison sign changed
                temp = self.heap[smallIdx]
                self.heap[smallIdx] = self.heap[index]
                self.heap[index] = temp
                self.trickleDown(smallIdx)

    def trickleUp(self, index):
        parentIndex = (index-1)//2

        if (index > 0 ):
            if (self.heap[index].priority < self.heap[parentIndex].priority): #comparison sign reveresed  
                temp = self.heap[parentIndex]
                self.heap[parentIndex] = self.heap[index]
                self.heap[index] = temp
                self.trickleUp(parentIndex)
    def printHeap(self):
        print('\n=======\n')
        for i in range(self.count):
            print("value-"+str(self.heap[i].value)+" Priority: ", str(self.heap[i].priority))
        print('\n=======\n')    
