#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 13:42:52 2021

@author: pradyumna agrawal
"""

from DSAHashEntry import DSAHashEntry
import numpy as np
import math
import pickle

class DSAHash():
    
    def __init__(self, maxSize):
        
        self.__maxSize = self.__getTableSize(maxSize)
        self.__hashArray = np.empty(self.__maxSize, dtype = DSAHashEntry)
        self.__count = 0
        for i in range(self.__maxSize):
            self.__hashArray[i] = DSAHashEntry()
        
    def __getTableSize(self, maxSize):
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
        hashIndex = 0
        for i in key:
            hashIndex += ord(i)
        
        return hashIndex%self.__maxSize
    
    def __probeIndex(self, index, size):
        return (index + size) % self.__maxSize
    
    def __find(self, key):
        
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
        hashIndex = 0
        for i in key:
            hashIndex += ord(i)
        return 11 - hashIndex%11
    
    def __newSize(self, variety):
        while self.getLoadFactor() > 0.60 and variety == 1:
            self.__maxSize = self.__getTableSize(int(self.__maxSize * 1.5))
        while self.__maxSize > 13 and self.getLoadFactor() < 0.10:
            self.__maxSize = self.__getTableSize(int(self.__maxSize/2))
            
    def __reSize(self, variety):
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
                print("new size is", self.__maxSize)
    
    
    def get(self, key):
        index = self.__find(key)
        if index != -1:
            return self.__hashArray[index]
        else:
            raise KeyError("key not found")
                
    def hasKey(self, key):
        return self.__find(key) != -1
    
    def getHashArray(self): #for file IO
        return self.__hashArray
    
    def deleteKey(self, key):
        index = self.__find(key)
        if index != -1:
            self.__hashArray[index].setState(2)
            self.__count -= 1
            if self.getLoadFactor() < 0.10:
                self.__reSize(2)
                print("new size is", self.__maxSize)
        else:
            raise KeyError("key not found")
    
    
    def getLoadFactor(self):
        return self.__count/self.__maxSize
    
    def getHashSize(self):
        return self.__maxSize


class hashIO():
    
    def __init__(self):
        self.__hashTable = None
        
    def readCSV(self, filename):
        file = open(filename, 'r')
        data = file.readlines()
        self.__hashTable = DSAHash(len(data))
        for i in data:
            try:
                self.__hashTable.put(i.split(',')[0], i.split(',')[1].strip())
            except KeyError as e:
                print(e, i.split(',')[0])
        return self.__hashTable
    
    def writeCSV(self, hashTable, filename):
        hashArray = hashTable.getHashArray()
        file = open(filename, 'w')
        for i in hashArray:
            if i.getState() == 1:
                file.write(str(i.getKey()) + ',' + str(i.getValue()) + '\n')
    
    def loadSerialisedFile(self, filename):
        try:
            with open(filename, "rb") as dataFile:
                self.__hashTable = pickle.load(dataFile)
        except:
            print("file does not exist")
        return self.__hashTable
    
    def saveSerialisedFile(self, hashTable, filename):
        with open(filename, "wb") as f:
                pickle.dump(hashTable, f)
        
                