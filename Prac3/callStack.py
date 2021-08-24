#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 09:30:36 2021

@author: prad
"""

from DSAStack import stack

callStack = stack()


def _fibonacii(n, callStack):
    arr = "fibonacii(" + str(n) + ")"
    callStack.push(arr)
    print("pushed ", arr, " in the stack")
    if n == 0 or n == 1:
        print("popped ", callStack.pop(), " from the array")
        ans = n
    else:
        ans = _fibonacii(n-1, callStack) + _fibonacii(n-2, callStack)
        
    return ans



def qFunc(a, b, callStack):
    arr = "qFUnc()"
    print("pushed ", arr, " in the stack")
    callStack.push(arr)
    print("now popping ", callStack.pop(), " from the stack")

    return int(a/b)

def modFunc(a, b, callStack):
    arr = "modFunc()"
    print("pushed ", arr, " in the stack")
    callStack.push(arr)
    q = qFunc(a, b, callStack)
    print("now popping ", callStack.pop(), " from the stack")
    return a - q*b

def main():
    _fibonacii(5, callStack)
    modFunc(10, 6, callStack)
    
if __name__ == "__main__":
    main()