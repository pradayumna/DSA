#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 09:38:11 2021

@author: pradyumna agrawal
"""

from DSABinarySearchTree import DSABinarySearchTree


#Test Harness        
def main():       
    file = open("RandomNames7000.csv")
    
    #code for insertion in tree1
    print("creating BST from the csv file")
    a = file.readlines()
    lst = [[int(i.split(',')[0]), i.split(',')[1]] for i in a]
    t1 = DSABinarySearchTree()
    for i in lst:
        t1.insert(i[0], i[1])
    input("tree created. press enter to continue")
    
    #code for insertion in tree2
    print("creating a BST with height = 2")
    t2 = DSABinarySearchTree()
    t2.insert(50, 1)
    t2.insert(30, 2)
    t2.insert(70, 3)
    t2.insert(10, 4)
    t2.insert(40, 5)
    t2.insert(60, 6)
    t2.insert(80, 7)  
    input("tree created. press enter to continue")
    
    #checking min key, max key, balance and height of both trees
    print("\nprinting minimum, maximum, and height for both trees")
    print("\nminimum key in first tree is " + str(t1.minKey()))
    print("\nmaximum key in first tree is " + str(t1.maxKey()))
    print("\nheight of first tree is " + str(t1.height()))
    print("\nTree has a balance percentage of " + str(t1.balance()))
    
    print("\nminimu key in second tree is " + str(t2.minKey()))
    print("\nmaximum key in second tree is " + str(t2.maxKey()))
    print("\nheight of second tree is " + str(t2.height()))
    print("\nTree has a balance percentage of " + str(t2.balance()))
    input("press enter to continue")
    
    #deletion Code
    t1.delete(14176744) #deleting a random node
    t2.delete(50) #deleting root
    t2.delete(10)
    input("nodes deleted. press enter to continue")
    #display Code
    
    #t1.display('1')
    print("inorder traversal" + "-"*10)
    t2.display('1')
    print("preorder traversal" + "-"*10)
    t2.display('2')
    print("postorder traversal" + "-"*10)
    t2.display('1')
    
    #finding code

    print(t2.find(50)) #we deleted this one already
    print(t2.find(30)) 
    print(t1.find(t1.minKey()))
    

if __name__ == "__main__":
    main()