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

def int2chr(n):
    if n <= 9:
        return chr(n + ord('0'))
    else:
        return chr(n - 10 + ord('A'))
    
def nconvert(n, base):
    if base > 16 or base < 2:
        return "choose a base between 2 and 16"
    if n < base:
        ans = int2chr(n)
    else:
        ans = nconvert(n//base, base) + int2chr(n%base)
    return ans

#print(nconvert(14782, 2))

def moveDisk(src, dest, level):
    print("\t" * (level) + "moving one disc from disc " + str(src) + "to " + str(dest))

def towerOfHanoi(n, src, dest, level):
    print("\t" * level + "towerOfHanoi(" + str(n) + "," + str(src) + "," + str(dest) + ')')
    if n == 1:
        moveDisk(src, dest, level)
    else:
        tmp = 6 - src - dest
        towerOfHanoi(n-1, src, tmp, level+1)
        moveDisk(src, dest, level+1)
        towerOfHanoi(n-1, tmp, dest, level+1)
        

def main():
    while(True):
        print("G'day mate. Which program you wanna run today?\n(1) (F)actorial\n(2) (G)CD\n(3) (N)umber Converter\n(4) (T)ower of Hanoi\n(5) (E)xit\n")
        menu = input().upper()
        if menu == "F":
            ans = factorial(int(input("Thats a great choice\nSo which factorial would you like to calculate?")))
            print("Here is your answer " + str(ans) + "\n")
        elif menu == "G":
            num1 = int(input("enter first number"))
            num2 = int(input("enter second number"))
            ans = gcd(num1, num2)
        elif menu == "N":
            num1 = int(input("enter the base to which you want to convert"))
            num2 = int(input("enter number in decimal"))
            ans = nconvert(num2, num1)
            print(str(num2) + " in " + str(num1) + " base is " + str(ans) + "\n")
        elif menu == "T":
            num = input("How many rings you want in the the game")
            towerOfHanoi(int(num), 1, 3, 0)
        elif menu == "E":
            break
        else:
            print("Please enter a valid input as follow \n")
if __name__ == "__main__":
    main()