#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:13:47 2021

@author: pradyumna agrawal
"""
from DSAHash import DSAHash
from DSAGraphWithEdge import DSAGraph

class Game():
    
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__NCode = DSAHash(10)
        self.__ECode = DSAHash(10)
        self.__graph = self.__makeGraph()
        
    def __makeGraph(self):
        #fully functional now
        Start = False
        Target = False
        file = open(self.__fileName, 'r')
        data = file.readlines()
        if len(data) == 0:
            raise ValueError("file is empty")
        graph = DSAGraph()
        for idx, i in enumerate(data):
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
        
    def nodeOperations(self):
        
        #complete
        print('welcome to node operation')
        while(True):
            command = input('Choose one of the following possible operations\n1. Look for a node\n2. Add a new node\n3. delete an existing node\n4. update a node\n5. Exit Node Operations')
            if command == '5':
                return
            elif command == '1':
                ndLabel = input('please enter the name of the node')
                node = self.__graph.getVertex(ndLabel)
                if not node:
                    print('this node does not exist')
                else:
                    print('this node exists')
                    print('(Node, value): (' + ndLabel + ', ' + str(node.getData()) + ')')
                    
            elif command == '2':
                ndLabel = input('please enter the name of the node that you want to add')
                if self.__graph.hasVertex(ndLabel):
                    print('The node already exists. Probably you want to update it')
                else:
                    print('choose among the following NCodes')
                    print(self.__NCode)
                    Ncode = input()
                    if not self.__NCode.hasKey(Ncode):
                        print('this node code does not exists')
                    else:
                        self.__graph.addVertex(ndLabel, Ncode)
                        print('\nNode added\n')
                    
            elif command == '3':
                ndLabel = input('please enter the name of the node that you want to delete')
                if not self.__graph.hasVertex(ndLabel):
                    print('The node does not even exists')
                else:
                    self.__graph.deleteVertex(ndLabel)
                    print('\nNode deleted\n')
            
            elif command == '4':
                ndLabel = input('please enter the name of the node that you want to update')
                if not self.__graph.hasVertex(ndLabel):
                    print('The node does not even exists')
                else:
                    print('currently Node Code at vertex ' + ndLabel + ' is ' + self.__graph.getVertex(ndLabel).getData())
                    print('choose among the following NCodes')
                    print(self.__NCode)
                    Ncode = input()
                    if not self.__NCode.hasKey(Ncode):
                        print('this node code does not exists')
                    else:
                        self.__graph.getVertex(ndLabel).updateData(Ncode)
                        print('\nNode Updated\n')
                        
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
                node1 = self.__graph.getVertex(ndLabel1)
                ndLabel2 = input('please enter the name of the to-node')
                node2 = self.__graph.getVertex(ndLabel2)
                
                if not node1 or not node2:
                    print('one of the nodes do not exist. Maybe try adding the nodes first')
                else:
                    if not self.__graph.isAdjacent(ndLabel1, ndLabel2):
                        print('this edge do not exist')
                    else:
                        print('this edge exists')
                        print('(from-Node, to-Node, value): (' + ndLabel1 + ', ' + ndLabel2 + ', ' + self.__graph.getEdgeWeight(ndLabel1, ndLabel2) + ')')
        
            elif command == '2':
                
                ndLabel1 = input('please enter the name of the from-node')
                node1 = self.__graph.getVertex(ndLabel1)
                ndLabel2 = input('please enter the name of the to-node')
                node2 = self.__graph.getVertex(ndLabel2)
                
                if not node1 or not node2:
                    print('one of the nodes do not exist. maybe add them first')
                else:
                    if self.__graph.isAdjacent(ndLabel1, ndLabel2):
                        print('this edge already exist. You might want to update it')
                    else:
                        print('choose among the following NCodes')
                        print(self.__ECode)
                        Ecode = input()
                        if not self.__ECode.hasKey(Ecode):
                            print('this node code does not exists')
                        else:
                            self.__graph.addEdge(ndLabel1, ndLabel2, Ecode)
                            print('\n edge added\n')
                            
            elif command == '3':
                ndLabel1 = input('please enter the name of the from-node')
                node1 = self.__graph.getVertex(ndLabel1)
                ndLabel2 = input('please enter the name of the to-node')
                node2 = self.__graph.getVertex(ndLabel2)
                
                if not node1 or not node2:
                    print('one of the nodes do not exist. maybe add them first')
                    
                else:
                    if not self.__graph.isAdjacent(ndLabel1, ndLabel2):
                        print('this edge does not exist so do not worry about deleting it')
                    else:
                        self.__graph.deleteEdge(ndLabel1, ndLabel2)
                        print('\edge deleted\n')
                        
            elif command == '4':
                ndLabel1 = input('please enter the name of the from-node')
                node1 = self.__graph.getVertex(ndLabel1)
                ndLabel2 = input('please enter the name of the to-node')
                node2 = self.__graph.getVertex(ndLabel2)
                
                if not node1 or not node2:
                    print('one of the nodes do not exist. maybe add them first')
                    
                else:
                    if not self.__graph.isAdjacent(ndLabel1, ndLabel2):
                        print('this edge does not exist so try adding it first')
                    else:
                        print('currently Edge Code at edge ' + ndLabel1 + '  ' + ndLabel2 + 'is ' + self.__graph.getEdgeWeight(ndLabel1, ndLabel2))
                        print('choose among the following ECodes')
                        print(self.__ECode)
                        Ecode = input()
                        if not self.__ECode.hasKey(Ecode):
                            print('this node code does not exists')
                        else:
                            self.__graph.updateEdge(ndLabel1, ndLabel2, Ecode)
                            print('\nedge updated\n')
                        
                
            
            
    def parameterTweaks(self):
        print('welcome to parameter tweak')
        while True:
            command = input('You can perform following tweaks\n1. List all Node Codes\n2. List all Edge Codes\n3. Add a Node Code\n4. Update a Node Code\n5. Add an Edge Code\n6. Update an Edge Code\n7. Go back to main menu')
            if command == '7':
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
                try:
                    self.__NCode.put(Ncode, int(value))
                    print('\nNode Code Added\n')
                except ValueError:
                    print('Value of Node Code is invalid. it has to be an integer\n')
                except KeyError:
                    print(' Node code is invalid as it already exists\n')
                
                
            elif command == '4':
                print('choose among the following Node Codes to update')
                print(self.__NCode)
                Ncode = input('enter the node code that you want to update')
                value = input('enter the value that you want to update')
                try:
                    self.__NCode.updateData(Ncode, int(value))
                    print('\nNode Code updated\n')
                except ValueError:
                    print('Value of Node Code is invalid. it has to be an integer\n')
                except KeyError:
                    print(' Node not found. Add it first\n')
                    
            elif command == '5':
                Ecode = input('please enter the Edge Code you want to add')
                value = input('please enter the value that you want to associate with this code')
                try:
                    self.__ECode.put(Ecode, int(value))
                    print('\nEdge Code Added\n')
                except ValueError:
                    print('Value of Node Code is invalid. it has to be an integer\n')
                except KeyError:
                    print(' Node code is invalid as it already exists\n')
                    
            elif command == '6':
                print('choose among the following Ecode Codes to update')
                print(self.__ECode)
                Ecode = input('enter the node code that you want to update')
                value = input('enter the value that you want to update')
                try:
                    self.__ECode.updateData(Ecode, int(value))
                    print('\nEdge Code updated\n')
                except ValueError:
                    print('Value of Node Code is invalid. it has to be an integer\n')
                except KeyError:
                    print(' Node not found. Add it first\n')
                    
            else:
                print('\ncommand not identified\n')
                
                
                
        
        
    def displayGraph(self):
        #fully functional now
        toSave = False
        print('display graph')
        toSave = input('do you want to save the matrix as well?enter 0 for no and 1 for yes')
        if toSave == '1':
            toSave = True
        if toSave == True:
            file = input('please enter the name of file that you want to save into')
            f = open(file, 'w')
        matrix = self.__graph.displayMatrix()
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix)):
                if matrix[i][j] != 0:
                    matrix[i][j] = self.__ECode.getData(matrix[i][j])
        matrix[0][0] = '/'
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print(matrix[i][j], end = ' ')
                if toSave == True:
                    f.write(str(matrix[i][j]) + ' ')
            print()
            if toSave == True:
                f.write('\n')
        
    def displayWorld(self):
        print('display world')
        
    def generateRoutes(self):
        print('generate Route')
        
    def displayRoutes(self):
        print('display routes')
        
    def saveNetwork(self):
        print('save network')
        
    def Play(self, outfile):
        self.__outFile = outfile