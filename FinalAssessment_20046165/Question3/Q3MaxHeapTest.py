#
# DSA Final Assessment Question 3 - Q3MaxHeapTest.py
#
# Name : 
# ID   :
#
# 
from Q3MaxHeap import *

print("\n===== Question 3: Testing Heaps =====\n")

testHeap = Q3MaxHeap()
		
print("Adding items...")
for i in range(0, 10):
	testHeap.add(i, "value-"+str(i))
	print("Added " + "value-"+str(i)+" Priority: ", str(i))

print()

print("Removing items...")
for i in range(0, 10):
	temp = testHeap.remove()
	print(temp)
    
print("\n===== Tests Complete =====\n")
