#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:48:17 2021

@author: pradyumna agrawal
"""

class DSATreeNode():

    #Constructor imports key and value
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._leftChild = None
        self._rightChild = None
        
    def __str__(self):
        return ("Key: " + str(self._key) + " Value: "+ str(self._value))
        
    # Assessor imports none exports key
    def getKey(self):
        return self._key
    
    # Assessor imports none exports value
    def getValue(self):
        return self._value
    
    # Assessor imports none exports left child
    def getLeft(self):
        return self._leftChild
    
    # Assessor imports none exports right child
    def getRight(self):
        return self._rightChild
    
    # Mutator imports new left exports none
    def setLeft(self, newLeft):
        self._leftChild = newLeft
        
    # Mutator imports new right exports none
    def setRight(self, newRight):
        self._rightChild = newRight
        
        
# Test Harness

def main():
    print("Testing node creation")
    myNode = DSATreeNode(1, "one")
    print(myNode)
if __name__ == "__main__":
    main()
     
