#
# DSA Final Assessment Question 4 - Q4MaxHeapTest.py
#
# Name : Pradyumna Agrawal
# ID   : 20046165
#
# 
import heapq #import heapq

print("\n===== Question 4: Testing Heaps =====\n")

		
print("Adding items...")
heapList = [] #declare a heap list
A = heapq.heapify(heapList) #heapify the list
for i in range(0, 10): #add items from 0 to 1
	heapq.heappush(heapList, -i) #i negate the priority as the inbuilt heap that I am using is a min heap. However, we want functionality of a max heap. Easiest way to do that is by negating priority at addition and then negating it again.
	print("Added " + "value-"+str(i)+" Priority: ", str(i))

print()

print("Removing items...")
for i in range(0, 10):
	temp = heapq.heappop(heapList)
	print(-temp)
    
print("\n===== Tests Complete =====\n")

#only priority is used. No value is added as 
#I was not able to find an iinbuilt heap that can also save values. 
