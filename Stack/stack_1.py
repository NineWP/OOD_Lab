# รุ้จักกับ Stack

class Stack :
    # Initializing an empty stack.

    def __init__(self, list = None):
        if list == None:
            self.items = []
        else :
            self.items = list

    def isEmpty(self):
        return self.items == [] # or len(self.items) == 0
    
    def size(self) :
        return len(self.items)

    def push(self, i):
        self.items.append(i)
        return "Add = {} and Size = {}".format(i, self.size())

    def pop(self): # remove & return the top
        if self.isEmpty() :
            return "-1"
        return "Pop = {} and Index = {}".format(self.items.pop(), self.size())

    def peek(self): # return the top
        return self.items[-1]
    
    def __str__(self) :
        s = "Value in Stack = "
        if self.isEmpty() :
            s += "Empty"
            return s
        for n in self.items :
            s += n + " "
        return s
        

list_input = [x for x in input("Enter Input : ").replace(',', ' ').split()]

stack = Stack()
for i in range(len(list_input)) :
    if list_input[i] == 'A' :
        stack.push(list_input[i + 1])
        print("Add = {} and Size = {}".format(list_input[i+1], stack.size()))
    elif list_input[i] == 'P' :
        print(stack.pop())
    
print(stack)

