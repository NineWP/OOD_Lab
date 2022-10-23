class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.data) 

class BST:
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
                
def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def left_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.left
          
    return ht
  
def right_height(node):
    ht = 0
    while(node):
        ht += 1
        node = node.right
          
    return ht

def TotalNodes(root):
    
    if(root == None):
        return 0
        
    lh = left_height(root)
    rh = right_height(root)
      
    if(lh == rh):
        return (1 << lh) - 1
        
    return 1 + TotalNodes(root.left) + TotalNodes(root.right)


T = BST()
inp = [int(i) for i in input('Enter Input : ').replace(' ', '/').split('/')]
for i in inp[:-1]:
    T.insert(i)
printTree90(T.root)
print('--------------------------------------------------')
print(TotalNodes(T.root))