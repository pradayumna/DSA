#
# DSA Final Assessment Question 3 - Q3MaxHeap.py
#
# Name : 
# ID   :
#
# 
import numpy as np

class Q3MaxHeap():
    # Inner class HeapEntry
    class HeapEntry(    ):
        def __init__(self, priority, value):
            self.priority = priority
            self.value = value
    # End Inner class
    MAXSIZE = 10
    
    def __init__(self):
        self.heap = np.zeros(self.MAXSIZE, dtype=object)
        self.count = 0

    def add(self, priority, value):
        self.heap[self.count] = self.HeapEntry(priority, value)
        self.count = self.count+1
        self.trickleUp(self.count-1)

    def remove(self): 
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
            largeIdx = leftIdx  
            if (rightIdx < self.count):
                if (self.heap[leftIdx].priority < self.heap[rightIdx].priority):
                    largeIdx = rightIdx
            if (self.heap[largeIdx].priority > self.heap[index].priority):
                temp = self.heap[largeIdx]
                self.heap[largeIdx] = self.heap[index]
                self.heap[index] = temp
                self.trickleDown(largeIdx)

    def trickleUp(self, index):
        parentIndex = (index-1)//2

        if (index > 0 ):
            if (self.heap[index].priority > self.heap[parentIndex].priority):   
                temp = self.heap[parentIndex]
                self.heap[parentIndex] = self.heap[index]
                self.heap[index] = temp
                self.trickleUp(parentIndex)
