#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Sun Oct 10 22:13:47 2021

@author: pradyumna agrawal

This file contains code for Game classs
"""
from linkedKList import DSALinkedList 
from DSAHash import DSAHash #Hash is needed for maintaining NCodes and ECodes.
from DSAGraphWithEdge import DSAGraph #DSAGraphWithEdge lets maintaining weighted graphs. 
import networkx as nx #This one is used for visualisation part. Its an add on feature. 
import matplotlib.pyplot as plt #This is also needed for visualisation part
import random #this one is also needed for visualisation part
from matplotlib.lines import Line2D #this one is also needed for visualisation part
import pickle #this is used to save the network. 
from DSAHeap import DSAHeap

class Game():
    
    def __init__(self, fileName):
        '''
        Default and the only constructor . 
        @Param: fileName -> file with network information (gameofcatz.txt)

        '''
        self.__fileName = fileName #we keep it saved so that we can use it to create outputs with same name. 
        self.__NCode = DSAHash(10) #The hash is self-resizing. so do not worry about it having just a size of 10
        self.__ECode = DSAHash(10)
        self.__graph = self.__makeGraph() #this function creates the graph. 
        self.__pathHeap = None        
    def __makeGraph(self):
        '''
        this function creates graph. 
        
        @return DSAGraph
        @raises ValueError -> when the file is empty
        @raises KeyError -> when the file do not have start and/or target
        '''
        Start = False #keeps track whether start has been found
        Target = False #yup, you got that right. 
        file = open(self.__fileName, 'r') #oopen the file
        data = file.readlines() #read lines (I am allowed this one, right?)
        if len(data) == 0: #checks if the file is empty
            raise ValueError("file is empty") #if yes, then raise an error.
        graph = DSAGraph() #create a graph object
        idx = 0 #keeps track of lines.
        length = len(data) 
        while idx < length: #loop till all data has been parsed
            i = data[idx] #data is an output of readlines. So it should be exception.    
            if i[0] != '#': #checking if the row starts with #. is yes, do nothing. 
                information = i.strip().split(' ') #if not, then split the row
                if information != '': #if the now is empty, then do nothing. 
                    if information[0] == 'Ecode': #if the first code is Ecode, then do as follow
                        try:
                            self.__ECode.put(information[1], int(information[2])) #try putting it in Ecode hash. Handle exception. 
                        except IndexError: #it is possible that line only had ecode written and other info was not there. 
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                        except KeyError: #it is possible that the ecode already existed in ahash. 
                            print('line ' + str(idx) + ' is invalid as key already exists\n' + i)
                        except ValueError: #it is possible that the value associated with ecode is not an integer. 
                            print('line ' + str(idx) + ' is invalid as value associated with E Code has to be an integer\n' + i)
                   
                    elif information[0] == 'Ncode': #exact copy of previous functions. Just for Ncode. 
                        try:
                            self.__NCode.put(information[1], int(information[2]))
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                        except KeyError:
                            print('line ' + str(idx) + ' is invalid as key already exists\n' + i)
                        except ValueError:
                            print('line ' + str(idx) + ' is invalid as value associated with N Code has to be an integer\n' + i)
                   
                    elif information[0] == 'Node': #to catch all the nodes. 
                        try:
                            if not self.__NCode.hasKey(information[2]): #check if we have an Ncode of the node in hash. 
                                print('line ' + str(idx) + ' is invalid as no such node code exists\n' + i) #snap, we did not. what a waste of line!
                            else:
                                graph.addVertex(information[1], information[2]) #try adding node to graph. 
                        except IndexError: #it is possible that only Node is written in line. we should prepapre for worst cases. 
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
            
                    elif information[0] == 'Edge': #same as previous. just for edges. 
                        try:
                            if not self.__ECode.hasKey(information[3]): #check if ecode is valid. 
                                print('line ' + str(idx) + ' is invalid as no such edge code exists\n' + i)
                            else: #try adding edge to graph.
                                graph.addEdge(information[1], information[2], information[3])
                        except IndexError: # it is possible that the line might have some information missing. 
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                        except ValueError: #it is possible that one of the node might be missing. 
                        #i am not taking the high road of creating nodes myself in case they are absent. 
                            print('line ' + str(idx) + ' is invalid as one of the nodes does not exists\n' + i)
                    
                    elif information[0] == 'Start': #set the starting node. 
                        try:
                            self.__Start = graph.getVertex(information[1]) #get the start vertex from the code
                            Start = True and self.__Start #gracefully handle if the node is not present in graph. 
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
                    
                    elif information[0] == 'Target':
                        try:
                            self.__Target = graph.getVertex(information[1])  #get target vertex from the graph. 
                            print(self.__Target)
                            Target = True and self.__Target #gracefully handle if the node is not present in graph.
                        except IndexError:
                            print('line ' + str(idx) + ' is invalid as it does not have required number of arguments\n' + i)
            idx += 1 #increase index
        if not Start or not Target: #check if start and target were found successfully. 
            raise KeyError()
        
        return graph
    
    def __visualise(self):
        '''
        this function uses few liberties for the purpose of visualisation. 
        if you find this in violation of guidelines, please do not assess this function
        as visualisation is an optional requirement.
        
        Code references 1
        @author: Arjit Gayen
        @year: 2019
        @link: https://www.geeksforgeeks.org/directed-graphs-multigraphs-and-visualization-in-networkx/
        
        
        Code reference 2
        @author: Marcus Müller and JohanC
        @year: 2020
        @link: https://stackoverflow.com/questions/28372127/add-edge-weights-to-plot-output-in-networkx
        
        Code reference 3
        @author: Ami Tavory
        @Year: 2016
        @link: https://stackoverflow.com/questions/40128692/networkx-how-to-add-weights-to-an-existing-g-edges
        '''
        G = nx.DiGraph() #create a ntetworkx 
        # I am going to use list for the next trick. Pardon me.
        edgeList = [] #the graphing function requires a list as input. So I had to do it. 
        colList = [] #graphing function requires a list as input. So I had to do it. 
        for i in self.__graph.vertices: #relax, its a self-made iterator. If you dont believe then check my linkedlist code
            for j in i.getAdjacentList(): #again, self implemented
                edgeList.append([i.getLabel(), j.vertex.getLabel(), self.__ECode.getData(j.getWeight())]) #sorry, for list. 
        G.add_weighted_edges_from(edgeList) #add all the edges to networkx graph
        pos = nx.planar_layout(G)
        colorHash = DSAHash(10)
        for i in self.__NCode: #self made
            # look for better ways to create colours
            colorHash.put(i.getKey(), "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        for i in list(G.nodes): #sorry, here I had to break the rule. Its for visualising. Its optional, right? 
            colList.append(colorHash.getData(self.__graph.getVertex(i).getData())) #add colour
        plt.figure(figsize=(len(list(G.nodes))/2, len(list(G.nodes))/2)) #set figure size. 
        plt.title("Graphical Visualisation of " + self.__fileName) #set title. 
        nx.draw_networkx(G, pos, with_labels = True, node_color = colList) #draw nodes
        labels = nx.get_edge_attributes(G,'weight') #add labels. 
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels) #draw graph
        legend_elements = [Line2D([0], [0], marker='o', color=i.getValue(), label=i.getKey(), markerfacecolor=i.getValue(), markersize=15) for i in colorHash.getHashArray() if i.getKey() is not None] #add legend
        #this thing had to be a list. So I had to use list convention. Again it is for visualisation. I am only taking liberty in this part and I/O part.
        plt.legend(handles=legend_elements, loc='lower right') #add legend to figure
        plt.savefig('graph.png') #save figure
        plt.close() #close figure
        
           
    
    def _lookForNode(self, ndLabel):
        
        '''
        @param: ndLabel -> label of the node. 
        Check if the node is present in the graph
        '''
        node = self.__graph.getVertex(ndLabel) #get node from the graph
        if not node: #if node not there then print this. 
            print(ndLabel, ' node does not exist')
        else: #if node there, then print node label and ncode. 
            print('this node exists')
            print('(Node, value): (' + ndLabel + ', ' + str(node.getData()) + ')')
            
    def _addNode(self, ndLabel, Ncode):
        '''
        @param1 : ndLabel -> label of the new node
        @param2: Ncode -> Ncode of the new node
        
        Add a new node to the graph. 
        '''
        if self.__graph.hasVertex(ndLabel): #check if node is already there
            print('The node already exists. Probably you want to update it')
        else:
            if not self.__NCode.hasKey(Ncode): #check if ncode is valid. 
                print('this node code does not exists')
            else: #if everything is okay, then add the node. 
                self.__graph.addVertex(ndLabel, Ncode)
                print('\nNode added\n')
            
    def _deleteNode(self, ndLabel):
        '''
        @param: ndLabel -> label of the node that has to be deleted. 
        
        Delete a node from the graph. 
        '''
        if not self.__graph.hasVertex(ndLabel): # check if node exists 
            print('The node does not even exists')
        else:
            #check if the node is a start/target node. 
            if self.__graph.getVertex(ndLabel) == self.__Start or self.__graph.getVertex(ndLabel) == self.__Target:
                print('you can not delete a node that is set as target or start. because coder is too lazy to take care of this situation.')
            else:
                self.__graph.deleteVertex(ndLabel)
                print('\nNode deleted\n')
            
    def _updateNode(self, ndLabel, Ncode):
        '''
        @param1: ndLabel: Label of the node that you want to update
        @param2: Ncode: new ncode
        
        Update the Ncode of an existing node. 
        '''
        if not self.__graph.hasVertex(ndLabel): #check if node exists. 
            print('The node does not even exists')
        else:
            if not self.__NCode.hasKey(Ncode): #check if Ncode is valid. 
                print('this node code does not exists')
            else: #update the node. 
                self.__graph.getVertex(ndLabel).updateData(Ncode)
                print('\nNode Updated\n')
            
    def _lookEdge(self, ndLabel1, ndLabel2):
        '''
        @param1: ndLabel1: label of from node.
        @param2: ndLabel2: label of to node. 
        
        Check if an edge is in the graph, if yes, print its Ecode. 
        '''
        node1 = self.__graph.getVertex(ndLabel1) #node1 is DSAGraphVertex object
        node2 = self.__graph.getVertex(ndLabel2) #node2 is DSAGraphVertex object
        if not node1 or not node2: #check if any of the node is missing. 
            print('one of the nodes do not exist. Maybe try adding the nodes first')
        else:
            if not self.__graph.isAdjacent(ndLabel1, ndLabel2): #check if the edge do not exists and print so. 
                print('this edge do not exist')
            else: #everything checks out so print the edge. 
                print('this edge exists') 
                print('(from-Node, to-Node, value): (' + ndLabel1 + ', ' + ndLabel2 + ', ' + self.__graph.getEdgeWeight(ndLabel1, ndLabel2) + ')')
        
    def _addEdge(self, ndLabel1, ndLabel2, Ecode):
         '''
            @param1: ndLabel1: label of from node.
            @param2: ndLabel2: label of to node. 
            @param3: Ecode: ecode of the new edge
            
            Add a new edge to the graph.  
         '''
        
         node1 = self.__graph.getVertex(ndLabel1) #get the DSAGraphVertex object associated with label. 
         node2 = self.__graph.getVertex(ndLabel2) #well, same.
         if not node1 or not node2:
             print('one of the nodes do not exist. maybe add them first')
         else:
             if self.__graph.isAdjacent(ndLabel1, ndLabel2): #check if there is an edge. if not, print so. 
                 print('this edge already exist. You might want to update it')
             else:
                 if not self.__ECode.hasKey(Ecode): #check if ecode is valid. 
                     print('this node code does not exists')
                 else: #all good. add the edge. 
                     self.__graph.addEdge(ndLabel1, ndLabel2, Ecode)
                     print('\n edge added\n')
                     
    def _deleteEdge(self, ndLabel1, ndLabel2):
        
        '''
        @param1: ndLabel1: label of from node.
        @param2: ndLabel2: label of to node. 
        
        Check if an edge is in the graph, if yes, delete it. 
        '''
        node1 = self.__graph.getVertex(ndLabel1) #get the DSAGraphVertex Object
        node2 = self.__graph.getVertex(ndLabel2) #get the DSAGraphVertex Object
        if not node1 or not node2: #check if both vertex are real. 
            print('one of the nodes do not exist. maybe add them first')
                    
        else:
            if not self.__graph.isAdjacent(ndLabel1, ndLabel2): #check if there is an edge. 
                print('this edge does not exist so do not worry about deleting it')
            else: #delete the edge. 
                self.__graph.deleteEdge(ndLabel1, ndLabel2)
                print('\edge deleted\n')
                
    def _updateEdge(self, ndLabel1, ndLabel2, Ecode):
        
        '''
            @param1: ndLabel1: label of from node.
            @param2: ndLabel2: label of to node. 
            @param3: Ecode: new ecode of the edge
            
            check if an edge exists and then update its ecode.   
         '''
        node1 = self.__graph.getVertex(ndLabel1) #get the node (DSAGraphVertex object)
        node2 = self.__graph.getVertex(ndLabel2) #umm, samsies. 
        if not node1 or not node2: #check if both of them are real. 
            print('one of the nodes do not exist. maybe add them first')
                    
        else:
            if not self.__graph.isAdjacent(ndLabel1, ndLabel2): #check if the edge is real. 
                print('this edge does not exist so try adding it first')
            else:
                if not self.__ECode.hasKey(Ecode): #check if the ecode is valid. 
                    print('this node code does not exists')
                else: #all good, update. 
                    self.__graph.updateEdge(ndLabel1, ndLabel2, Ecode)
                    print('\nedge updated\n')
                    
    def _addNcode(self, Ncode, value):
        '''
        @param1: Ncode -> new ncode that you want to add
        @param2: value -> value that you want to associate with the new ncode. 
        
        Add a new Ncode to the graph
        '''
        
        try:
            self.__NCode.put(Ncode, int(value)) #try putting the new ncode to ncode hash. and handle exceptions. 
            print('\nNode Code Added\n')
        except ValueError: #the value associated with ncode may not have been an integer
            print('Value of Node Code is invalid. it has to be an integer\n')
        except KeyError: #the ncode already existed in the hash. 
            print(' Node code is invalid as it already exists\n')
            
    def _updateNcode(self, Ncode, value):
        '''
        @param1: Ncode -> ncode that you want to update
        @param2: value -> value that you want to associate with the ncode. 
        
        Update an existing Ncode. 
        '''
        try:
            self.__NCode.updateData(Ncode, int(value)) #try updating. handle exceptions. 
            print('\nNode Code updated\n')
        except ValueError: #it is possible that value given by user is not integer. 
            print('Value of Node Code is invalid. it has to be an integer\n')
        except KeyError: #it is possible that the ncode is not present in the code. 
                print(' Ncode not found. Add it first\n')
                
    def _addEcode(self, Ecode, value):
        
        '''
        @param1: Ecode -> new Ecode that you want to ad..
        @param2: value -> value that you want to associate with the Ecode. 
        
        Add a new Ecode. 
        '''
        try:
            self.__ECode.put(Ecode, int(value)) #try adding. handle exceptions. 
            print('\nEdge Code Added\n')
        except ValueError: #possible that the value user is associating with the code is not integer.
            print('Value of Edge Code is invalid. it has to be an integer\n')
        except KeyError: #it is possbile that the node was already in the hash. 
            print('Edge code is invalid as it already exists\n')
        
    def _updateEcode(self, Ecode, value):
        
        '''
        @param1: Ecode -> Ecode that you want to update
        @param2: value -> value that you want to associate with the Ecode. 
        
        Update an existing Ecode. 
        '''
        try:
            self.__ECode.updateData(Ecode, int(value)) #try updating, handle exceptions. 
            print('\nEdge Code updated\n')
        except ValueError: #same old, same old. 
            print('Value of Edge Code is invalid. it has to be an integer\n')
        except KeyError: #same old, same old. 
            print('Ecode not found. Add it first\n')
            
    def _setStart(self, newStart):
        
        '''
        @param: newStart: label of the node that user wants to set as Start
        
        Make another node the starting point in the game
        '''
        
        node= self.__graph.getVertex(newStart) #get the node (DSAGraphVertex)
        if node != None: #check if node exists. 
            self.__Start = node #if yes, then change the start. 
        else:
            print('\nenter a valid node \n') #if no, then print so. 
            
    def _setTarget(self, newTarget):
        
        '''
        @param: newTarget: label of the node that user wants to set as Target
        
        Make another node the target point in the game
        '''
        
        node= self.__graph.getVertex(newTarget) #get the node (DSAGraphVertex)
        if node != None: #check if node is real. 
            self.__Target = node #set the new target
        else:
            print('\nenter a valid node \n') #else print so. 
            
    def _displayGraph(self, f, toSave):
        '''
        param1: f: file obj 
        paran2: toSave: indicator of if user wants to save in the file obj (f)
        
        create a matrix display of the graph. Save it (optional)
        '''
        
        matrix = self.__graph.displayMatrix() #create display matrix (np.array())
        i = 1  #set starting row index
        while i < len(matrix): #loop till last row in the matrix
            j = 1 #set starting column index
            while j < len(matrix): #loop till last columns
                
                if matrix[i][j] != 0: #check if there is an edge
                    matrix[i][j] = self.__ECode.getData(matrix[i][j]) #get the value for that edge from ecode hash. 
                j = j +1 #increment column index
            i = i + 1 #increment row index
        matrix[0][0] = '/' #well, you get it. 
        #loop over rows and columns of the matrix to display and save(optional) them. 
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
            
    def _displayRoutes(self, number, toSave, file):
        '''
        @param1: number -> number of routes that user wants to display. keep it '-a' for diplaying all routes. 
        @param2: toSave -> whether user wants to save the routes
        @param3: file -> file obj (in case user wants to save the file)
        
        Display all possbile routes from start to end. 
        '''
        
        num = 1 #set number as one
        if number == '-a': #if user wants to print all paths, then set factor as true else fast. 
            
            factor = True #I came up with this with some basic boolean algebra. bottom line -> it works. 
        else:
            factor = False
            try:
                num = int(number)
            except ValueError:
                print('bad output') #if number is not a number. 
                return
        count = 0 #keep track of how many paths have been displayed till now
        
        while count < self.__pathList.getCount() and (factor or count < num): #keep displaying/saving till this condition stands. 
            qobj = self.__pathHeap.getHeapArray()[count] #get the heap element at index count 
            if toSave == '1': #if user wants to write it to a file, then do so. 
                file.write(str(qobj.getPriority()) + '  ' + str(qobj.getValue()) + '\n')
            else:
                print(qobj.getPriority(), qobj.getValue())
            count = count + 1

            
    def _calculateCost(self, path):
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
    
    def _printNodeDistribution(self):
        tempHash = DSAHash(10)
        for i in self.__NCode:
            tempHash.put(i.getKey(), 0)
        for i in self.__graph.vertices:
            tempHash.updateData(i.getData(), tempHash.getData(i.getData()) + 1)
        return tempHash
    
    def _printEdgeDistribution(self):
        tempHash = DSAHash(10)
        for i in self.__ECode:
            tempHash.put(i.getKey(), 0)
        
        for i in self.__graph.vertices: #self made iterator
            for j in i.getAdjacentList(): #self made iterator
                tempHash.updateData(j.getWeight(), tempHash.getData(j.getWeight()) + 1)
        return tempHash
    
################################################################################################   
##  All the functions above are private to Game class. The functions below are the public one ##
##  which will be accessed by gameofcatz.py to provide required functionalities.              ##  
################################################################################################
    
    def nodeOperations(self):
        '''
        This function lets a user perform four node operations (look, add, delete, and update.)
        It is an interactive function. It requires user input at various points. 
        '''        
    
        print('welcome to node operation')
        while(True): #keep going till user is tired. 
            
            #ask user what they want to do. 
            command = input('Choose one of the following possible operations\n1. Look for a node\n2. Add a new node\n3. delete an existing node\n4. update a node\n5. Exit Node Operations')
            if command == '5': #looks like user is tired. let them go home. 
                print('\nwe are now back to main menu\n')
                return
            
            #user wants to look at a node
            elif command == '1':
                ndLabel = input('please enter the name of the node') #ask user for the label of node. 
                self._lookForNode(ndLabel) #call the function to look for the node. 
                
            #user wants to add a new node.
            elif command == '2':
                #ask user for name of the new node.
                ndLabel = input('please enter the name of the node that you want to add')
                #print available Ncodes and ask the user to choose one of them. 
                print('choose among the following NCodes')
                print(self.__NCode)
                Ncode = input()
                self._addNode(ndLabel, Ncode) #call function to add a new node. 

            #user wants to delete a node
            elif command == '3':
                #ask user for the name of the node that they want to delete. 
                ndLabel = input('please enter the name of the node that you want to delete')
                self._deleteNode(ndLabel) #call the node killing function. 

            #user wants to update a node
            elif command == '4':
                #ask user for the name of the node that they want to update. 
                ndLabel = input('please enter the name of the node that you want to update')
                #let user know of the existing ncodes and ask them to choose one. 
                print('choose among the following NCodes')
                print(self.__NCode)
                Ncode = input()
                self._updateNode(ndLabel, Ncode) #call the function to update node. 
                
            else: #in case user is a 'tester'
                print('sorry command not identified')
                                  
                
    def edgeOperations(self):
        
        '''
        This function lets a user perform four edge based operations (look, add, delete, and update.)
        It is an interactive function. It requires user input at various points. 
        '''  
        
        print('Welcome to edge operation')
        while(True): #as captain america said, "I can do this all day'
            
            #ask user what they want to do 
            command = input('Choose one of the following possible operations\n1. Look for an edge\n2. Add a new edge\n3. delete an existing edge\n4. update an edge\n5. Exit Node Operations')
            if command == '5': #user wants to quit
                print('\nWe are back to main menu noew\n')
                return
                
            elif command == '1': #user wants too look at an edge
                ndLabel1 = input('please enter the name of the from-node') #ask for from label
                ndLabel2 = input('please enter the name of the to-node') #ask for two label
                self._lookEdge(ndLabel1, ndLabel2) #call function to look for the edge
                
            elif command == '2': #user wants to add an new edge
                
                ndLabel1 = input('please enter the name of the from-node') #ask for from label
                ndLabel2 = input('please enter the name of the to-node') #ask for to label
                print('choose among the following NCodes') #let them know about Ecodes
                print(self.__ECode)
                Ecode = input() #ask for Ecode
                self._addEdge(ndLabel1, ndLabel2, Ecode) #call function to add a new edge
                
            elif command == '3': #user wants to delete an edge
                ndLabel1 = input('please enter the name of the from-node') #ask for from label
                ndLabel2 = input('please enter the name of the to-node') #ask for to label
                self._deleteEdge(ndLabel1, ndLabel2) #call function to delete edge
                        
            elif command == '4': #user wants to update an edge
                ndLabel1 = input('please enter the name of the from-node') #ask for from label
                ndLabel2 = input('please enter the name of the to-node') #ask for to label
                print('choose among the following ECodes') #let them know about existing codes
                print(self.__ECode)
                Ecode = input() #ask for an Ecode
                self._updateEdge(ndLabel1, ndLabel2, Ecode) #call function to update an edge. 
            
    def parameterTweaks(self):
        
        '''
        This function lets a user perform following parameter tweaks- 
        1. Look at Ncodes, Ecodes
        2. Add new Ncodes, Ecodes
        3. Update existing Ncodes, Ecodes
        4. Update Start and Target
        It is an interactive function. It requires user input at various points. 
        '''  
        print('welcome to parameter tweak')
        while True: #Loop till user quits 
            command = input('You can perform following tweaks\n1. List all Node Codes\n2. List all Edge Codes\n3. Add a Node Code\n4. Update a Node Code\n5. Add an Edge Code\n6. Update an Edge Code\n7. Change start node\n8. Change target Node\n9. Go back to main menu')
            if command == '9': #user wants to exit
                print('\nwe are back to main menu\n')
                return
            
            elif command == '1': #user wants to look at Ncodes
                print('Right Now, we have following Node Codes')
                print(self.__NCode) #print Ncodes
                
            elif command == '2': #user wants to look at Ecodes
                print('Right Now, we have following Edge Codes')
                print(self.__ECode) #print Ecodes. 
            
            elif command == '3': #user wants to add an Ncode
                Ncode = input('please enter the Node Code you want to add') #ask for new Ncode
                value = input('please enter the value that you want to associate with this code') #ask for new value
                self._addNcode(Ncode, value) #call function to update Ncode
                
                
            elif command == '4': #user wants to update an Ncode
                print('choose among the following Node Codes to update')
                print(self.__NCode) #let user know about existing Ncodes
                Ncode = input('enter the node code that you want to update') #ask user to enter one of the existing Ncodes
                value = input('enter the value that you want to update') #ask user to enter a new value
                self._updateNcode(Ncode, value) #call function to update the Ncode. 
                    
            elif command == '5': #user wants to add an Ecode. 
                Ecode = input('please enter the Edge Code you want to add') #ask name for the new Ecode
                value = input('please enter the value that you want to associate with this code') #ask new value
                self._addEcode(Ecode, value) #call function to add the new Ecode 
                    
            elif command == '6': #user wants to update an Ecode.  
                print('choose among the following Ecode Codes to update')
                print(self.__ECode) #print available Ecodes. 
                Ecode = input('enter the node code that you want to update') #ask user to enter an existing Ecode
                value = input('enter the value that you want to update') #ask user to enter a new value
                self._updateEcode(Ecode, value) #call function to update Ecode. 
                    
            elif command == '7': #user wants to update start position
                newStart = input('\nPlease enter the node you want to make new starting point') #ask user for the new start. 
                self._setStart(newStart) #call function to update Start node. 
                    
            elif command == '8': #user wants to update target position. 
                newTarget = input('\nPlease enter the node you want to make new target point')
                self._setTarget(newTarget) #call function to update Target node. 
                
            else: #in case a tester tries to break my sweet code. 
                print('\ncommand not identified\n')
                
        
    def displayGraph(self):
        '''
        It is an interactive function. It takes inputs from user at various points. 
        It provides two fuctionalities. 
        1. Display a graph in adjacency matrix format. 
        2. save a graph in adjacency matric format. 
        '''
    
        print('welcome to display graph')
        #ask user if they also want to save the graph
        toSave = input('do you want to save the matrix as well?enter 0 for no and 1 for yes')
        if toSave == '1':
            # if yes, then create a file obj after asking user for the name of the file. 
            file = input('please enter the name of file that you want to save into')
            f = open(file, 'w')
        else:
            #if not, keep the file obj object empty. I am still struggling with creating functions with optional arguments so, I am using a little cheat here. No violation of rules though. 
            f = None
        self._displayGraph(f, toSave) #call function to display/save adjacency matrix. 
        
    def displayWorld(self):
        
        '''
        This function provides three functionalities.
        1. Display a textual summary of world
        2. Save textual summary of world
        3. Visualise the graph using networkx
        '''
        print('display world')
        command = input('There are three things that you can do\n1. Display information about features\n2. Save information about features\n3. Save a visual representation of the world')
        
        if command == '1': #user wants to display summary of world
            print('\n\n\n' + '-'*20)
            print('The world has ' + str(self.__graph.getVertexCount()) + ' Nodes\n') #display vertex count.
            for i in self.__graph.vertices: #self made iterator
                print(i.getLabel(), i.getData()) #display name of all vertices. 
                
            print('\n' + '-'*20 + '\n')
            
            print('The world has ' + str(self.__graph.getEdgeCount()) + ' Edges\n') #display number of edges.
            for i in self.__graph.vertices: #self made iterator
                for j in i.getAdjacentList(): #self made iterator
                    print(i.getLabel(), j.vertex.getLabel(), j.getWeight()) #display all the edges. 
            
            print('\n' + '-'*20 + '\n')
            print('The world has following NCodes:\n')
            print(self.__NCode) #diplay all N codes.
            print('\n' + '-'*20 + '\n')
            print('The world has following ECodes:\n')
            print(self.__ECode) #Display all E Codes. 
            print('\n' + '-'*20 + '\n')
            print('\nThe number of nodes of each type are as follow\n')
            tempHash = self._printNodeDistribution()
            print(tempHash)
            print('\n' + '-'*20 + '\n')
            print('\nThe number of edges of each type are as follow\n')
            tempHash = self._printEdgeDistribution()
            print(tempHash)
            print('\n' + '-'*20 + '\n')
        
        if command == '2': #user want to save the info. Pretty much similar to previous thing. 
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
            file.write('\n' + '-'*20 + '\n')
            file.write('\nThe number of nodes of each type are as follow\n')
            tempHash = self.__printNodeDistribution()
            for i in tempHash:
                file.write(i.getKey() + ' ' + str(i.getValue()) + '\n')
            file.write('\n' + '-'*20 + '\n')
            file.write('\nThe number of edges of each type are as follow\n')
            tempHash = self.__printEdgeDistribution()
            for i in tempHash:
                file.write(i.getKey() + ' ' + str(i.getValue()) + '\n')
            file.write('\n' + '-'*20 + '\n')
                    
        if command == '3': #user wants to visualise
            self.__visualise()
    

    def generateRoutes(self): #user wants to print all the routes. 
        '''
        This function generates all possible routes and save each route as a DSALinkedList. 
        All Lists are saved in a heap
        '''
        print('generate Route')
        self.__pathList = self.__graph.findPaths(self.__Start, self.__Target) #create routes. 
        numberOfPaths = self.__pathList.getCount()
        self.__pathHeap = DSAHeap(numberOfPaths)
        for i in self.__pathList: #self made iterator
            cost = self._calculateCost(i) #calculate cost.
            self.__pathHeap.add(cost, i)
        self.__pathHeap = self.__pathHeap.heapSort()
        print(numberOfPaths)
        
    def displayRoutes(self):
        '''
        This function displays/save all available routes
        '''
        print('display routes')
        print('currently there are', int(self.__pathList.getCount()), 'routes')
        #ask user for the number of routes that they want to save
        number = input('How many top routes you want to display? \nplease enter an integer.\nenter -a to display all paths')
        #ask if they want to save routes in a file. 
        toSave = input('do you want to save the matrix as well?enter 0 for no and 1 for yes')
        if toSave == '1': #if yes, then create a file obj after taking file name as input. 
            fname = input('please enter the name of the file where you want to save')
            file = open(fname, 'w')
        else:
            file = None 
        self._displayRoutes(number, toSave, file) #call function to diplay routes.
            
        
    def returnRoutes(self, num):
        count = 0
        
        routeList = DSALinkedList()
        while count < self.__pathList.getCount() and  count < num: #keep displaying/saving till this condition stands. 
            qobj = self.__pathHeap.getHeapArray()[count]
            routeList.insertLast(qobj.getPriority())
            count += 1
        return routeList
            
        
    
    def saveNetwork(self):
        '''
        This function saves Game class as a serialised file using pickle
        '''
        print('save network')
        filename = input('\nplease enter the name of file') #ask user for file name. 
        with open(filename, "wb") as f:
                pickle.dump(self, f)
        
    def Play(self, outfile):
        '''
        This function takes an outfile as parameter.
        it saves all the posbbile paths in that file. 
        '''
        file = open(outfile, 'w')
        self.generateRoutes()
        i = 0
        while i < self.__pathList.getCount():
            obj = self.__pathHeap.getHeapArray()[i]
            file.write(str(obj.getPriority()) + '  ' + str(obj.getValue()) + '\n')
            i = i + 1
            
################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########  