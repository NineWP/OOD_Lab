class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

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