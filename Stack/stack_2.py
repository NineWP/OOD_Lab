from inspect import ismemberdescriptor


class Stack :
    def __init__(self, list = None) :
        if list == None:
            self.items = []
        else :
            self.items = list


    def isEmpty(self) :
        return self.item == []

    def size(self) :
        return len(self.items)
    
    def push(self, i) :
        self.items.append(i)
        return "Add = " + i

    def pop(self) :
        if not self.isEmpty() :
            return "Add = " + self.items.pop() 
        else :
            return "-1"

    def peek(self):
        if not self.isEmpty() :
            return self.items[-1]

    def delete(self, num) :
        self.items.remove(num)
        return "Delete = " + num

    def lessThan_delete(self, num) :
        if self.isEmpty() : return -1

    def moreThan_delete(self, num) :
        if self.isEmpty() : return -1
        
    def __str__(self) :
        s = "Value in Stack = " + self.items
        return s


stack = Stack()

list_input = [x for x in input("Enter Input : ").replace(',', ' ').split()]

for i in range(len(list_input)) :
    if list_input[i] == 'A' :
        stack.push(list_input[i + 1])
        print("Add = {} and Size = {}".format(list_input[i+1], stack.size()))
    elif list_input[i] == 'P' :
        print(stack.pop())