#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 00:17:26 2021

@author: pradyumna agrawal
"""

from linkedKList import DSALinkedList
import os
from DSAQueue import queue
from DSAHash import DSAHash
import pickle 
import numpy as np

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
        
    def deleteVertex(self, label):
        if self.hasVertex(label):
            for i in self.vertices:
                adjList = i.getAdjacentList()
                for j in adjList:
                    if j.vertex.getLabel() == label:
                        adjList.deleteNode(j)
            self.vertices.deleteNode(self.getVertex(label))
            
        
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
        
    def addEdge(self, label1, label2, value = None):
        
        if not self.hasVertex(label1):
            raise ValueError('No such vertex exists')  
        if not self.hasVertex(label2):
            raise ValueError('No such vertex exists')
        if not self.isAdjacent(label1, label2):
           
            v1 = self.getVertex(label1)
            v2 = self.getVertex(label2)
            v1.addAdjacent(v2, value)
            

    
    def isAdjacent(self, label1, label2):
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    return True
        return False
    
    def deleteEdge(self, label1, label2):
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    adjacentList.deleteNode(j)
                    
    def updateEdge(self, label1, label2, Ecode):
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    j.setWeight(Ecode)
                    
    
    def getEdgeWeight(self, label1, label2):
        v1 = self.getVertex(label1)
        if(v1):
            adjacentList = v1.getAdjacentList()
            for j in adjacentList:
                label = j.vertex.getLabel()
                if label == label2:
                    return j.getWeight()
    
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
                label = j.vertex.getLabel()
                print(str(label), end = " ")
            print()
            
    def displayMatrix(self):
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
            
    def degree(self, label):
        v = self.getVertex(label)
        if(v):
            return v.getDegree()
        return 0
    
    def _DFS(self, v, visited, T):
        visited.add(v)
        for i in v.getAdjacentList():
            if i.vertex not in visited:
                T.append([v.getLabel(), i.vertex.getLabel(), i.getWeight()])
                self._DFS(i.vertex, visited, T)
        return T
    
    def DFS(self):
        visited = set()
        T = []
        T = self._DFS(self.vertices.head.value, visited, T)
        return T
    
    def _BFS(self, q, visited, T):
        
        if q.isEmpty():
            return T
        else:
            v = q.dequeue()
            for w in v.getAdjacentList():
                if w.vertex not in visited:
                    T.append([v.getLabel(), w.vertex.getLabel(), w.getWeight()])
                    visited.add(w.vertex)
                    q.enqueue(w.vertex)
                    
            T = self._BFS(q, visited, T)
                
        
    def BFS(self):
        visited = set()
        T = []
        visited.add(self.vertices.head.value)
        q = queue()
        q.enqueue(self.vertices.head.value)
        self._BFS(q, visited, T)
        return T
            
class DSAGraphVertex():
    
    def __init__(self, label, data):
        self.label = label
        self.data = data
        self.vertexList = DSALinkedList()
        
    def __str__(self):
        return self.data

        
    def getLabel(self):
        return self.label
    
    def getData(self):
        return self.data
    
    def updateData(self, data):
        self.data = data
    
    def getAdjacentList(self):
        return self.vertexList
    
    def printAdjacentList(self):
        for i in self.getAdjacentList():
            print([i.vertex.getLabel(), i.value], end = " ")
    
    def addAdjacent(self, vertex, value):
        edge = DSAGraphEdge(vertex, value)
        self.vertexList.insertLast(edge)
    
    def getDegree(self):
        count = 0
        for i in self.vertexList:
            count += 1
        return count
    
class DSAGraphEdge():
    
    def __init__(self, vertex, value):
        self.vertex = vertex
        self.value = value
        
    def getWeight(self):
        return self.value
    
    def setWeight(self, weight):
        self.value = weight
        
        
class GraphIO():
    def __init__(self):
        self.graph = DSAGraph()
    def makeGraph(self, filename):
        if os.path.isfile(filename):
            file = open(filename)
            a = file.readlines()
            lst = [[i.split(' ')[0], i.split(' ')[1].strip(), i.split(' ')[2].strip()] for i in a]
            for i in lst:
                self.graph.addEdge(i[0], i[1], i[2])

        return self.graph
    
    def saveGraph(self, graph, filename, variety):
        file = open(filename, 'w')
        if variety == "BFS":
            T = graph.BFS()
        else:
            T = graph.DFS()
        for i in T:
            string = str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + '\n'
            file.write(string)
            
    def loadSerialisedGraph(self, filename):
        try:
            with open(filename, "rb") as dataFile:
                self.graph = pickle.load(dataFile)
        except:
            print("file does not exist")
        return self.graph
    
    def saveSerialisedGraph(self, graph, filename):
        with open(filename, "wb") as f:
                pickle.dump(graph, f)

