#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 04:35:54 2021

@author: pradyumna agrawal
"""
from EquationSolver import equationSolver


f = ['4', '4 + 7', '4 - 7', '4 * 7', '4 / 7', '4 + 7 * 4 / 7', '4 * ( 4 + 7 )']

for equation in f:
    EQObject = equationSolver(equation)
    print(EQObject.solve())