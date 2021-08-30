#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:34:20 2021

@author: pradyumna agrawal
"""

from DSAQueue import queue

def main():
    q = queue()
       
    print('Therefore, it is ', q.isEmpty(), ' that queue is Empty')
        
    print('\n--------------\n')
    print('now we will push elements in the queue')
    print('\n--------------\n')    
    for i in range(10):
        print('putting ', i, ' in the queue')
        try:
            q.enqueue(i)
        except IndexError as ind:
            print(ind)
    print('\n--------------\n')
    print('now trying iterators')
    print('\n--------------\n')          
    for i in q:
        print(i)    
    
    print('\n--------------\n')
    print('now we will dequeue elements in the queue and also look at the top element')
    print('\n--------------\n')
    while not q.isEmpty():
        try:
            print('currently, ', q.peek(), ' is the first element')
        except IndexError as err:
            print(err)
        print('trying to dequeue an element')
        try:
            print('so we dequeued ', q.dequeue())
        except IndexError as err:
            print(err)
if __name__ == "__main__":
    main()