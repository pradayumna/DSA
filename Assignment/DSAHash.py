#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:42:52 2021

@author: pradyumna agrawal
CODE ORIGINALLY CREATED FOR PRAC 7 SUBMISSION FOR COURSE DATA STRUCTURE AND ALGORITHM UNIT 
AT CURTIN UNIVERSITY
"""

from DSAHashEntry import DSAHashEntry
import numpy as np
import math

class DSAHash():
    '''
    DEFAULT CONSTRUCTOR
    @param maxSize: size of hash (dont matter much as hash can resize
    '''
    
    def __init__(self, maxSize):
        
        self.__maxSize = self.__getTableSize(maxSize) #get the closest prime number
        self.__hashArray = np.empty(self.__maxSize, dtype = DSAHashEntry) #create a hasharray
        self.__count = 0 #set counter at 0
        for i in range(self.__maxSize):
            self.__hashArray[i] = DSAHashEntry() #create hash entries
            
    def __iter__(self):
        '''
        ITERATOR
        '''
        count = 0 #start with count = 0
        while count < self.__maxSize: #go till count is less than maxsize
            if self.__hashArray[count].getKey() is not None: #check for empty Hash
                if self.__hashArray[count].getState() != 2: #check for deleted hash entry
                    yield self.__hashArray[count] 
            count += 1
    
    def __str__(self):
        '''
        Printing support
        '''
        for i in self.__hashArray:
            if i.getKey() != None:
                print(i.getKey(), i.getValue())
        return ' '
        
    def __getTableSize(self, maxSize):
        '''
        @param: maxSize -> number entered by user
        @return: maxSize -> nearest prime Number
        This function returns the nearest prime number
        '''
        
        if maxSize < 13:
            maxSize = 11
        if maxSize%2 == 0:
            maxSize = maxSize - 1
        isPrime = False
        while(not isPrime):
            maxSize = maxSize + 2
            i = 3
            isPrime = True
            rootSize = math.sqrt(maxSize)
            while(i <= rootSize and isPrime):
                if maxSize % i == 0 :
                    isPrime = False
                else:
                    i = i + 2
        return maxSize
    
    def __hashFunction(self, key):
        '''
        @param key
        @return index
        this function convers key to index of hasharray
        '''
        
        hashIndex = 0
        for i in key:
            hashIndex += ord(i)
        
        return hashIndex%self.__maxSize
    
    def __probeIndex(self, index, size):
        '''
        @param index
        @param size
        @return index
        this function takes index and size and return new index after probing
        '''
        return (index + size) % self.__maxSize
    
    def __find(self, key):
        
        '''
        @Param key
        @return index
        This function takes a key and tells the index at which the key is present in the hash array
        '''
        
        index = self.__hashFunction(key)
        found = False
        count = 0 #need to cater for the case when hash table is full and key is not in there
        while(self.__hashArray[index].getState() != 0 and count <= self.__maxSize):
            if self.__hashArray[index].getKey() == key:
                found = True
                break
            index = self.__probeIndex(index, self.__stepHash(key))
            count = count + 1
        if found and self.__hashArray[index].getState() == 1:
            return index
        else:
            return -1
        
    def __stepHash(self, key):
        '''
        @param Key
        @return size
        This is the second hashing function. It returns the size for probing
        '''
        
        hashIndex = 0
        for i in key:
            hashIndex += ord(i)
        return 11 - hashIndex%11
    
    def __newSize(self, variety):
        '''
        @param: variety -> 1 for increasing size, 0 for decreasing
        This function calculates the new size for hash array based on requirement
        '''
        
        while self.getLoadFactor() > 0.60 and variety == 1:
            self.__maxSize = self.__getTableSize(int(self.__maxSize * 1.5))
        while self.__maxSize > 13 and self.getLoadFactor() < 0.10:
            self.__maxSize = self.__getTableSize(int(self.__maxSize/2))
            
    def __reSize(self, variety):
        '''
        @param: variety -> 1 for increasing size, 0 for decreasing
        This function resizes the hasharray
        '''
        
        self.__newSize(variety)
        tempArray = self.__hashArray
        self.__count = 0
        self.__hashArray = np.empty(self.__maxSize, dtype = DSAHashEntry)
        for i in range(self.__maxSize):
            self.__hashArray[i] = DSAHashEntry()
        for i in tempArray:
            if i.getState() == 1:
                self.put(i.getKey(), i.getValue())

    
    def put(self, key, data):
        
        '''
        @param key
        @param data
        
        This function puts a key and respective data in hash table
        '''
        
        if self.hasKey(key):
            raise KeyError("key already exists")
        else:
            index = self.__hashFunction(key)
            while(self.__hashArray[index].getState() == 1):
                index = self.__probeIndex(index, self.__stepHash(key))
            self.__hashArray[index].setData(key, data)
            self.__count += 1
            if self.getLoadFactor() > 0.60:
                self.__reSize(1)
    
    
    def get(self, key):
        
        '''
        @param key
        @return DSAHashEntry
        
        This function takes a key and returns the hash entry object associated with that key
        '''
        
        index = self.__find(key)
        if index != -1:
            return self.__hashArray[index]
        else:
            raise KeyError("key not found")
            
    def updateData(self, key, data):
        
        '''
        @param key
        @param data
        
        This function updates the data at the key.
        '''
        
        index = self.__find(key)
        if index != -1:
            self.__hashArray[index].setValue(data)
        else:
            raise KeyError("key not found")
        
            
    def getData(self, key):
        
        '''
        @param key
        @return data (object)
        
        This function takes a key and returns the associated data' '
        '''
        index = self.__find(key)
        if index != -1:
            return self.__hashArray[index].getValue()
        else:
            raise KeyError("key not found")
                
    def hasKey(self, key):
        '''
        @param key
        @return bool 
        This function returns true if a key is in hash table
        '''
        
        return self.__find(key) != -1
    
    def getHashArray(self):
        '''
        @return np.array(dtype = DSAHashEntry)
        '''
        
        return self.__hashArray
    
    def deleteKey(self, key):
        
        '''
        @param key
        
        This function takes a key and deletes hash entry associated with it
        '''
        
        index = self.__find(key)
        if index != -1:
            self.__hashArray[index].setState(2)
            self.__count -= 1
            if self.getLoadFactor() < 0.10:
                self.__reSize(2)
                #print("new size is", self.__maxSize)
        else:
            raise KeyError("key not found")
    
    
    def getLoadFactor(self):
        '''
        @return load factor
        This function returns load factor
        '''
        
        return self.__count/self.__maxSize
    
    def getHashSize(self):
        '''
        @return size
        This function returns size of the hash
        '''
        
        return self.__maxSize

################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########                