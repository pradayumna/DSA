#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:34:20 2021

@author: pradyumna agrawal
"""

from DSAQueue import sequenceQueue, circularQueue


sQ = sequenceQueue()
cQ = circularQueue()

qList = [sQ, cQ]



for q in qList:
    
    print('initially the size of queue is', q.getCount())
    
    print('Therefore, it is ', q.isEmpty(), ' that queue is Empty')
    
    print('\n--------------\n')
    print('now we will push elements in the queue')
    
    for i in range(q.capacity):
        print('putting ', i, ' in the queue')
        try:
            q.enqueue(i)
        except IndexError as ind:
            print(ind)
            
    
    print('\n--------------\n')
    print('now we will dequeue elements in the queue and also look at the top element')

    for i in range(q.getCount()):
        try:
            print('currently, ', q.peek(), ' is the first element')
        except IndexError as err:
            print(err)
        print('trying to dequeue an element')
        try:
            print('so we dequeued ', q.dequeue())
        except IndexError as err:
            print(err)