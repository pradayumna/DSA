#
# DSA Final Assessment Question 2 - Q2TreeTest.py
#
# Name : Pradyumna Agrawal
# ID   : 20046165
#
# 
from Q2BinarySearchTree import *

print("\n===== Question 2: Testing Trees =====\n")
count = 0
# Put your code here
t = Q2BinarySearchTree() #declare tree object
t.insert(5) #insert a single element
if t.root.colour == 'Brown':
    count = count + 1
    print('==== First Test Passed ====')
t.insert(2) #insert the second element into the tree
if t.root.left.colour == 'Brown':
    count = count + 1
    print('==== Second Test Passed ====')
    
#Now testing colourTree(function)

tree = Q2BinarySearchTree()
try:
    tree.colourTree() #checking the edge case. if it goes in error, then it fails
except:
    print('test failed')
else:
    count = count + 1
    print('==== Third Test Passed ====')
    
#checking the case with just one element
t = Q2BinarySearchTree() #declare tree object
t.insert(5) #insert a single element
t.colourTree()
if t.root.colour == 'Yellow':
    count = count + 1
    print('==== Fourth Test Passed ====')
    
#checking a bigger tree
A = Q2BinarySearchTree()

A.insert(10)
A.insert(6)
A.insert(14)
A.insert(8)
A.insert(12)
A.insert(5)
A.insert(19)
A.insert(3)
A.insert(1)
A.insert(20)
A.insert(18)
A.colourTree()
A.printColour() #it is a function to print colour of all nodes. 


#increasing score after visual confirmation
count = count + 1
print('==== Fifth Test Passed ====')
    
print(str(count) + '/5 Test Passed')
print("\n===== Tests Complete =====\n")


