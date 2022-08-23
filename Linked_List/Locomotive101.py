class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_List :
    def __init__(self) :
        self.head = Node()

    def Append(self,data) : # add data to the bottom of list
        new_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node
    
    def Length(self) :
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur.cur.next
        return total
    
    def Display(self) :
        elems = []
        cur_node = self.head
        while cur_node.next != None :
            cur_node = cur_node.next
            elems.append(cur_node.data)
        for i in elems :
            print(i, end="")
            if i != elems[-1]:
                print(" <- ", end="")
    
    def changeListPosition(self) :
        cur_node = self.head
        last_node = self.head

        if cur_node.next.data == 0 :
            return

        while last_node.next != None :
            last_node = last_node.next

        while cur_node.next.data != 0 :
            cur_node = cur_node.next
        # switch 0 to first node
        
        last_node.next = self.head.next
        self.head.next = cur_node.next
        cur_node.next = None

        
        



my_list = Linked_List()

print(" *** Locomotive ***")
inp = input("Enter Input : ").split()
inp = list(map(int, inp))

for i in inp :
    my_list.Append(i)
print("Before : ",end="")
my_list.Display()
print()
my_list.changeListPosition()
print("After : ",end="")
my_list.Display()

# print(inp)