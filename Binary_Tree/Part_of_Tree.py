class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
    
    def getMinNode(self,root):
        current = root
        while current.left:
            current = current.left
        return current

    def insert(self, val):  
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root
            while True:
                if val < current.data:
                    if not current.left:
                        current.left = Node(val)
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = Node(val)
                        break
                    current = current.right
        return self.root

    def delete(self,r,data):
        parent = None
        current = r

        while current and current.data != data:
            parent = current

            if data < current.data:
                current = current.left
            else:
                current = current.right
        
        if current is None:
            print('Error! Not Found DATA')
            return r
        
        if current.left is None and current.right is None:
            if current != r:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                r = None
            
        elif current.left and current.right:
            successor = self.getMinNode(current.right)
            temp = successor.data
            self.delete(r,successor.data)
            current.data = temp
        
        else:
            if current.left:
                child = current.left
            else:
                child = current.right
            
            if not parent:
                r = child

            if child != r:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
        return r

    def checkpos(self, lkpval) :
        if lkpval < self.data:
            if self.left is None:
                return "Not exist"
            return self.left.checkpos(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return "Not exist"
            return self.right.checkpos(lkpval)
        else:
            if self.root == self:
                print("Root")
            elif self.left != None and self.right != None :
                print("Inner")
            else :
                print("Leaf")
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


T = BinarySearchTree()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    T.insert(inp[i])
printTree90(T.root)
print(T.checkpos(inp[0]))