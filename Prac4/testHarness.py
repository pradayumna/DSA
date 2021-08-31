#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 11:05:43 2021

@author: pradyumna agrawal
"""

from linkedKList import DSALinkedList 

def main():
#these are just tests to check if the list is working properly. Will add them seperately in a testHarness
    A = DSALinkedList()
    A.insertFirst(5)
    A.insertFirst(4)
    print(A.peekFirst()) #should print 4
    print(A.peekLast()) #should print 5
    A.insertLast(6)
    print(A.peekLast()) # should print 6
    A.insertFirst(3)
    print(A.peekFirst()) #should print 3
    print(A.peekLast()) #should print 6
    print(A.removeFirst()) #should print 3
    print(A.peekFirst()) #should print 4
    print(A.removeLast()) #should print 6
    print(A.peekLast()) #should print 5
    A.insertFirst(8)
    
    #ITERATOR
    for i in A:
        print(i)
    
    #Now checking extreme cases
    B = DSALinkedList()
    B.insertFirst(4)
    print(B.removeFirst()) #should print 4
    print(B.peekLast())
    print(B.peekFirst()) #should print none
    B.insertLast(2) #should print none
    print(B.removeLast()) #should print 2
    
if __name__ == "__main__":
    main()

