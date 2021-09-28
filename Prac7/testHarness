#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 08:44:21 2021

@author: pradyumna agrawal
"""
from DSAHash import DSAHash, hashIO
def main():
    
    
    print("creating a hash with initial size of 20")
    newHash = DSAHash(20)
    print("\nhash initialised. however, the actual size of the hash is ", newHash.getHashSize())
    input("press enter to continue")
    print("--"*8 + "\nadding few elements in the hash")
    newHash.put("red", 10)
    newHash.put("green", 20)
    newHash.put("orange", 30)
    newHash.put("blue", 40)
    newHash.put("white", 60)
    newHash.put('purple', 20)
    
    input(" elements added press enter to continue")
    print("\nadding an entry with a key that has already been added\n")
    try:
        newHash.put("orange", 30)
    except KeyError as err:
        print(err)
        
    input("\npress enter to continue")
    print("\nlooking for a key in the hash")
    
    print("\nhash has orange ", newHash.hasKey("orange"))
    
    input("\npress enter to continue")
    print("\nlooking for a key in the hash")
    print("\nhash has ivory ", newHash.hasKey("ivory"))
    
    input("\npress enter to continue")
    print("\nremoving a key from hash")
    newHash.deleteKey("orange")
    print("\nhash has orange ", newHash.hasKey("orange"))
    
    input("\npress enter to continue")
    print("\nfinding something in hash\n")
    print("value stored with purple is ", newHash.get("purple").getValue())
    
    
    input("\npress enter to continue")
    print("----"*10)
    print("now doing file IO operations")
    print("\nfirst we willl read a CSV file")
    B = hashIO()
    hTable = B.readCSV('RandomNames7000.csv')
    
    input("\npress enter to continue")
    print("\nnow we willl write to a CSV file")
    B.writeCSV(hTable, 'newFile.csv')
    
    input("\npress enter to continue")
    print("\nnow we willl save to a serialised file")
    B.saveSerialisedFile(hTable, 'serialisedTable')
    
    
    input("\npress enter to continue")
    print("\nnow we willl load to a serialised file")
    C = B.loadSerialisedFile('serialisedTable')
    
    print("\nnow we willl lget value of a key")
    print(C.get('14080040').getValue())

if __name__ == "__main__":
    main()