#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 11:16:27 2021

@author: pradyumna agrawal
"""

import numpy as np 
import random

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    leftIdx = 0
    rightIdx = len(A) - 1
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx)//2
        _mergeSortRecurse(A, leftIdx, midIdx)
        _mergeSortRecurse(A, midIdx+1, rightIdx)
        _merge(A, leftIdx, midIdx, rightIdx)
    return A

def _mergeSortRecurse(A, leftIdx, rightIdx):
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx)//2
        _mergeSortRecurse(A, leftIdx, midIdx)
        _mergeSortRecurse(A, midIdx+1, rightIdx)
        _merge(A, leftIdx, midIdx, rightIdx)

def _merge(A, leftIdx, midIdx, rightIdx):
    tempArr = np.empty(rightIdx - leftIdx + 1)
    ii = leftIdx
    jj = midIdx + 1
    kk = 0
    while (ii <= midIdx) and (jj <= rightIdx):
        if A[ii] < A[jj]:
            tempArr[kk] = A[ii]
            ii += 1
        else:
            tempArr[kk] = A[jj]
            jj += 1
        kk += 1
    for i in range(ii, midIdx+1):
        tempArr[kk] = A[i]
        kk += 1
    for i in range(jj, rightIdx+1):
        tempArr[kk] = A[i]
        kk += 1
    for i in range(leftIdx, rightIdx+1):
        A[i] = tempArr[i - leftIdx]




def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    leftIdx = 0
    rightIdx = len(A) - 1
    if rightIdx > leftIdx:
        pivotIdx = leftIdx
        newPivotIdx = _doPartistioning(A, leftIdx, rightIdx, pivotIdx)
        
        _quickSortRecurse(A, leftIdx, newPivotIdx-1)
        _quickSortRecurse(A, newPivotIdx+1, rightIdx)
    return A

def _quickSortRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = leftIdx
        newPivotIdx = _doPartistioning(A, leftIdx, rightIdx, pivotIdx)
        
        _quickSortRecurse(A, leftIdx, newPivotIdx-1)
        _quickSortRecurse(A, newPivotIdx+1, rightIdx)

def _doPartistioning(A, leftIdx, rightIdx, pivotIdx):
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal
    currIdx = leftIdx
    for i in range(leftIdx, rightIdx+1):
        if A[i] < pivotVal:
            A[i], A[currIdx] = A[currIdx], A[i]
            currIdx += 1
    A[currIdx], A[rightIdx] = A[rightIdx], A[currIdx]
    return currIdx

def median_of_three(L, low, high, mid):
    a = L[low]
    b = L[mid]
    c = L[high]
    if a <= b <= c:
        return mid
    if c <= b <= a:
        return mid
    if a <= c <= b:
        return high
    if b <= c <= a:
        return high
    return low

def quickSortMedian3(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    leftIdx = 0
    rightIdx = len(A) - 1
    _quickSortMedian3Recurse(A, leftIdx, rightIdx)
    return A   

def _quickSortMedian3Recurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        midIdx = (leftIdx + rightIdx)//2
        pivotIdx = median_of_three(A, leftIdx, rightIdx, midIdx)
        newPivotIdx = _doPartistioning(A, leftIdx, rightIdx, pivotIdx)
        
        _quickSortRecurse(A, leftIdx, newPivotIdx-1)
        _quickSortRecurse(A, newPivotIdx+1, rightIdx)
        
def quickSortRandom(A):
    leftIdx = 0
    rightIdx = len(A) - 1
    _quickSortRandomRecurse(A, leftIdx, rightIdx)
    return A
    
def _quickSortRandomRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = random.randint(leftIdx, rightIdx)
        newPivotIdx = _doPartistioning(A, leftIdx, rightIdx, pivotIdx)
        
        _quickSortRecurse(A, leftIdx, newPivotIdx-1)
        _quickSortRecurse(A, newPivotIdx+1, rightIdx)

A = np.array([3,0, 0, 1, 12, 3, 12, 11, 99])
print('printing results of merge sort')
print('unsorted array is ', A)
print(mergeSort(A))

input('press enter to use next type of sorting: quick sort')
print('\n'*5)
A = np.random.randint(50, size= 10)
print('unsorted array is ', A)
print('sorted array is ', quickSort(A))

input('press enter to use next type of sorting: quick sort 3 median')
print('\n'*5)
A = np.random.randint(50, size= 10)
print('unsorted array is ', A)
print('sorted array is ', quickSortMedian3(A))

input('press enter to use next type of sorting: quick sort random')
print('\n'*5)
A = np.random.randint(50, size= 10)
print('unsorted array is ', A)
print('sorted array is ', quickSortRandom(A))