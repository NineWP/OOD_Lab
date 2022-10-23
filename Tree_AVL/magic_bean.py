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
            print('*')
            return self.root
        else:
            cur = self.root
            while True:
                if data < cur.data:
                    if cur.left:
                        cur = cur.left
                        print('L', end='')
                    else:
                        cur.left = Node(data)
                        print('L*')
                        break
                elif data > cur.data:
                    if cur.right:
                        cur = cur.right
                        print('R', end='')
                    else:
                        cur.right = Node(data)
                        print('R*')
                        break
                else:
                    break
            return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    T.insert(i)