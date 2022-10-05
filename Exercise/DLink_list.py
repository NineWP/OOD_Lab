class Node :
    def __init__(self, data = None) :
        self.data = data
        self.next = None
        self.prev = None 

class DLink_list :
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def Append(self, data) :
        new_node = Node(data)
        cur = self.head
        while cur.next :
            cur = cur.next
        cur.next = new_node
        if cur != self.head : new_node.prev = cur
        self.tail.prev = new_node

    def __str__(self) :
        s = "["
        cur = self.head
        while cur.next :
            s += str(cur.next.data) 
            cur = cur.next
            if cur.next : s += ","
        s += "]"
        return s

lst = DLink_list()

lst.Append(5)
lst.Append(6)
lst.Append(7)

