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
            print(i, end=" ")
        print()

    def Get(self,index) :
        if index >= self.Length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0 
        cur_node = self.head
        while True :
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

def MergeList(list1, list2) :
    cur_node = list2.head.next
    elems = []
    while cur_node.next != None :
        elems.append(cur_node.data)
        cur_node = cur_node.next
    if cur_node.next == None : elems.append(cur_node.data)
    for i in reversed(elems) :
        list1.Append(i) 


L1 = Linked_List()
L2 = Linked_List()

inp = input("Enter Input (L1,L2) : ").split()
# print(inp)
list1 = inp[0].split('->')
list2 = inp[1].split('->')

for i in list1 : L1.Append(i)
for i in list2 : L2.Append(i)
    
# L1.Display()
# L2.Display()

print("L1    :",' '.join(list1))
print("L2    :",' '.join(list2))
MergeList(L1, L2)
print("Merge : ", end="")
L1.Display()
