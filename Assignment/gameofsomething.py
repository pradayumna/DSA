#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 09 21:12:27 2021

@author: Pradyumna agrawal 


Welcome to the show readers. Its a huge chunk of code. But bear with my comment.
We will together make sense out of it.

"""
import sys #we need this for handling command line arguments
from Game import Game #well this is the class where magic happens

def __printUsageInformation():
    '''
    This one runs when you want to know what this entire program is about 
    or if you just forget to enter arguments.
    Returns
    -------
    None.

    '''
    instructions = open('instructions.txt', 'r') #to keep it clean, I wrote instructions in a txt file. 
    print(instructions.read())
    
def __interactiveTestingEnvironment():
    
    '''
    This one lets you interact with the program and see everything happening in real time
    '''    
    
    print('Welcome to interactive testing mode' + '\n'*4)
    commands = open('interactiveCommands.txt', 'r') #it just helps in keeping the code more readable
    print(commands.read())
    gameSet = False #so this tracks if we have set the 'map/graph/nework/that thing with edges and nodes' yes 
    
    while(True): #this lets you keep interacting untill you are tired of it. 
        command = input() #lets ask user what they want to do
        
        if command == '10': #ah snap, user is tired. lets stop this.
            return
        
        elif command == '1': #it means that user wants to set up the map. 
            filename = input('please enter the name of the file') #ask user the filename that has map
            try:
                game = Game(filename) #try setting up map. will not always happen. I think I have taken care of 
                #almost all bad inputs. if an input is bad, game wont set. 
                gameSet = True #the battlefield is set. 
            except ValueError as err: #catches empty files.
                print(err)
                print('enter new file name as this one is empty')
            except FileNotFoundError as err: #file does not even exists. 
                print(err)
                print('enter new file name as no such file exists')
            except KeyError: #there is no start or end. 
                print('the file do not have either a functional start or target. please enter a file that has both')
                #scope for imrovement - let user select start/target when they are missing
                #instead of completely disregarding their input. 
            
        else:
            if not gameSet: #this is the gatekeeper to other functionalities. It will not let
            #user use other functionalities till the map is set. 
                print('please enter an input file first to use other options')
            elif command == '2':
                game.nodeOperations() #allows node operations (look, add, delete, update).
            elif command == '3':
                game.edgeOperations() #allows edge operations (look, add, delete, update).
            elif command == '4':
                game.parameterTweaks() #allows updating start, target, Ecodes, Ncodes. 
            elif command == '5':
                game.displayGraph() #displays map in matrix form (also provides option to save).
            elif command == '6':
                game.displayWorld() #allows printings few stats and also has a graphical element.
            elif command == '7':
                game.generateRoutes() #creates all possible routes. 
            elif command == '8':
                game.displayRoutes() #displays possible routes. 
            elif command == '9':
                game.saveNetwork() #saves network using pickle (not gherkin)
            else:
                print('command not identified')
    
    
def __simulationMode(infile, outfile):
    
    '''
    (The direct route)
    This function takes an infile and prints all paths in an outfile. 

    Parameters
    ----------
    infile : TYPE
        DESCRIPTION.
    outfile : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    '''
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
    
    
################### THE END (HOPEFULY). PLEASE REAMIN SEATED FOR END CREDIT SCENES ##########