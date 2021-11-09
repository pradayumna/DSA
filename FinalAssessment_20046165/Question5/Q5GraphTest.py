#
# DSA Final Assessment Question 5 - Q5GraphTest.py
#
# Name : 
# ID   :
#
# 
from Q5Graph import *
    

print("\n===== Question 5: Testing Graphs =====\n")

g = Q5Graph()

g.addVertex("one")
g.addVertex("two")
g.addVertex("three")
g.addVertex("four")

g.addEdge("one", "two", 3)
g.addEdge("one", "three", 4)
g.addEdge("one", "four", 5)
g.addEdge("four", "two", 6)
g.addEdge("four", "three", 7)

g.displayAsWeightMatrix()

print("\n===== Tests Complete =====\n")

print("now testing file IO functionality and display functions")

g2 = Q5Graph() # define a graph object 
g2.readGraph('Q5GraphData.txt') #read graph from the file
g2.displayAsWeightMatrix() #print graph in matrix form
g2.displayAsList() #print graph in list form


