#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 10:11:18 2021

@author: pradyumna agrawal
"""
import pickle
from linkedKList import DSALinkedList

LL = DSALinkedList()
for i in range(10):
    LL.insertFirst(i)
    
while(True):
    option = input("what you want to do?\n1) Load Object I/O Stream\n2) print linked list \n3) Dump Object I/O Stream\n4) exit")
    
    
    
    if option == "1":
        try:
            with open('placesDAT', "rb") as dataFile:
                PP = pickle.load(dataFile)
        except:
            print("file does not exist")
                    
    if option == "2":
        try:            
            for i in PP:
                print(i)
        except:
            ("yet to load object stream")
            
    if option == "3":
        try:
            LL.insertFirst(12)
            with open('placesDAT', "wb") as f:
                pickle.dump(LL, f)
        except:
            "nothing to dump"
        
    if option == "4":
        break

                
                