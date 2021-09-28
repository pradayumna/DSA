#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 23:53:52 2021

@author: pradyumna agrawal
"""
import prac2func as f


def factorial(number):
    if number < 0:
        raise ValueError(str(number) + " is not a valid input.")
    else:
        return f._factorial(number)

def fibonacci(number):
    if number < 0:
        raise ValueError(str(number) + " is not a valid input.")
    else:
        return f._fibonacii(number)
def gcd(num1, num2):
    if num1 < 1 or num2 < 1:
        raise ValueError("please enter numbers greater than 0")
    else:
        return f._gcd(num1, num2)

def nconvert(num1, num2):
    if num2 < 0:
        raise ValueError("please enter a non-negative integer")
    else:
        return f._nconvert(num1, num2)

def main():
    while(True):
        print("G'day mate. Which program you wanna run today?\n(1) (F)actorial\n(2) Fibon(a)cii\n(3)(G)CD\n(4) (N)umber Converter\n(5) (E)xit\n")
        menu = input().upper()
        if menu == "F":
            try:
                inp = int(input("Thats a great choice\nSo which factorial would you like to calculate?"))
                ans = factorial(inp)
                print("Here is your answer " + str(ans) + "\n")
            except ValueError as err:
                print(err, "Please enter a non-negative integer")
        elif menu == "G":
            try:
                num1 = int(input("enter first number"))
                num2 = int(input("enter second number"))
                ans = gcd(num1, num2)
                print(ans)
            except ValueError as err:
                print(err, "Please enter a non-negative integer")
        elif menu == "N":
            try:
                num1 = int(input("enter the base to which you want to convert"))
                num2 = int(input("enter number in decimal"))
                ans = nconvert(num2, num1)
            except ValueError as err:
                print(err, "please enter a non-negative number")
            print(str(num2) + " in " + str(num1) + " base is " + str(ans) + "\n")
        elif menu == "A":
            try:
                inp = int(input("Thats a great choice\nSo which fibonacci number would you like to calculate?"))
                ans = fibonacci(inp)
                print("Here is your answer " + str(ans) + "\n")
            except ValueError as err:
                print(err, "Please enter a non-negative integer")
        elif menu == "E":
            break
        else:
            print("Please enter a valid input as follow \n")
if __name__ == "__main__":
    main()

