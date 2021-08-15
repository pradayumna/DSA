#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 15:44:33 2021

@author: pradyumna agrawal
@student ID: 20046165
@Practical 2

highest factorial - 2958
"""

def factorial(n):
    if n == 1:
        fact = n
    else:
        fact = n * factorial(n-1)
    return fact

#print(factorial(2958))

def fibonacii(n):
    if n == 0 or n == 1:
        ans = n
    else:
        ans = fibonacii(n-1) + fibonacii(n-2)
        
    return ans
    
#print(fibonacii(40))

def gcd(a, b):
    if a > b:
        ans = gcd(b, a)
        return ans
    if b%a == 0:
        ans = a
    else:
        ans = gcd(b%a, b)
    return ans

#print(gcd(112, 120))

def nconvert(n, base):
    if base > 16 or base < 2:
        return "choose a base between 2 and 16"
    if n < base:
        ans = n
    else:
        ans = n%base + 10* nconvert(n//base, base)
    return ans

print(nconvert(34, 16))