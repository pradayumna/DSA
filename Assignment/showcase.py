#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 09:56:03 2021

@author: pradyumna agrawal
"""

from Game import Game

def _findrange(ll):
    high = low = ll.head.value
    for i in ll:
        if i < low:
            low = i
        if i > high:
            high = i
    return high - low

#Showcae - 1

sparse = Game('pacman1.txt') #loading sparse graph

dense = Game('gameofcatz2.txt') #loading dense graph

sparse.generateRoutes() #generating routes for sparse graph

dense.generateRoutes() #generating routes for dense graph

sparseRoutes = sparse.returnRoutes(15)

denseRoutes = dense.returnRoutes(15)

print('range for pacman1 is', _findrange(sparseRoutes))

print('range for gameofcatz2 is', _findrange(denseRoutes))

#showcase - 2

G = Game('gameofcatz.txt')

G.generateRoutes()

#showcase - 3

G = Game('amazing4.txt')

G.generateRoutes()

