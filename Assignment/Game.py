#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:13:47 2021

@author: pradyumna agrawal
"""
from DSAHash import DSAHash
from DSAGraphWithEdge import DSAGraph
import networkx as nx
import matplotlib.pyplot as plt
import random
from matplotlib.lines import Line2D
from DSAQueue import priorityQueue
import pickle

class Game():
    
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__NCode = DSAHash(10)
        self.__ECode = DSAHash(10)
        self.__graph = self.__makeGraph()
        self.__pathQueue = priorityQueue()
        
    def __makeGraph(self):
        #fully functional now
        Start = False
        Target = False
        file = open(self.__fileName, 'r')
        data = file.readlines()
        if len(data) == 0:
            raise ValueError("file is empty")
        graph = DSAGraph()
        for idx, i in enumerate(data): #gotta do something for this
            if i[0] != '#':
                information = i.strip().split(' ')
                if information != '':
                    if information[0] == 'Ecode':
                        try:
                            self.__ECode.put(information[1], int(information[2]))
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                        except KeyError:
                            print('line ' + str(idx) + ' is invalid as key already exists\n' + i)
                        except ValueError:
                            print('line ' + str(idx) + ' is invalid as value associated with E Code has to be an integer\n' + i)
                   
                    elif information[0] == 'Ncode':
                        try:
                            self.__NCode.put(information[1], int(information[2]))
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                        except KeyError:
                            print('line ' + str(idx) + ' is invalid as key already exists\n' + i)
                        except ValueError:
                            print('line ' + str(idx) + ' is invalid as value associated with N Code has to be an integer\n' + i)
                    elif information[0] == 'Node':
                        try:
                            if not self.__NCode.hasKey(information[2]):
                                print('line ' + str(idx) + ' is invalid as no such node code exists\n' + i)
                            else:
                                graph.addVertex(information[1], information[2])
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
            
                    elif information[0] == 'Edge':
                        try:
                            if not self.__ECode.hasKey(information[3]):
                                print('line ' + str(idx) + ' is invalid as no such edge code exists\n' + i)
                            else:
                                graph.addEdge(information[1], information[2], information[3])
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                        except ValueError:
                            print('line ' + str(idx) + ' is invalid as one of the nodes does not exists\n' + i)
                    
                    elif information[0] == 'Start':
                        try:
                            self.__Start = graph.getVertex(information[1])
                            Start = True and self.__Start
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                    
                    elif information[0] == 'Target':
                        try:
                            self.__Target = graph.getVertex(information[1])
                            print(self.__Target)
                            Target = True and self.__Target
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
        if not Start or not Target:
            raise KeyError()
        return graph
    
    def __visualise(self):
        G = nx.DiGraph()
        # I am going to use list for the next trick. Pardon me.
        colorHash = self.__createColorHash()
        edgeList = []
        colList = []
        for i in self.__graph.vertices: #relax, its a self-made iterator. If you dont believe then check my linkedlist code
            for j in i.getAdjacentList(): #again, self implemented
                edgeList.append([i.getLabel(), j.vertex.getLabel(), self.__ECode.getData(j.getWeight())])
        G.add_weighted_edges_from(edgeList)
        pos = nx.planar_layout(G)
        for i in list(G.nodes): #sorry, here I had to break the rule. Its for visualising. Its optional, right? 
            colList.append(colorHash.getData(self.__graph.getVertex(i).getData()))
        plt.figure(figsize=(len(list(G.nodes))/2, len(list(G.nodes))/2))
        plt.title("Graphical Visualisation of " + self.__fileName)
        nx.draw_networkx(G, pos, with_labels = True, node_color = colList)
        labels = nx.get_edge_attributes(G,'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        
        
        legend_elements = [Line2D([0], [0], marker='o', color=i.getValue(), label=i.getKey(), markerfacecolor=i.getValue(), markersize=15) for i in colorHash.getHashArray() if i.getKey() is not None]
        #this thing had to be a list. So I had to use list convention. Again it is for visualisation. I am only taking liberty in this part and I/O part.
        plt.legend(handles=legend_elements, loc='lower right')
        plt.savefig('graph.png')
        plt.close()
        
    def __createColorHash(self):
        colorHash = DSAHash(10)
        for i in self.__NCode: #self made
            # look for better ways to create colours
            colorHash.put(i.getKey(), "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        return colorHash
    
    def __calculateCost(self, path):
        cost = 0
        for i in path:
            cost = cost + self.__NCode.getData(self.__graph.getVertex(i).getData())
        i = 0
        node = path.head
        while (i < path.getCount() - 1):
            cost = cost + self.__ECode.getData(self.__graph.getEdgeWeight(node.value, node.next.value))
            i = i + 1
            node = node.next
        return cost
        
    
    def __lookForNode(self, ndLabel):
        node = self.__graph.getVertex(ndLabel)
        if not node:
            print('this node does not exist')
        else:
            print('this node exists')
            print('(Node, value): (' + ndLabel + ', ' + str(node.getData()) + ')')
            
    def __addNode(self, ndLabel, Ncode):
        if self.__graph.hasVertex(ndLabel):
            print('The node already exists. Probably you want to update it')
        else:
            if not self.__NCode.hasKey(Ncode):
                print('this node code does not exists')
            else:
                self.__graph.addVertex(ndLabel, Ncode)
                print('\nNode added\n')
            
    def __deleteNode(self, ndLabel):
        if not self.__graph.hasVertex(ndLabel):
            print('The node does not even exists')
        else:
            self.__graph.deleteVertex(ndLabel)
            print('\nNode deleted\n')
            
    def __updateNode(self, ndLabel, Ncode):
        if not self.__graph.hasVertex(ndLabel):
            print('The node does not even exists')
        else:
            if not self.__NCode.hasKey(Ncode):
                print('this node code does not exists')
            else:
                self.__graph.getVertex(ndLabel).updateData(Ncode)
                print('\nNode Updated\n')
            
    def __lookEdge(self, ndLabel1, ndLabel2):
        node1 = self.__graph.getVertex(ndLabel1)
        node2 = self.__graph.getVertex(ndLabel2)
        if not node1 or not node2:
            print('one of the nodes do not exist. Maybe try adding the nodes first')
        else:
            if not self.__graph.isAdjacent(ndLabel1, ndLabel2):
                print('this edge do not exist')
            else:
                print('this edge exists')
                print('(from-Node, to-Node, value): (' + ndLabel1 + ', ' + ndLabel2 + ', ' + self.__graph.getEdgeWeight(ndLabel1, ndLabel2) + ')')
        
    def __addEdge(self, ndLabel1, ndLabel2, Ecode):
         node1 = self.__graph.getVertex(ndLabel1)
         node2 = self.__graph.getVertex(ndLabel2)
         if not node1 or not node2:
             print('one of the nodes do not exist. maybe add them first')
         else:
             if self.__graph.isAdjacent(ndLabel1, ndLabel2):
                 print('this edge already exist. You might want to update it')
             else:
                 if not self.__ECode.hasKey(Ecode):
                     print('this node code does not exists')
                 else:
                     self.__graph.addEdge(ndLabel1, ndLabel2, Ecode)
                     print('\n edge added\n')
                     
    def __deleteEdge(self, ndLabel1, ndLabel2):
        node1 = self.__graph.getVertex(ndLabel1)
        node2 = self.__graph.getVertex(ndLabel2)
        if not node1 or not node2:
            print('one of the nodes do not exist. maybe add them first')
                    
        else:
            if not self.__graph.isAdjacent(ndLabel1, ndLabel2):
                print('this edge does not exist so do not worry about deleting it')
            else:
                self.__graph.deleteEdge(ndLabel1, ndLabel2)
                print('\edge deleted\n')
                
    def __updateEdge(self, ndLabel1, ndLabel2, Ecode):
        node1 = self.__graph.getVertex(ndLabel1)
        node2 = self.__graph.getVertex(ndLabel2)
        if not node1 or not node2:
            print('one of the nodes do not exist. maybe add them first')
                    
        else:
            if not self.__graph.isAdjacent(ndLabel1, ndLabel2):
                print('this edge does not exist so try adding it first')
            else:
                if not self.__ECode.hasKey(Ecode):
                    print('this node code does not exists')
                else:
                    self.__graph.updateEdge(ndLabel1, ndLabel2, Ecode)
                    print('\nedge updated\n')
                    
    def __addNcode(self, Ncode, value):
        try:
            self.__NCode.put(Ncode, int(value))
            print('\nNode Code Added\n')
        except ValueError:
            print('Value of Node Code is invalid. it has to be an integer\n')
        except KeyError:
            print(' Node code is invalid as it already exists\n')
            
    def __updateNcode(self, Ncode, value):
        try:
            self.__NCode.updateData(Ncode, int(value))
            print('\nNode Code updated\n')
        except ValueError:
            print('Value of Node Code is invalid. it has to be an integer\n')
        except KeyError:
                print(' Node not found. Add it first\n')
                
    def __addEcode(self, Ecode, value):
        try:
            self.__ECode.put(Ecode, int(value))
            print('\nEdge Code Added\n')
        except ValueError:
            print('Value of Node Code is invalid. it has to be an integer\n')
        except KeyError:
            print(' Node code is invalid as it already exists\n')
        
    def __updateEcode(self, Ecode, value):
        try:
            self.__ECode.updateData(Ecode, int(value))
            print('\nEdge Code updated\n')
        except ValueError:
            print('Value of Node Code is invalid. it has to be an integer\n')
        except KeyError:
            print(' Node not found. Add it first\n')
            
    def __setStart(self, newStart):
        
        node= self.__graph.getVertex(newStart)
        if node != None:
            self.__Start = node
        else:
            print('\n enter a valid node \n')
            
    def __setTarget(self, newTarget):
        node= self.__graph.getVertex(newTarget)
        if node != None:
            self.__Target = node
        else:
            print('\n enter a valid node \n')
            
    def __displayGraph(self, f, toSave):
        matrix = self.__graph.displayMatrix()
        i = 1
        while i < len(matrix):
            j = 1
            while j < len(matrix):
                
                if matrix[i][j] != 0:
                    matrix[i][j] = self.__ECode.getData(matrix[i][j])
                j = j +1
            i = i + 1
        matrix[0][0] = '/'
        i = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix):
                
                print(matrix[i][j], end = ' ')
                if toSave == '1':
                    f.write(str(matrix[i][j]) + ' ')
                j = j +1
            print()
            if toSave == '1':
                f.write('\n')
            i = i + 1
            
    def __displayRoutes(self, number, toSave, file):
        num = 1
        if number == '-a':
            factor = True
        else:
            factor = False
            try:
                num = int(number)
            except ValueError:
                print('bad output')
                return
        count = 0
        
        while not self.__pathQueue.isEmpty() and (factor or count < num):
            qobj = self.__pathQueue.dequeue()
            if toSave == '1':
                file.write(str(qobj.getValue()) + '  ' + str(qobj.getPath()) + '\n')
            else:
                print(qobj.getValue(), qobj.getPath())
            count = count + 1
        
    
    def nodeOperations(self):
        
        #complete
        print('welcome to node operation')
        while(True):
            
            
            command = input('Choose one of the following possible operations\n1. Look for a node\n2. Add a new node\n3. delete an existing node\n4. update a node\n5. Exit Node Operations')
            if command == '5':
                return
            
            elif command == '1':
                ndLabel = input('please enter the name of the node')
                self.__lookForNode(ndLabel)
                
            elif command == '2':
                ndLabel = input('please enter the name of the node that you want to add')
                print('choose among the following NCodes')
                print(self.__NCode)
                Ncode = input()
                self.__addNode(ndLabel, Ncode)

            elif command == '3':
                ndLabel = input('please enter the name of the node that you want to delete')
                self.__deleteNode(ndLabel)

            elif command == '4':
                ndLabel = input('please enter the name of the node that you want to update')
                print('choose among the following NCodes')
                print(self.__NCode)
                Ncode = input()
                self.__updateNode(ndLabel, Ncode)
                
            else:
                print('sorry command not identified')
                                  
                
    def edgeOperations(self):
        
        #complete
        print('Welcome to edge operation')
        while(True):
            
            command = input('Choose one of the following possible operations\n1. Look for an edge\n2. Add a new edge\n3. delete an existing edge\n4. update an edge\n5. Exit Node Operations')
            if command == '5':
                    return
                
            elif command == '1':
                ndLabel1 = input('please enter the name of the from-node')
                ndLabel2 = input('please enter the name of the to-node')
                self.__lookEdge(ndLabel1, ndLabel2)
                
            elif command == '2':
                
                ndLabel1 = input('please enter the name of the from-node')
                ndLabel2 = input('please enter the name of the to-node')
                print('choose among the following NCodes')
                print(self.__ECode)
                Ecode = input()
                self.__addEdge(ndLabel1, ndLabel2, Ecode)
                
            elif command == '3':
                ndLabel1 = input('please enter the name of the from-node')
                ndLabel2 = input('please enter the name of the to-node')
                self.__deleteEdge(ndLabel1, ndLabel2)
                        
            elif command == '4':
                ndLabel1 = input('please enter the name of the from-node')
                ndLabel2 = input('please enter the name of the to-node')
                print('choose among the following ECodes')
                print(self.__ECode)
                Ecode = input()
                self.__updateEdge(ndLabel1, ndLabel2, Ecode)
            
    def parameterTweaks(self):
        print('welcome to parameter tweak')
        while True:
            command = input('You can perform following tweaks\n1. List all Node Codes\n2. List all Edge Codes\n3. Add a Node Code\n4. Update a Node Code\n5. Add an Edge Code\n6. Update an Edge Code\n7. Change start node\n8. Change target Node\n9. Go back to main menu')
            if command == '9':
                return
            
            elif command == '1':
                print('Right Now, we have following Node Codes')
                print(self.__NCode)
                
            elif command == '2':
                print('Right Now, we have following Edge Codes')
                print(self.__ECode)
            
            elif command == '3':
                Ncode = input('please enter the Node Code you want to add')
                value = input('please enter the value that you want to associate with this code')
                self.__addNcode(Ncode, value)
                
                
            elif command == '4':
                print('choose among the following Node Codes to update')
                print(self.__NCode)
                Ncode = input('enter the node code that you want to update')
                value = input('enter the value that you want to update')
                self.__updateNcode(Ncode, value)
                    
            elif command == '5':
                Ecode = input('please enter the Edge Code you want to add')
                value = input('please enter the value that you want to associate with this code')
                self.__addEcode(Ecode, value)
                    
            elif command == '6':
                print('choose among the following Ecode Codes to update')
                print(self.__ECode)
                Ecode = input('enter the node code that you want to update')
                value = input('enter the value that you want to update')
                self.__updateEcode(Ecode, value)
                    
            elif command == '7':
                newStart = input('\nPlease enter the node you want to make new starting point')
                self.__setStart(newStart)
                    
            elif command == '8':
                newTarget = input('\nPlease enter the node you want to make new target point')
                self.__setTarget(newTarget)
                
            else:
                print('\ncommand not identified\n')
                
        
    def displayGraph(self):
        #fully functional now
        toSave = False
        print('display graph')
        toSave = input('do you want to save the matrix as well?enter 0 for no and 1 for yes')
        if toSave == '1':
            file = input('please enter the name of file that you want to save into')
            f = open(file, 'w')
        else:
            f = None
        self.__displayGraph(f, toSave)
        
    def displayWorld(self):
        print('display world')
        command = input('There are three things that you can do\n1. Display information about features\n2. Save information about features\n3. Save a visual representation of the world')
        if command == '1':
            print('\n\n\n' + '-'*20)
            print('The world has ' + str(self.__graph.getVertexCount()) + ' Nodes\n')
            for i in self.__graph.vertices: #self made iterator
                print(i.getLabel(), i.getData())
                
            print('\n' + '-'*20 + '\n')
            
            print('The world has ' + str(self.__graph.getEdgeCount()) + ' Edges\n')
            for i in self.__graph.vertices: #self made iterator
                for j in i.getAdjacentList(): #self made iterator
                    print(i.getLabel(), j.vertex.getLabel(), j.getWeight())
            
            print('\n' + '-'*20 + '\n')
            print('The world has following NCodes:\n')
            print(self.__NCode)
            print('\n' + '-'*20 + '\n')
            print('The world has following ECodes:\n')
            print(self.__ECode)
        
        if command == '2':
            filename = input('please enter the name of file in which you want to save information')
            file = open(filename, 'w')
            file.write('The world has ' + str(self.__graph.getVertexCount()) + ' Nodes\n')
            for i in self.__graph.vertices: #self made iterator
                file.write(i.getLabel() + ' ' + i.getData() + '\n')
                
            file.write('\n' + '-'*20 + '\n')
            
            file.write('The world has ' + str(self.__graph.getEdgeCount()) + ' Edges\n')
            for i in self.__graph.vertices: #self made iterator
                for j in i.getAdjacentList(): #self made iterator
                    file.write(i.getLabel() + ' ' + j.vertex.getLabel() + ' ' + j.getWeight() + '\n')
                    
            file.write('\n' + '-'*20 + '\n')
            file.write('The world has following NCodes:\n')
            for i in self.__NCode: #self made iterator
                    file.write(i.getKey() + ' ' + str(i.getValue()) + '\n')
            file.write('\n' + '-'*20 + '\n')
            file.write('The world has following ECodes:\n')
            for i in self.__ECode: #self made iterator
                    file.write(i.getKey() + ' ' + str(i.getValue()) + '\n')
                    
        if command == '3':
            self.__visualise()
    

    def generateRoutes(self):
        print('generate Route')
        self.__pathList = self.__graph.findPaths(self.__Start, self.__Target)
        for i in self.__pathList:
            cost = self.__calculateCost(i)
            self.__pathQueue.enqueue(cost, i)
        
    def displayRoutes(self):
        print('display routes')
        
        number = input('How many top routes you want to display? \nplease enter an integer.\nenter -a to display all paths')
        toSave = input('do you want to save the matrix as well?enter 0 for no and 1 for yes')
        if toSave == '1':
            fname = input('please enter the name of the file where you want to save')
            file = open(fname, 'w')
        else:
            file = None
        self.__displayRoutes(number, toSave, file)
            
        
    def saveNetwork(self):
        print('save network')
        filename = input('\nplease enter the name of file')
        with open(filename, "wb") as f:
                pickle.dump(self, f)
        
    def Play(self, outfile):
        file = open(outfile, 'w')
        self.generateRoutes()
        while not self.__pathQueue.isEmpty():
            qobj = self.__pathQueue.dequeue()
            file.write(str(qobj.getValue()) + '  ' + str(qobj.getPath()) + '\n')
        