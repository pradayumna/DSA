#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 23:52:57 2021

@author: pradyumna agrawal
"""

class DSAHashEntry():
    
    def __init__(self, *args):
        if args:    
            self.__key = args[0]
            self.__value = args[1]
            self.__state = 1 #1 means that there is an object over here
        else:
            self.__key = None
            self.__value = None
            self.__state = 0 #0 means that it is empty
    
            
    def getKey(self):
        return self.__key
    
    def getValue(self):
        return self.__value
    
    def getState(self):
        return self.__state
    
    def setKey(self, key):
        self.__key = key
        
    def setValue(self, value):
        self.__value = value
        
    def setState(self, state):
        self.__state = state
        
    def setData(self, key, data):
        self.__key = key
        self.__value = data
        self.__state = 1
            
        

