#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:59:14 2021

@author: pradyumna agrawal
"""

class DSAHeapEntry():
    
    def __init__(self, *args):
        if len(args) > 0:
            self.__priority = args[0]
        else:
            self.__priority = None
        if len(args) > 1:
            self.__value = args[1]
        else:
            self.__value = None
            
    def setPriority(self, priority):
        self.__priority = priority 
        
    def setValue(self, value):
        self.__value = value
        
    def getPriority(self):
        return self.__priority
    
    def getValue(self):
        return self.__value
        

