#
# DSA Final Assessment Question 2 - Q2BinarySearchTree.py
#
# Name : Pradyumna Agrawal
# ID   : 20046165
#
# 

class Q2BinarySearchTree():
    # Inner Treenode class
    class Q2TreeNode():
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            self.colour = 'Brown'
            
        def updateColour(self, colour):
            self.colour = colour
    # End inner class

    def __init__(self):
        self.root = None
    
    def insert(self, val):
        if (self.isEmpty()):
            self.root = self.Q2TreeNode(val)
        else:
            self.root = self.insertRec(val, self.root)

    def isEmpty(self):
        return self.root == None

    def insertRec(self, inVal, cur):
        if (cur == None):
            cur = self.Q2TreeNode(inVal)
        else:
            if (inVal < cur.value):
                cur.left = self.insertRec(inVal, cur.left)
            else:
                cur.right = self.insertRec(inVal, cur.right)
        return cur
    
    def colourTree(self):
        if self.root is not None: #check if the tree is not empty
            self.colour_rec(self.root, 0) #call the recursive colouring function
        else:
            print('tree is empty. You chopped them all down') #inform user about this the global warming
    
    def colour_rec(self, node, depth):
        # this function is inspired from pre-order traversal that I submitted as part of week 5 practical. 
        self.change_colour(node, depth) #call the function that uses if-else conditions to colour the tree
        if node.left is not None:
            self.colour_rec(node.left, depth+1)
        if node.right is not None:
            self.colour_rec(node.right, depth+1)

    
    def change_colour(self, node, depth):
        if node.left != None and node.right != None:
            node.updateColour('Black')
        elif node.left is not None or node.right is not None:
            node.updateColour('Brown')
        else:
            if depth <= 2:
                node.updateColour('Yellow')
            else:
                node.updateColour('Orange')
                
    def printColour(self):
        '''
       some additional functions for sanity check. This one provides the colour of tree nodes with the node values. 

        '''
        if self.root is not None:
            self.print_rec(self.root)
        else:
            print('tree is empty')
    
    def print_rec(self, node):
        print(node.value, node.colour)
        if node.left != None:
            self.print_rec(node.left)
        if node.right != None:
            self.print_rec(node.right)
        

            
        
