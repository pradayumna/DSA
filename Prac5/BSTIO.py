#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:00:04 2021

@author: pradyumna agrawal
"""
import pickle
import os.path
from DSABinarySearchTree import DSABinarySearchTree
Tree = DSABinarySearchTree()

while(True):
    choice = input("select one of the follwing options\n1. Load a CSV file\n2. Load a serialised file\n3. display the tree\n4. write a csv file\n5. write a serialised file\n6. quit")
    
    if choice == '6':
        print("-"*6 + '\n' + "thanks for running the program")
        break
    elif choice == '1':
        filename = input("\nPlease enter the name of the file you want to load")
        if os.path.isfile(filename):
            try:
                file = open(filename)
                a = file.readlines()
                lst = [[int(i.split(',')[0]), i.split(',')[1]] for i in a]
                for i in lst:
                    Tree.insert(i[0], i[1])
            except:
                print("file is not in the required format")
        else:
            print("file does not exists")
            
    elif choice == '2':
        filename = input("\nPlease enter the name of the file you want to load")
        if os.path.isfile(filename):
            try:
                with open(filename, "rb") as dataFile:
                    Tree = pickle.load(dataFile)
            except:
                print("file does not exist")
        else:
            print("file does not exists")
            
    elif choice == '3':
        order = input("what type of traversal you want? 1. In-order, 2. Pre-order, 3. Post-order")
        Tree.display(order)
        
    elif choice == '4':
        order = input("what type of traversal you want? 1. In-order, 2. Pre-order, 3. Post-order")
        filename = input("\nwhat filename you want to keep?")
        Tree.writeCSV(filename, order)
        
    elif choice == '5':
        filename = input("\nwhat filename you want to keep?")
        Tree.serialize(filename)

