#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:17:26 2021

@author: pradyumna agrawal

CODE ORIGINALLY CREATED FOR PRAC 6 SUBMISSION FOR COURSE DATA STRUCTURE AND ALGORITHM UNIT 
AT CURTIN UNIVERSITY
"""

from linkedKList import DSALinkedList
from DSAHash import DSAHash
import numpy as np

class DSAGraph:
    '''
    This class represents a Directed, weighted graph with Adjacency list implementation using DSALinkedList
    '''
    
    def __init__(self):
        '''
        Default constructor. 
        Sets a DSALinkedList to contain graph vertices. 
        '''
        self.vertices = DSALinkedList()
        
    def addVertex(self, label, data):
        '''
        @param1: label -> A label to identify vertices. 
        @param2: value -> A value to save in vertices. They can be anything (example - weight of vertex)
        Add a vertex to the graph
        '''
        if self.hasVertex(label): #check if vertex already exists. 
            print("vertex already exists")
        else: #if not, then create a new DSAGraphVertex object and add it to the vertexlist of the graph. 
            newVertex = DSAGraphVertex(label, data)
            self.vertices.insertLast(newVertex)
            
    def hasVertex(self, label):
        '''
        @param: label -> Name of the vertex that needs to be searched
        @return: result (Boolean) -> true if vertex is in the graph, false otherwise.
        This function tells whether a vertex label is in graph or not
        '''
        result = False #assume that vertex is not there
        for i in self.vertices: #self made iterator
            if i.getLabel() == label:
                result = True #vertex found.
        return result
    
    def getVertex(self, label):
        '''
        @param: label -> Label of the vertex that needs to be returned
        @return: DSAGraphVertex -> Object that has the same label name. 
        This function takes a vertex label and returns vertex associated with that label. 
        '''
        for i in self.vertices: #interate over vertex list
            if i.getLabel() == label: #if a match is found
                return i #return that vertex
        
        return None #return nothing if not found
        
    def deleteVertex(self, label):
        '''
        @param: label -> Label of the vertex that needs to be deleted
        This function takes a vertex label and deletes vertex associated with that label. 
        '''
        
        if self.hasVertex(label): #check if vertex label is in the graph. 
            for i in self.vertices: # we have to delete all edges as well. so iterate over adjacency list (DSALinkedList) of the vertex. 
                adjList = i.getAdjacentList()
                for j in adjList: #iterate over all the vertices in the adjaceny list. 
                    if j.vertex.getLabel() == label: #label mathced. 
                        adjList.deleteNode(j) #delete that node
            self.vertices.deleteNode(self.getVertex(label)) #delete vertex. 
            
        
    def getVertexCount(self):
        '''
        return: Count (int) -> number of vertices. 
        this function returns number of vertices in the graph
        '''
        count = 0 #start with count zero
        for i in self.vertices: #iterate over all vertices
            count += 1 #increase count
        return count 
    
    def getAdjacent(self, label):
        '''
        @param: label of the vertex
        @returnL Adjacency List (DSALinkedList)
        if a vertex is in the graph, return its adjacency list 
        '''
        vertex = self.getVertex(label) #get the vertex from the label
        if (vertex): #if vertex exists
            return vertex.getAdjacentList() #return its adjacentList
        return None #else return nothing. 
        
    def addEdge(self, label1, label2, value = None):
        '''
        @param1: label1 -> from label
        @param2: label2 -> to label
        @param3: value -> edge weight (optional)  
        
        Basically, add label 2 in the adjacency of label 1
        '''
        
        if not self.hasVertex(label1):
            raise ValueError('No such vertex exists')  
        if not self.hasVertex(label2):
            raise ValueError('No such vertex exists')
        if not self.isAdjacent(label1, label2):
           
            v1 = self.getVertex(label1)
            v2 = self.getVertex(label2)
            v1.addAdjacent(v2, value)
            

    
    def isAdjacent(self, label1, label2):
        '''
        @param1: label1 -> from label
        @param2: label2 -> to label
        @return: Boolean -> true if edge exists from label 1 to label 2, false other wise
        
        This function checks if two vertices are adjacent
        '''
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    return True
        return False
    
    def deleteEdge(self, label1, label2):
        '''
        @param1: label1 -> from label
        @param2: label2 -> to label
        
        This function deletes edge from label1 to label2
        '''
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    adjacentList.deleteNode(j)
                    
    def updateEdge(self, label1, label2, Ecode):
        '''
        @param1: label1 -> from label
        @param2: label2 -> to label
        @param3: Ecode -> new weight
        
        This function updates the weight of an edge (Ecode in this case)
        '''
        
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    j.setWeight(Ecode)
                    
    
    def getEdgeWeight(self, label1, label2):
        '''
        @param1: label1 -> from label
        @param2: label2 -> to label
        @return: Ecode -> the weight of an edge
        
        This function returns weight of edge label1 -> label2
        '''
        
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    return j.getWeight()
    
    def getEdgeCount(self):
        
        '''
        @return: Int -> number of edges in the graph
        
        This function returns number of edges in the graph
        '''
        count = 0
        for i in self.vertices:
            adjacentList = i.getAdjacentList()
            for j in adjacentList:
                count = count + 1
        return int(count)
            
            
    def displayMatrix(self):
        '''
        @return: matrix (np.array) -> adjacency matrix
        This function returns graph in the format of Adjacency Matrix
        '''
        count = 0
        count = self.getVertexCount()
        vertexHash = DSAHash(count)
        matrix = np.zeros([count+1, count+1], dtype = object)
        for idx, i in enumerate(self.vertices): 
            matrix[idx+1][0] = matrix[0][idx+1] = i.getLabel()
            vertexHash.put(i.getLabel(), idx+1)
        for i in self.vertices:
            for j in i.vertexList:
                matrix[vertexHash.getData(i.getLabel())][vertexHash.getData(j.vertex.getLabel())] = j.getWeight()
        return matrix
            
    
    def _findPaths(self, start, target, visited, T, paths):
        '''
        @param1: start -> the node from which paths should be found 
        @param2: target -> the node to which paths should be found
        @param3: visited -> DSAHash that keeps track of all the nodes visited
        @param4: T -> DSALinkedList to keep track of the path getting travered currently
        @param5: paths -> DSALinkedList to save all the completed paths found till now.
        
        Code Reference:
            @Author: Shivam Gupta
            @Last Updated: 02 Jul, 2021
            @Link: https://www.geeksforgeeks.org/find-paths-given-source-destination/
        
        '''
        visited.put(start.getLabel(), start)
        T.insertLast(start.getLabel())
        if start == target:
            temp = DSALinkedList()
            for i in T:
                temp.insertLast(i)
            paths.insertLast(temp)
            
        else:
            for i in start.getAdjacentList():
                if not visited.hasKey(i.vertex.getLabel()):
                    self._findPaths(i.vertex, target, visited, T, paths)
        T.removeLast()
        visited.deleteKey(start.getLabel())          
        
                    
    def findPaths(self, start, target):
        '''
        @param1: start -> the node from which paths should be found 
        @param2: target -> the node to which paths should be found
        @return: paths -> A DSALinkedList with all possible paths. 
        
        Code Reference:
            @Author: Shivam Gupta
            @Last Updated: 02 Jul, 2021
            @Link: https://www.geeksforgeeks.org/find-paths-given-source-destination/  
        '''
        paths = DSALinkedList() #it will save all completed paths
        visited = DSAHash(10) #it will keep track of all the nodes visited till now
        T = DSALinkedList() #it will jeep track of the path in constructions
        self._findPaths(start, target, visited, T, paths) #call recursive function. 
        return paths

            
class DSAGraphVertex():

    #This class represents vertices of a graph. 
    
    
    def __init__(self, label, data):
        '''
        DEFAULT CONSTRUCTOR
        @param1: label -> label of the vertex
        @param2: data -> can be anything (for example weight, color)
        '''
        self.label = label #set label
        self.data = data #set data
        self.vertexList = DSALinkedList() #set vertex list 
        
    def __str__(self): #prints data
        return self.data

    #setters and getters    
    def getLabel(self):
        return self.label
    
    def getData(self): #returns data
        return self.data
    
    def updateData(self, data): #sets data
        self.data = data
    
    def getAdjacentList(self): #returns adjacency list (DSALinkedList)
        return self.vertexList
    
    
    def addAdjacent(self, vertex, value):
        '''
        @param1: vetex -> DSAGraph vertex (to vertex)
        @param2: value -> Weight of the edge
        This function adds an edge
        '''
        
        edge = DSAGraphEdge(vertex, value)
        self.vertexList.insertLast(edge)
    
    
class DSAGraphEdge():
    
    #this class represents a graph edge. It has name of a vertex and the weight
    
    def __init__(self, vertex, value): #default constructor
        self.vertex = vertex #add vertex
        self.value = value #add weight
        
    def getWeight(self):
        return self.value #return weight
    
    def setWeight(self, weight):
        self.value = weight #set weight
        


a = DSAGraph()
for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
    a.addVertex(i, i)
    

a.addEdge('A', 'B', 35)
a.addEdge('A', 'F', 30)
a.addEdge('A', 'D', 40)
a.addEdge('B', 'E', 35)
a.addEdge('C', 'F', 30)
a.addEdge('D', 'H', 45)
a.addEdge('E', 'G', 35)
a.addEdge('D', 'E', 60)
a.addEdge('F', 'E', 45)
a.addEdge('H', 'J', 50)
#a.displayList()

b = a.findPaths(a.getVertex('A'), a.getVertex('E'))

for i in b:
    print(type(i))
    
################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########