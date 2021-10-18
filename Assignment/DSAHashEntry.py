#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:52:57 2021

@author: pradyumna agrawal

CODE ORIGINALLY CREATED FOR PRAC 7 SUBMISSION FOR COURSE DATA STRUCTURE AND ALGORITHM UNIT 
AT CURTIN UNIVERSITY
"""

class DSAHashEntry():
    #Hash entries are building blocks of hash table. 
    #they store a key, value and, state
    
    def __init__(self, *args):
        '''
        DEFAULT CONSTRUCTOR
        Optional parameter -> it can either be called with a key and value or without them
        '''
        if args:    
            self.__key = args[0]
            self.__value = args[1]
            self.__state = 1 #1 means that there is an object over here
        else:
            self.__key = None
            self.__value = None
            self.__state = 0 #0 means that it is empty
    
            
    def getKey(self):
        '''
        @return key
        '''
        return self.__key
    
    def getValue(self):
        '''
        @return value
        '''
        return self.__value
    
    def getState(self):
        '''
        @return state
        '''
        return self.__state
    
    def setKey(self, key):
        '''
        @param key
        This function sets the key
        '''
        self.__key = key
        
    def setValue(self, value):
        '''
        @param value
        This function sets the value
        '''
        self.__value = value
        
    def setState(self, state):
        '''
        @param state
        This function sets the state
        '''
        self.__state = state
        
    def setData(self, key, data):
        '''
        @param key
        @param data
        This function sets key and data together.
        idk, I found it handy. 
        '''
        self.__key = key
        self.__value = data
        self.__state = 1
            
################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########