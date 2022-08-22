# Into the Woods

class Stack():

    def __init__(self, ls = None):
        if ls == None:
            self.items = []
        else :
            self.items = ls

    def isEmpty(self):
        return self.items == []

    def push(self,i):
        self.items.append(i)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def clear(self):
        self.items.clear()

    def size(self):
        return len(self.items)

    def peek(self):
        if not self.isEmpty() : return self.items[-1]


s = Stack()

inp = input('Enter Input : ').replace(',', ' ').split()

for i in range(len(inp)) :
        if inp[i] == 'A':
            # print(s.peek(), inp[i+1])
            while (not s.isEmpty()) and int(s.peek()) < int(inp[i+1]):
                s.pop()
            if s.isEmpty() or int(s.peek()) > int(inp[i+1]):
                s.push(inp[i+1])
        elif inp[i] == 'B':
            print(s.size())
