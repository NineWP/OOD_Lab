class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        cur = self.root
        if self.root == None :
            self.root = Node(data)
        else :
            while(1) :
                if cur.data < data :
                    if cur.right != None :
                        cur = cur.right
                    else :
                        cur.right = Node(data)
                        return cur.right
                if cur.data > data :
                    if cur.left != None :
                        cur = cur.left
                    else :
                        cur.left = Node(data)
                        return cur.left
                        

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)
T.printTree(T.root)