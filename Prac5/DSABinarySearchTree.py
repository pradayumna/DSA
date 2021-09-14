#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:03:54 2021

@author: pradyumna agrawal
"""

from DSATreeNode import DSATreeNode
from DSAQueue import queue
import pickle

class DSABinarySearchTree():
    
    def __init__(self):
        self._root = None
        
    def _findRec(self, key, currNd):
        
        value = None
        if currNd == None:
            raise KeyError("Key " + str(key) + " not found")
            
        elif currNd.getKey() == key:
            value = currNd.getValue()
            
        elif currNd.getKey() < key:
            value = self._findRec(key, currNd.getRight())
            
        else:
            value = self._findRec(key, currNd.getLeft())
            
        return value
    
    def find(self, key):
        try:
            value = self._findRec(key, self._root)
            return value
        except:
            print("key does not exists")
        
    def _insertRec(self, key, value, currNd):
        updateNode = currNd
        if currNd == None:
            newNd = DSATreeNode(key, value)
            updateNode = newNd
        elif key == currNd.getKey():
            raise KeyError("key already exists " + str(key))
        elif key < currNd.getKey():
            currNd.setLeft(self._insertRec(key, value, currNd.getLeft()))
        else:
            currNd.setRight(self._insertRec(key, value, currNd.getRight()))
        return updateNode
    
    def insert(self, key, value):
        try:
            self._root = self._insertRec(key, value, self._root)
        except:
            print(str(key) + " is duplicate")
    def _promoteSuccessor(self, node):
        successor = node
        if node.getLeft() == None:
            successor = node
        elif node.getLeft() != None:
            successor = self._promoteSuccessor(node.getLeft())
            if successor == node.getLeft():
                node.setLeft(successor.getRight())
        return successor
    
    def _deleteNode(self, key, node):
        updateNode = node
        if node.getLeft() == None and node.getRight() == None:
            updateNode = None
        elif node.getLeft() != None and node.getRight() == None:
            updateNode = node.getLeft()
        elif node.getLeft() == None and node.getRight() != None:
            updateNode = node.getRight()
        else:
            updateNode = self._promoteSuccessor(node.getRight())
            if updateNode != node.getRight():
                updateNode.setRight(node.getRight())
            updateNode.setLeft(node.getLeft())
        return updateNode
    
    def _deleteRec(self, key, node):
        updateNode = node
        if node == None:
            raise KeyError("key not in tree")
        elif key == node.getKey():
            updateNode = self._deleteNode(key, node)
        elif key < node.getKey():
            node.setLeft(self._deleteRec(key, node.getLeft()))
        else:
            node.setRight(self._deleteRec(key, node.getRight()))
        return updateNode
    
    def delete(self, key):
        try:
            self._root = self._deleteRec(key, self._root)
        except KeyError as E:
            print(E)
        
    def display(self, tType):
        tQ = queue()
        if self._root == None:
            return tQ
        else:
            if tType == '1':
                tQ = self._inOrderTraversal(self._root, tQ)
            elif tType == '2':
                tQ = self._preOrderTraversal(self._root, tQ)
            elif tType == '3':
                tQ = self._postOrderTraversal(self._root, tQ)
            for i in tQ:
                print(i)
    
    def _heightRec(self, currNd):
        if currNd is None:
            htSoFar = -1
        else:
            leftHt = self._heightRec(currNd.getLeft())
            rightHt = self._heightRec(currNd.getRight())
            
            if leftHt > rightHt:
                htSoFar = leftHt + 1
            else:
                htSoFar = rightHt + 1
        return htSoFar
    
    def height(self):
        return self._heightRec(self._root)
        
    def minKey(self):
        currNd = self._root
        while (currNd.getLeft() != None):
            currNd = currNd.getLeft()
            minKey = currNd.getKey()
        return minKey
    
    def maxKey(self):
        currNd = self._root
        while (currNd.getRight() != None):
            currNd = currNd.getRight()
            minKey = currNd.getKey()
        return minKey
    def _inOrderTraversal(self, node, tQ):
        if node.getLeft() != None:
            tQ = self._inOrderTraversal(node.getLeft(), tQ)
        tQ.enqueue([node.getKey(), node.getValue()])
        if node.getRight() != None:
            tQ = self._inOrderTraversal(node.getRight(), tQ)
        return tQ
    
        
    def _preOrderTraversal(self, node, tQ):
        tQ.enqueue([node.getKey(), node.getValue()])
        if node.getLeft() != None:
            tQ = self._preOrderTraversal(node.getLeft(), tQ)
        if node.getRight() != None:
            tQ = self._preOrderTraversal(node.getRight(), tQ)
        return tQ
    
        
    def _postOrderTraversal(self, node, tQ):
        if node.getLeft() != None:
            tQ = self._postOrderTraversal(node.getLeft(), tQ)
        if node.getRight() != None:
            tQ = self._postOrderTraversal(node.getRight(), tQ)
        tQ.enqueue([node.getKey(), node.getValue()])
        return tQ      
    
    def balance(self):
        height = self.height()
        idealSize = 2**(height + 1) - 1
        tQ = queue()
        actualSize = self._postOrderTraversal(self._root, tQ).count()
        return 100 - ((idealSize - actualSize)*100)/idealSize
    
    def serialize(self, name):
        with open(name, "wb") as f:
                pickle.dump(self, f)
                
    def writeCSV(self, name, order):
        tQ = queue()
        if self._root == None:
            return tQ
        else:
            if order == '1':
                tQ = self._inOrderTraversal(self._root, tQ)
            elif order == '2':
                tQ = self._preOrderTraversal(self._root, tQ)
            elif order == '3':
                tQ = self._postOrderTraversal(self._root, tQ)
        with open(name, 'w') as f:
            for i in tQ:
                f.write(str(i[0]) + ',' + str(i[1]))
