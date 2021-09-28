#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 09:04:59 2021

@author: pradyumna AGrawal
"""

from DSAGraphWithEdge import DSAGraph, GraphIO
def main():
    
    # First we will create a graph and add three vertices into it
    
    A = DSAGraph()
    A.addVertex(1, "A")
    A.addVertex(2, "B")
    A.addVertex(3, "C")
    A.addEdge(1, 2) #Adding a edge without weight
    A.addEdge(4, 2, 6) #Adding an edge with weight
    A.addEdge(2, 3, 1) 
    A.addEdge(3, 1, 6)
    A.addEdge(4, 5, 1)
    
    A.displayList() #Displaying graph in adjacency list form
    
    print('\ngraph has 1: ', A.hasVertex(1)) #should return true
    
    print('graph has 333: ', A.hasVertex(333)) #should return false
    
    print('\ngraph has a total vertex :', A.getVertexCount()) #should return 5
    
    print('\ngraph has total edges : ', A.getEdgeCount()) #should resturn 5
    
    print('\ndegree of vertex 2 is: ', A.degree(2)) #should print 3
    
    print('\n')

    #input output 
    io = GraphIO() #creating input output object 
    
    graph = io.makeGraph('prac6_Act_4.al') #reading a file
    
    io.saveSerialisedGraph(graph, 'DATFile') #saving it as a serialised file
    
    graph2 = io.loadSerialisedGraph('DATFile') #reading that file again 
   
    graph2.displayList() #displaying adjacency list 
    print('\n')
    print(graph.BFS()) #printing BFS
    print('\n')
    print(graph.DFS()) #printing DFS
    
    io.saveGraph(graph, 'prac6_Act_4_BFST.al', "BFS") #saving BFS minimum spanning tree
    
if __name__ == "__main__":
    main()
