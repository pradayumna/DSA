#
# DSA Final Assessment Question 3 - Q3MaxHeapTest.py
#
# Name : Pradyumna Agrawal
# ID   : 20046165
#
# 
from FA_MinHeap import * #changed name of the file from which heap structure is getting imported
from PracExamException import PracExamException #importing exception class

print("\n===== Question 3: Testing Heaps =====\n")

testHeap = FA_MinHeap() #changed the heap declaration to declare a minHeap instead. 
		
print("Adding items...")
for i in range(0, 10):
	testHeap.add(i, "value-"+str(i))
	print("Added " + "value-"+str(i)+" Priority: ", str(i))

print()

#after adding 10 items, we add one more item while the maxsize of heaparray is 10 to check is the exception handling is working
print('\nadding extra item to see if exception handling works\n')
try: 
    testHeap.add(11, "eleven") #try to add up an extra item. It should not execute and an error should occur
except PracExamException as err:
    print("\nexception handling is working for add\n", err) #if this prints that would mean that error handling is working correctly.
    

print("Removing items...")
for i in range(0, 10):
	temp = testHeap.remove()
	print(temp)

#heap array had 10 items. We have removed all of them. Now we will remove one more item to see if exception handling is working. 
print('\nremoving extra item to see if exception handling works\n')
try:
    testHeap.remove() #try removing an element from an empty heap. This should not execute and error should occur. 
except PracExamException as err:
    print("\nexception handling is working for remove\n", err) #if this prints that would mean that error handling is working fine. 
    
print("\n===== Tests Complete =====\n")


print('\nPerforming File IO\n')
filename = 'Q3HeapData.txt' #defining file name
link = open(filename, 'r') #opening file
data = link.readlines() #reading file

heapIO = FA_MinHeap() #declaring min heap
for i in data: #using for loop to add items in heap array
    heapIO.add(int(i.split(' ')[0]), i.split(' ')[1].strip()) #adding one item at a time
    heapIO.printHeap() #printing heap after every addition
    
#removing items from the heap 
for i in range(0, 11):
    temp = heapIO.remove()
    print('the item removed is ', temp)
    heapIO.printHeap() #printing heap after every removal
