#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#
import numpy as np
import statistics
import random

def bubbleSort(A):
    pas = 0   #this counter tells how many numbers at the end of array are sorted
    sort = False #this bool tells wether the array is sorted or not
    while sort == False: #run till the array is not sorted
        sort = True #lets assume the array is sorted
        for i in range(len(A) - pas - 1): #run till the unsorted part of array
            if A[i] > A[i+1]: #check if our assumption is true
                A[i] = A[i] + A[i+1] #if not, make a swap
                A[i+1] = A[i] - A[i +1]
                A[i] = A[i] - A[i+1]
                sort = False #yo so assumption is wrong 
        pas = pas + 1 #anyway, one more bubble bursted. 
    return A #return the array
          

def insertionSort(A):
    for i in range(1,len(A)): #Run from second index to last
        j = i #basically j means that array till j is sorted
        temp = A[j] #now make j as the element that we want to insert
        while j > 0 and A[j - 1] > temp: #check for the location where we want to insert it
            A[j] = A[j-1] #keep sliding 
            j = j-1 #keep husling mate
        A[j] = temp #ah we found it, now insert
    return A #dont forget to return the array

def selectionSort(A):
    for i in range(len(A) -1): #run till second last index
        minima = i #let the ith index be the smallest 
        for j in range(i+1, len(A)): #check from ith index till last index
            if A[j] < A[minima]: #check if that index is smallest
                minima = j #well it is smallest
        temp = A[i] # now we know the smallest one, so lets put is in front
        A[i] = A[minima] 
        A[minima] = temp
    return A #dont forget to return the array. 

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    leftIdx = depth = 0
    rightIdx = len(A) - 1
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx)//2
        _mergeSortRecurse(A, leftIdx, midIdx, depth+1)
        _mergeSortRecurse(A, midIdx+1, rightIdx, depth+1)
        _merge(A, leftIdx, midIdx, rightIdx, depth+1)
    return A

def _mergeSortRecurse(A, leftIdx, rightIdx, depth):
    #for i in range(depth):
        #print('\t' + '|', end = '')
    #print('_mergeSortRecurse( ' + str(A) + ', ' + str(leftIdx) + ', ' + str(rightIdx) + ')')
    print(depth)
    if leftIdx < rightIdx:
        midIdx = (leftIdx + rightIdx)//2
        _mergeSortRecurse(A, leftIdx, midIdx, depth+1)
        _mergeSortRecurse(A, midIdx+1, rightIdx, depth+1)
        _merge(A, leftIdx, midIdx, rightIdx, depth+1)

def _merge(A, leftIdx, midIdx, rightIdx, depth):
    print(depth)
    # for i in range(depth):
    #     print('\t' + '|', end = '')
    # print('_merge( ' + str(A) + ', ' + str(leftIdx) + ', ' + str(midIdx) + ', ' + str(rightIdx) + ')')
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
    depth = 0
    leftIdx = 0
    rightIdx = len(A) - 1
    _quickSortRecurse(A, leftIdx, rightIdx, depth)
    return A

def _quickSortRecurse(A, leftIdx, rightIdx):
    # for i in range(depth):
    #     print('\t' + '|', end = '')
    # print('qsort_rec( ' + str(A) + ', ' + str(leftIdx) + ', ' + str(rightIdx) + ')')
    if rightIdx > leftIdx:
        pivotIdx = leftIdx
        newPivotIdx = _doPartistioning(A, leftIdx, rightIdx, pivotIdx)
        
        _quickSortRecurse(A, leftIdx, newPivotIdx-1)
        _quickSortRecurse(A, newPivotIdx+1, rightIdx)

def _doPartistioning(A, leftIdx, rightIdx, pivotIdx):
    # for i in range(depth):
    #     print('\t' + '|', end = '')
    # print('dopart( ' + str(A) + ', ' + str(leftIdx) + ', ' + str(rightIdx) + ', ' + str(pivotIdx) + ')')
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
def _quickSortRandomRecurse(A, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = random.randint(leftIdx, rightIdx)
        newPivotIdx = _doPartistioning(A, leftIdx, rightIdx, pivotIdx)
        
        _quickSortRecurse(A, leftIdx, newPivotIdx-1)
        _quickSortRecurse(A, newPivotIdx+1, rightIdx)
    
def radixSort(A):
    ...