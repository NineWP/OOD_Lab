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
        if not self.root:
            self.root = Node(data)
            return self.root
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        break
                elif data > cur.data:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        break
                else:
                    break
            return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def checkpos(self,data):
        r = self.root
        if r.data == data:
            print("Root")
            return 
        while True:
            if r == None:
                print("Not exist")
                break
            if (r.left or r.right) and r.data == data:
                print("Inner")
                break
            if not r.left and not r.right and r.data == data:
                print("Leaf")   
                break
            if data < r.data:
                r = r.left
            if data > r.data:
                r = r.right
            

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
root = ""
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])