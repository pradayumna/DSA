#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:44:33 2021

@author: pradyumna agrawal
@student ID: 20046165
@Practical 2

highest factorial - 2958
"""

def _factorial(n):
    if n == 1 or n == 0:
        fact = 1
    else:
        fact = n * _factorial(n-1)
    return fact


def _fibonacii(n):
    if n == 0 or n == 1:
        ans = n
    else:
        ans = _fibonacii(n-1) + _fibonacii(n-2)
        
    return ans


def _gcd(a, b):
    if a > b:
        ans = _gcd(b, a)
        return ans
    if b%a == 0:
        ans = a
    else:
        ans = _gcd(b%a, a)
    return ans

def int2chr(n):
    if n <= 9:
        return chr(n + ord('0'))
    else:
        return chr(n - 10 + ord('A'))
    
def _nconvert(n, base):
    if base > 16 or base < 2:
        return "choose a base between 2 and 16"
    if n < base:
        ans = int2chr(n)
    else:
        ans = _nconvert(n//base, base) + int2chr(n%base)
    return ans
