#
# DSA Final Assessment Question 5 - Q5Graph.py
#
# Name : 
# ID   :
#
# 
import numpy as np
from PracExamException import PracExamException 
      
class Q5Graph():

    def __init__(self):
        self.maxsize = 20
        self.wmatrix = np.zeros((self.maxsize,self.maxsize), dtype=int)
        self.labels = np.zeros(self.maxsize, dtype=object)
        self.count = 0

    def addVertex(self, vname):
        if self.count == self.maxsize:
            raise PracExamException("graph is full")
        if not self.hasVertex(vname):
            self.labels[self.count] = vname
            self.count += 1

    def addEdge(self, vname1, vname2, weight):
        self.addVertex(vname1)  # won't add if already there
        self.addVertex(vname2)
        label1 = self.getIndex(vname1)
        label2 = self.getIndex(vname2)
        self.wmatrix[label1,label2] = weight
        
    def getIndex(self, vname):   ## Not on slides
        returnval = None
        for i in range(self.count):
            if self.labels[i] == vname:
                returnval = i
        return returnval
        
    def hasVertex(self, vname):
        returnval = False
        for v in self.labels:
            if v == vname:
                returnval = True
        return returnval
        
    def getVertexCount(self):
        return self.count
    

    def displayAsList(self): 
        print('\nAdjacency list for graph is:\n')
        
        for i in range(self.count): #loop through all vertices
            print(self.labels[i], ':', end = ' ') #print the label
            for j in range(self.count): #print through all vertices
                if self.wmatrix[i][j] != 0: #check for an edge
                    print(self.labels[j], end = ' ') #if ende exists, print lables
            print()

    def readGraph(self, filename):

        link = open(filename, 'r') #opening file
        data = link.readlines() #reading file
        for i in data:
            info = i.split(' ') #getting the relevant information
            try:
                self.addVertex(info[0]) #adding a vertex
                self.addVertex(info[1]) #adding second vertex
                self.addEdge(info[0], info[1], info[2]) #adding an edge
            except IndexError():
                print('file format is not correct')
            
    def displayAsWeightMatrix(self):
        print('weighted matrix for the graph is:\n') #header
        print('   ', end = '') #initial gap for better formatting
        for i in range(self.count): #loop through all the vertices
            print(self.labels[i], end = ' ') #print vertex name
        print('\n------------------------------------') #print a line
        for i in range(self.count): #loop again
             print(self.labels[i], end = ' ') #print the label 
             for j in range(self.count): #print through the second axis
                 print(self.wmatrix[i][j], end = ' ') #print the weight
             print()
        
        
