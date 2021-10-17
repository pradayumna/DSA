#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 21:12:27 2021

@author: pradyumna agrawal
"""
import sys
from Game import Game

def __printUsageInformation():
    instructions = open('instructions.txt', 'r')
    print(instructions.read())
    
def __interactiveTestingEnvironment():
    
    print('Welcome to interactive testing mode' + '\n'*4)
    commands = open('interactiveCommands.txt', 'r')
    print(commands.read())
    gameSet = False
    
    while(True):
        command = input()
        
        if command == '10':
            return
        
        elif command == '1':
            filename = input('please enter the name of the file')
            try:
                game = Game(filename)
                gameSet = True
            except ValueError as err:
                print(err)
                print('enter new file name as this one is empty')
            except FileNotFoundError as err:
                print(err)
                print('enter new file name as no such file exists')
            except KeyError:
                print('the file do not have either a functional start or target. please enter a file that has both')
            
            
        else:
            if not gameSet:
                print('please enter an input file first to use other options')
            elif command == '2':
                game.nodeOperations()
            elif command == '3':
                game.edgeOperations()
            elif command == '4':
                game.parameterTweaks()
            elif command == '5':
                game.displayGraph()
            elif command == '6':
                game.displayWorld()
            elif command == '7':
                game.generateRoutes()
            elif command == '8':
                game.displayRoutes()
            elif command == '9':
                game.saveNetwork()
            else:
                print('command not identified')
    
    
def __simulationMode(infile, outfile):
    print('Welcome to simulation mode')
    
    game = Game(infile)
    game.Play(outfile)


def main():
    
    # if there are no arguments, then just print the usage information
    if len(sys.argv) == 1:
        __printUsageInformation()
        
    # if there is an argument and its equal to -i, then start interactive testing
    else:
        if sys.argv[1] == '-i':
            __interactiveTestingEnvironment()
            
        # if there is an argument and its equal to -s, then check for presence of second and third arguments. 
        elif sys.argv[1] == '-s':
            if len(sys.argv) < 4:
                # let user know that there are not sufficient arguments. 
                print('you are missing one or more file name')
                __printUsageInformation()
            else:
                __simulationMode(sys.argv[2], sys.argv[3])
        else:
            # if the argument is invalid, let the user know. 
            print('This command does not exists')
            __printUsageInformation()    

    
    
if __name__ == "__main__":
    main()
    
    

