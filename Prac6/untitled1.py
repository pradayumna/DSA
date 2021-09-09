#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:17:26 2021

@author: pradyumna agrawal
"""

from linkedKList import DSALinkedList
import os


class DSAGraph:
    
    def __init__(self):
        self.vertices = DSALinkedList()
        
    def addVertex(self, label, data):
        if self.hasVertex(label):
            print("vertex already exists")
        else:
            newVertex = DSAGraphVertex(label, data)
            self.vertices.insertLast(newVertex)
            
    def hasVertex(self, label):
        result = False
        for i in self.vertices:
            if i.getLabel() == label:
                result = True
        return result
    
    def getVertex(self, label):
        for i in self.vertices:
            if i.getLabel() == label:
                return i
        else:
            return None
        
    def getVertexCount(self):
        count = 0
        for i in self.vertices:
            count += 1
        return count
    
    def getAdjacent(self, label):
        vertex = self.getVertex(label)
        if (vertex):
            return vertex.getAdjacentList()
        return None
        
    def addEdge(self, label1, label2):
        
        if not self.hasVertex(label1):
            self.addVertex(label1, None)   
        if not self.hasVertex(label2):
            self.addVertex(label2, None)
        if not self.isAdjacent(label1, label2):
           
            v1 = self.getVertex(label1)
            v2 = self.getVertex(label2)
            v1.addAdjacent(v2)
            v2.addAdjacent(v1)  

    
    def isAdjacent(self, label1, label2):
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.getLabel()
                if label == label2:
                    return True
        return False
        
    
    def getEdgeCount(self):
        count = 0
        for i in self.vertices:
            adjacentList = i.getAdjacentList()
            for j in adjacentList:
                count = count + 1
        return int(count/2)
            
    def displayList(self):
        for i in self.vertices:
            label = i.getLabel()
            adjacentList = i.getAdjacentList()
            print(str(label) + ' : ', end = " ")
            for j in adjacentList:
                label = j.getLabel()
                print(str(label), end = " ")
            print()
            
    def degree(self, label):
        v = self.getVertex(label)
        if(v):
            return v.getDegree()
        return 0
    
    def _DFS(self, v, visited, T):
        visited.add(v)
        for i in v.getAdjacentList():
            if i not in visited:
                T.append([v.getLabel(), i.getLabel()])
                self._DFS(i, visited, T)
        return T
    
    def DFS(self):
        visited = set()
        T = []
        T = self._DFS(self.vertices.head.value, visited, T)
        return T
    
    def _BFS(self, v, visited, T):
        visited.add(v)
        searchList = []
        for i in v.getAdjacentList():
            if i not in visited:
                T.append([v.getLabel(), i.getLabel()])
                visited.add(i)
                searchList.append(i)
        for i in searchList:
            T = self._BFS(i, visited, T)
        return T
                
        
    def BFS(self):
        visited = set()
        T = []
        T = self._BFS(self.vertices.head.value, visited, T)
        return T
            
class DSAGraphVertex():
    
    def __init__(self, label, data):
        self.label = label
        self.data = data
        self.vertexList = DSALinkedList()

        
    def getLabel(self):
        return self.label
    
    def getData(self):
        return self.data
    
    def getAdjacentList(self):
        return self.vertexList
    
    def printAdjacentList(self):
        for i in self.getAdjacentList():
            print(i.getLabel(), end = " ")
    
    def addAdjacent(self, vertex):
        self.vertexList.insertLast(vertex)
    
    def getDegree(self):
        count = 0
        for i in self.vertexList:
            count += 1
        return count
        
        
class GraphIO():
    def __init__(self):
        self.graph = DSAGraph()

    def makeGraph(self, filename):
        if os.path.isfile(filename):
            file = open(filename)
            a = file.readlines()
            lst = [[i.split(' ')[0], i.split(' ')[1].strip()] for i in a]
            for i in lst:
                print(i)
                self.graph.addEdge(i[0], i[1])

        return self.graph

def main():
    A = DSAGraph()
    A.addVertex(1, "A")
    A.addVertex(2, "B")
    A.addVertex(3, "C")
    A.addEdge(1, 2)
    A.addEdge(4, 2)
    A.addEdge(2, 3)
    A.addEdge(3, 1)
    A.addEdge(4, 5)
    A.displayList()
    
    io = GraphIO()
    graph = io.makeGraph('prac6_1.al')
    graph.displayList()
    print(graph.BFS())
    print(graph.DFS())
    
if __name__ == "__main__":
    main()