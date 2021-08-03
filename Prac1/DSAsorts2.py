#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

def bubbleSort(A):
    pas = 0   #this counter tells how many numbers at the end of array are sorted
    sort = False #this bool tells wether the array is sorted or not
    while sort == False: #run till the array is not sorted
        sort = True #lets assume the array is sorted
        for i in range(len(A) - pas - 1): #run till the unsorted part of array
            if A[i][0] > A[i+1][0]: #check if our assumption is true
                temp = A[i]
                A[i] = A[i+1]
                A[i+1] = temp
                sort = False #yo so assumption is wrong 
        pas = pas + 1 #anyway, one more bubble bursted. 
    return A #return the array              

def insertionSort(A):
    for i in range(1,len(A)): #Run from second index to last
        j = i #basically j means that array till j is sorted
        temp = A[j] #now make j as the element that we want to insert
        while j > 0 and A[j - 1][0] > temp[0]: #check for the location where we want to insert it
            A[j] = A[j-1] #keep swaping 
            j = j-1 #keep husling mate
        A[j] = temp #ah we found it, now insert
    return A #dont forget to return the array

def selectionSort(A):
    for i in range(len(A) -1): #run till second last index
        minima = i #let the ith index be the smallest 
        for j in range(i+1, len(A)): #check from ith index till last index
            if A[j][0] < A[minima][0]: #check if that index is smallest
                minima = j #well it is smallest
        temp = A[i] # now we know the smallest one, so lets put is in front
        A[i] = A[minima] 
        A[minima] = temp
    return A #dont forget to return the array. 

def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    ...

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    ...

def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    ...
    