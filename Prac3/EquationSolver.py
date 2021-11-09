#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:58:03 2021

@author: pradyumna agrawal
"""
from DSAStack import stack
from DSAQueue import circularQueue


class equationSolver():
    
    def __init__(self, infix):
        self.infix = infix
    
    def _PrecedenceOf(self, sign):
        if sign in ['+', '-']:
            return 1
        elif sign in ['*', '/']:
            return 2
        
    def _parseInfixToPostfix(self):
        postFix = circularQueue()
        opStack = stack()
        infix = self.infix.split(' ')
        
        for i in infix:
            if i == '(':
                opStack.push('(')
            elif i == ')':
                while opStack.top() != '(':
                    postFix.enqueue(opStack.pop())
                opStack.pop()
            elif i in ['+', '-', '*', "/" ]:
                while (not opStack.isEmpty()) and (opStack.top() != '(') and (self._PrecedenceOf(opStack.top()) >= self._PrecedenceOf(i)):
                    postFix.enqueue(opStack.pop()) 
                opStack.push(i)
            else:
                postFix.enqueue(float(i))
            print(postFix)    
        while (not opStack.isEmpty()):
            postFix.enqueue(opStack.pop())
        
        return postFix
    
    def _executeOperation(self, op, op1, op2):
        if op == '+':
            return op1 + op2
        elif op == '-':
            return op2 - op1
        elif op == '*':
            return op1 * op2
        elif op == '/':
            return op2/op1
    def _evaluatePostFix(self, postFix):
        opStack = stack()
        while postFix.getCount() > 0:
            symbol = postFix.dequeue()
            if type(symbol) == float:
                opStack.push(symbol)
            else:
                op1 = opStack.pop()
                op2 = opStack.pop()
                opStack.push(self._executeOperation(symbol, op1, op2))
                
        return opStack.pop()
   
        
    def solve(self):
        postFix = self._parseInfixToPostfix()
        answer = self._evaluatePostFix(postFix)
        return answer
    
        
    

A = equationSolver('( 10 + 5 ) / 3 + ( 4 + 5 ) * 7')
A._parseInfixToPostfix()