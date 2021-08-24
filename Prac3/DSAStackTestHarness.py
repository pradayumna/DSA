#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:03:34 2021

@author: pradyumna agrawal
"""

from DSAStack import stack

def main():
    
    testStack = stack()
    
    print('initially the size of stack is', testStack.count())
    
    print('Therefore, it is ', testStack.isEmpty(), ' that stack is Empty')
    
    print('\n--------------\n')
    print('now we will push elements in the stack')
    
    for i in range(testStack.maxSize):
        print('putting ', i, ' in the stack')
        try:
            testStack.push(i)
        except IndexError as ind:
            print(ind)
            
    
    print('\n--------------\n')
    print('now we will pop elements in the stack and also check the top element')

    for i in range(testStack.count()):
        try:
            print('currently, ', testStack.top(), ' is on the top')
        except IndexError as err:
            print(err)
        print('trying to pop an element')
        try:
            print('so we popped ', testStack.pop())
        except IndexError as err:
            print(err)
if __name__ == "__main__":
    main()