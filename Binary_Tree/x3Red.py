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

    def printTreexThree(self, node, k , level = 0) :
        if node != None:
            if node.data > k : node.data *= 3
            self.printTreexThree(node.right, k, level + 1)
            print('     ' * level, node)
            self.printTreexThree(node.left, k, level + 1)

    def findHeight(self, root) :
        if root is None:
            return 0 
        leftAns = self.findHeight(root.left)
        rightAns = self.findHeight(root.right)
        return max(leftAns, rightAns) + 1
    
    def Height(self) :
        return self.findHeight(self.root) - 1

T = BST()
inp = [int(i) for i in input('Enter Input : ').replace(' ', '/').split('/')]
for i in inp[0:-1]:
    T.insert(i)
T.printTree(T.root)
print("--------------------------------------------------")
T.printTreexThree(T.root, inp[-1])