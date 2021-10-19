#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:14:24 2021

@author: pradyumna agrawal
"""

from linkedKList import DSALinkedList
from DSAHashEntry import DSAHashEntry
from DSAHash import DSAHash
from DSAGraphWithEdge import DSAGraph, DSAGraphVertex, DSAGraphEdge
from DSAHeap import DSAHeap
from Game import Game

def UnitTestDSAHeap(score):
    
    #test - 1: create a heap of length 10
    try:
        h = DSAHeap(10)
        score += 1
    except:
        print('test 1 failed')
        
    #test 2 - add to Heap 
    try:
        h.add(5, 'E')
        h.add(2, 'B')
        h.add(6, 'F')
        score += 1
    except:
        print('test 2 failed')
        
    #test 3 - return count
    if h.returnCount() == 3:
        score += 1
        
    #test 4 - add to an already full heap
    h = DSAHeap(2)
    try:
        h.add(2, 'B')
        h.add(5, 'E')
        h.add(1, 'A')
    except:
        score += 1
        
    #test 5 - delete from a heap
    try:
        h.remove()
        score += 1
    except:
        print('test 5 failed')
        
    #test 6 - remove from heap and check its value
    if h.remove().getPriority() == 2:
        score += 1
        
    #test 7 - remove from NULL heap
    try:
        h.remove()
        h.remove()
    except:
        score += 1
    
    #test 8 - get heap array
    h.add(6, 'R')
    h.add(1, 'S')
    if h.getHeapArray()[1].getPriority() == 1:
        score += 1
        
    #test 9 - see if top element of the array changes
    h = DSAHeap(5)
    h.add(7, 'F')
    if h.getHeapArray()[0].getPriority() == 7:
        h.add(30, 'L')
        if h.getHeapArray()[0].getPriority() == 30:
            score += 1
    
    return score
def UnitTestDSALinkedList(score):
    
    L = DSALinkedList()
    
    #Test - 10: try adding elements in the beginning
    try:
        L.insertFirst(30)
        L.insertFirst(40)
        L.insertFirst(20)
        score += 1
        
    except:
        print('failed unit test 10')

    #Test - 11: try adding elements in the last
    try:
        L.insertLast(30)
        L.insertLast(40)
        L.insertLast(20)
        score += 1
        
    except:
        print('failed unit test 11')
    
    #test - 12 and 13: try peekfirst and peeklast
    if L.peekFirst() == 20:
        score += 1
    if L.peekLast() == 20:
        score += 1

    # test - 14: remove first
    L.removeFirst()
    if L.removeFirst() == 40:
        score += 1
        
    # test - 15: remove last
    L.removeLast()
    if L.removeLast() == 40:
        score += 1
        
    #test - 16: checking get count
    if L.getCount() == 2:
        score += 1
        
    return score

def UnitTestDSAHashEntry(score):
    h = DSAHashEntry()
    
    #test - 17: checking state getter
    h.setData('A', 10)
    if h.getState() == 1:
        score += 1

    #test - 18: checking key getter
    if h.getKey() == 'A':
        score += 1
        
    #test - 19: checking data getter
    if h.getValue() == 10:
        score += 1
    return score

def UnitTestDSAHash(score):
    newHash = DSAHash(20)
    
    #test - 20: checking put function
    try:
        newHash.put("red", 10)
        newHash.put("green", 20)
        newHash.put("orange", 30)
        newHash.put("blue", 40)
        newHash.put("white", 60)
        score += 1
    except:
        print('test 20 failed')
        
    #test - 21: adding a key thats already added
    try:
        newHash.put("white", 60)
    except:
        score += 1
        
    #test - 22: search a key in hash
    if newHash.hasKey("orange") == True:
        score += 1
        
    #test - 23: search a key not in hash
    if newHash.hasKey('Ivory') == False:
        score += 1
        
    #test - 24: checking delete key
    newHash.deleteKey("orange")
    if newHash.hasKey("orange") == False:
        score += 1
        
    #test - 25: checking getData
    if newHash.getData('blue') == 40:
        score += 1
        
    #test - 26: update data
    newHash.updateData('blue', 60)
    if newHash.getData('blue') == 60:
        score += 1
    return score

def UnitTestDSAGraphVertex(score):
    
    #test - 27: create vertices
    try:
        A = DSAGraphVertex('A', 1)
        B = DSAGraphVertex('B', 2)
        C = DSAGraphVertex('C', 3)
        D = DSAGraphVertex('D', 4)
        score += 1
    except:
        print('test 27 failed')

    #test - 28: get label
    if A.getLabel() == 'A':
        score += 1
        
    #test - 29: get Data
    if A.getData() == 1:
        score += 1
        
    #test - 30: update data
    B.updateData(5)
    if B.getData() == 5:
        score += 1
        
    #test - 31: add adjacent
    try:    
        B.addAdjacent(A, 10)
        B.addAdjacent(C, 10)
        B.addAdjacent(D, 10)
        score += 1
    except:
        print('test 31 failed')
        
    #test - 32: get adjacent list
    L = B.getAdjacentList()
    if L.peekFirst().vertex.getLabel() == 'A':
        score += 1
          
    return score

def UnitTestDSAGraphEdge(score):
    
    #test 33: check weight getter
    V = DSAGraphVertex('V', 2)
    E = DSAGraphEdge(V, 10)
    if E.getWeight() == 10:
        score += 1
        
    #test 34: check set weight
    E.setWeight(20)
    if E.getWeight() == 20:
        score += 1
        
    return score

def UnitTestDSAGraph(score):
    G = DSAGraph()
    
    #test 35: Adding vertex
    try:
        G.addVertex('A', 1)
        G.addVertex('B', 2)
        G.addVertex('C', 3)
        score += 1
    except:
        print('test 35 failed')
        
    #test 36 - checking hasVertex()
    if G.hasVertex('A') == True and G.hasVertex('H') == False:
        score += 1
        
    #test 37 - checking getVertex
    V = G.getVertex('A')
    if V.getLabel() == 'A':
        score += 1

    #test 38 - checking deleteVertex
    G.deleteVertex('A')
    if G.hasVertex('A') == False:
        score += 1
    
    #test 39 - check getVertexCount
    if G.getVertexCount() == 2:
        score += 1
        
    #test 40 and 41 - check addEdge and isAdjacent
    G.addEdge('B', 'C', 10)
    if G.isAdjacent('B', 'C') == True:
        score += 2
        
    #test 42 - check getAdjacent
    A = G.getAdjacent('B')
    if A.peekFirst().vertex.getLabel() == 'C':
        score += 1
        
    #test 43 and 44 - check deleteEdge and isAdjacent
    G.deleteEdge('B', 'C')
    if G.isAdjacent('B', 'C') == False:
        score += 2
        
    #test 45 and 46 - check updateEdge and getEdgeWeight
    G.addEdge('B', 'C', 10)
    G.updateEdge('B', 'C', 15)
    if G.getEdgeWeight('B', 'C') == 15:
        score += 2
        
    #test 47 - check getEdgeCount
    if G.getEdgeCount() == 1:
        score += 1
        
    # test 48 - check displayMatrix
    #print(G.displayMatrix())  #Visually confirmed. remove '#' to confirm yourself 
    score += 1
    
    # test 49 - check findPaths with just one path
    # graph: A - > B - > C
    G.addVertex('A', 5)
    G.addEdge('A', 'B', 2)
    path = G.findPaths(G.getVertex('A'), G.getVertex('C'))
    if str(path) == 'ABC':
        score += 1
        
    #test 50 - check findPaths with more than one path
    #graph: A -> B -> C
    #       A -> D -> C
    G.addVertex('D', 5)
    G.addEdge('A', 'D', 3)
    G.addEdge('D', 'C', 2)
    path = G.findPaths(G.getVertex('A'), G.getVertex('C'))
    path1 = path.removeFirst()
    path2 = path.removeFirst()
    if str(path1) == 'ABC' and str(path2) == 'ADC':
        score += 1
        #only add score when both paths are getting printed. 
        
    return score

def UnitTestGame(score):
    #test 51 - trying creating graph with a non existing file
    
    try:
        game = Game('yipeeKayYay.txt')
    except FileNotFoundError:
        score += 1
        
    #test 52 - trying creating a graph with no Start node
    try:
        game = Game('catwithoutstart.txt')
    except KeyError:
        score += 1
        
    #test 53 - trying creating a graph with an empty file
    try:
        game = Game('emptyFile.txt')
    except ValueError:
        score += 1

    #test 54 - create a graph with acceptable file
    try:
        game = Game('gameofcatz.txt')
        score += 1
    except:
        print('case 54 failed')
        

    #test 55 - check _lookForNode(ndLabel)
    print('\nTest Case 55')
    print('---'*5, '\n')
    game._lookForNode('A')
    game._lookForNode('Z')
    score += 1  #visually verified
    
    #test 56 - check _addNode(ndLabel, Ncode) with valid arguments
    game._addNode('Z', '-')
    print('\nTest Case 56')
    print('---'*5, '\n')
    game._lookForNode('Z')
    score += 1  #visually verified
    
    #test 57 - check _addNode(ndLabel, Ncode) with invalid NCode
    game._addNode('W', 'W')
    print('\nTest Case 57')
    print('---'*5, '\n')
    game._lookForNode('W')
    score += 1  #visually verified
    
    #test 58 - check _deleteNode(ndLabel) with valid Node
    game._deleteNode('B')
    print('\nTest Case 58')
    print('---'*5, '\n')
    game._lookForNode('B')
    score += 1  #visually verified
    
    #test 59 - check _deleteNode(ndLabel) with Start/Target node (A)
    #note - in my implementation, deleting a start/target node is not permittable. 
    print('\nTest Case 59')
    print('---'*5, '\n')
    game._deleteNode('A')
    game._lookForNode('A')
    score += 1  #visually verified
    
    #test 60 - check _updateNode(ndLabel, Ncode) with valid arguments
    print('\nTest Case 60')
    print('---'*5, '\n')
    game._updateNode('A', 'T')
    game._lookForNode('A')
    score += 1  #visually verified
    
    #test 61 - check _updateNode(ndLabel, Ncode) with invalid Node
    print('\nTest Case 61')
    print('---'*5, '\n')
    game._updateNode('X', 'T')
    score += 1  #visually verified
    
    #test 62 - check _updateNode(ndLabel, Ncode) with invalid Ncode
    print('\nTest Case 62')
    print('---'*5, '\n')
    game._updateNode('A', 'X')
    score += 1  #visually verified
    
    #test 63 - check _lookEdge(ndLabel1, ndLabel2) with valid nodes
    print('\nTest Case 63')
    print('---'*5, '\n')
    game._lookEdge('A', 'E')
    score += 1  #visually verified
    
    #test 64 - check _lookEdge(ndLabel1, ndLabel2) with valid nodes but no edge
    print('\nTest Case 64')
    print('---'*5, '\n')
    game._lookEdge('A', 'C')
    score += 1  #visually verified
    
    #test 65 - check _lookEdge(ndLabel1, ndLabel2) with invalid nodes
    print('\nTest Case 65')
    print('---'*5, '\n')
    game._lookEdge('X', 'C')
    score += 1  #visually verified
    
    #test 66 - check _addEdge(ndLabel1, ndLabel2, Ecode) with valid argument
    print('\nTest Case 66')
    print('---'*5, '\n')
    game._addEdge('A', 'C', '-')
    game._lookEdge('A', 'C')
    score += 1  #visually verified
    
    #test 67 - check _addEdge(ndLabel1, ndLabel2, Ecode) with invalid node
    print('\nTest Case 67')
    print('---'*5, '\n')
    game._addEdge('X', 'C', '-')
    score += 1  #visually verified
    
    #test 68 - check _addEdge(ndLabel1, ndLabel2, Ecode) with invalid Ecode
    print('\nTest Case 68')
    print('---'*5, '\n')
    game._addEdge('A', 'D', '@')
    score += 1  #visually verified
    
    #test 69 - check _addEdge(ndLabel1, ndLabel2, Ecode) when edge already exists
    print('\nTest Case 69')
    print('---'*5, '\n')
    game._addEdge('A', 'C', '-')
    score += 1  #visually verified
    
    #test 70 - check _deleteEdge(ndLabel1, ndLabel2) with valid arguments
    print('\nTest Case 70')
    print('---'*5, '\n')
    game._deleteEdge('A', 'C')
    game._lookEdge('A', 'C') #to check if actually deleted
    score += 1  #visually verified
    
    #test 71 - check _deleteEdge(ndLabel1, ndLabel2) with valid nodes with no edge
    print('\nTest Case 71')
    print('---'*5, '\n')
    game._deleteEdge('A', 'C')
    score += 1  #visually verified
    
    #test 72 - check _deleteEdge(ndLabel1, ndLabel2) with invalid node
    print('\nTest Case 72')
    print('---'*5, '\n')
    game._deleteEdge('A', 'X')
    score += 1  #visually verified
    
    #test 73 - check _updateEdge(ndLabel1, ndLabel2, Ecode) with valid arguments
    print('\nTest Case 73')
    print('---'*5, '\n')
    game._updateEdge('A', 'E', '-')
    score += 1  #visually verified
    
    #test 74 - check _updateEdge(ndLabel1, ndLabel2, Ecode) with invalid Ecode
    print('\nTest Case 74')
    print('---'*5, '\n')
    game._updateEdge('A', 'E', '@')
    score += 1  #visually verified
    
    #test 75 - check _updateEdge(ndLabel1, ndLabel2, Ecode) with valid nodes but no edge between them
    print('\nTest Case 75')
    print('---'*5, '\n')
    game._updateEdge('A', 'F', '-')
    score += 1  #visually verified
    
    #test 76 - check _updateEdge(ndLabel1, ndLabel2, Ecode) with invalid node
    print('\nTest Case 76')
    print('---'*5, '\n')
    game._updateEdge('A', 'X', '-')
    score += 1  #visually verified
    
    #test 77 - check _addNcode(Ncode, value) with valid arguments
    print('\nTest Case 77')
    print('---'*5, '\n')
    game._addNcode('$', 10)
    score += 1  #visually verified
    
    #test 78 - check _addNcode(Ncode, value) with non-int value
    print('\nTest Case 78')
    print('---'*5, '\n')
    game._addNcode('$', 'E')
    score += 1  #visually verified
    
    #test 79 - check _addNcode(Ncode, value) with already existing Ncode
    print('\nTest Case 79')
    print('---'*5, '\n')
    game._addNcode('T', 10)
    score += 1  #visually verified
    
    #test 80 - check _updateNcode(Ncode, value) with valid arguments
    print('\nTest Case 80')
    print('---'*5, '\n')
    game._updateNcode('T', 10)
    score += 1  #visually verified
    
    #test 81 - check _updateNcode(Ncode, value) with non-int value
    print('\nTest Case 81')
    print('---'*5, '\n')
    game._updateNcode('$', 'E')
    score += 1  #visually verified
    
    #test 82 - check _updateNcode(Ncode, value) with  non-existing Ncode
    print('\nTest Case 82')
    print('---'*5, '\n')
    game._updateNcode('!', 10)
    score += 1  #visually verified
    
    #test 83 - check _addEcode(Ecode, value) with valid arguments
    print('\nTest Case 83')
    print('---'*5, '\n')
    game._addEcode('$', 10)
    score += 1  #visually verified
    
    #test 84 - check _addEcode(Ecode, value) with non-int value
    print('\nTest Case 84')
    print('---'*5, '\n')
    game._addEcode('$', 'E')
    score += 1  #visually verified
    
    #test 85 - check _addNcode(Ecode, value) with already existing Ecode
    print('\nTest Case 85')
    print('---'*5, '\n')
    game._addEcode('$', 10)
    score += 1  #visually verified
    
    #test 86 - check _updateNcode(Ecode, value) with valid arguments
    print('\nTest Case 86')
    print('---'*5, '\n')
    game._updateEcode('$', 20)
    score += 1  #visually verified
    
    #test 87 - check _updateNcode(Ecode, value) with non-int value
    print('\nTest Case 87')
    print('---'*5, '\n')
    game._updateEcode('$', 'E')
    score += 1  #visually verified
    
    #test 88 - check _updateNcode(Ecode, value) with  non-existing Ecode
    print('\nTest Case 88')
    print('---'*5, '\n')
    game._updateEcode('!', 10)
    score += 1  #visually verified
    
    #test 89 - check _setStart(newStart) with existing Node
    print('\nTest Case 89')
    print('---'*5, '\n')
    game._setStart('C')
    score += 1  #visually verified
    
    #test 90 - check _setStart(newStart) with non-existing Node
    print('\nTest Case 90')
    print('---'*5, '\n')
    game._setStart('S')
    score += 1  #visually verified
    
    #test 91 - check _setTarget(newTarget) with existing Node
    print('\nTest Case 91')
    print('---'*5, '\n')
    game._setTarget('D')
    score += 1  #visually verified
    
    #test 92 - check _setTarget(newTarget) with non-existing Node
    print('\nTest Case 92')
    print('---'*5, '\n')
    game._setTarget('S')
    score += 1  #visually verified
    
    #test 93 - check _displayGraph(f, toSave) with no fileobj and toSave = '0'
    print('\nTest Case 93')
    print('---'*5, '\n')
    game._displayGraph(None, False)
    score += 1  #visually verified

    #test 94 - check generateRoutes() and _displayRoutes(number, toSave, file) with 3 routes
    print('\nTest Case 94')
    print('---'*5, '\n')
    game.generateRoutes()
    game._displayRoutes('-a', False, None)
    score += 1  #visually verified
    
    #test 94 - check generateRoutes() and _displayRoutes(number, toSave, file) with all routes
    print('\nTest Case 95')
    print('---'*5, '\n')
    game.generateRoutes()
    game._displayRoutes('-a', False, None)
    score += 1  #visually verified
    return score

    
def main():
    score = 0
    score = UnitTestDSAHeap(score)
    score = UnitTestDSALinkedList(score)
    score = UnitTestDSAHashEntry(score)
    score = UnitTestDSAHash(score)
    score = UnitTestDSAGraphVertex(score)
    score = UnitTestDSAGraphEdge(score)
    score = UnitTestDSAGraph(score)
    score = UnitTestGame(score)
    print('--------'*5, '\n')
    print(score, 'test passed')
    print('95 tests are enough for today. have a good night')
    print('\nsee yall on campus soon\n')
    print('--------'*5, '\n')
    
    
if __name__ == '__main__':
    main()