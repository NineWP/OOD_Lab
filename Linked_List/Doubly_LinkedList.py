from hashlib import new


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class Doubly_Linked_List:
    def __init__(self):
        self.head = Node()
        self.tail = Node()

    def Append(self, data):  # add data to the bottom of list
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head.next = new_node
        else:
            new_node = Node(data)
            self.tail.next = new_node
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def Prepend(self, data):  # add data to the start of list
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head.next = new_node
        else:
            new_node = Node(data)
            cur = self.head.next
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = None
            self.head.next = new_node

    def insert(self, index, data) :
        cur = self.head
        new_node = Node(data)
        if index < 0 or index > self.Length() :
            print("Data cannot be added")
        elif index == 0 :
            self.Prepend(data)
        elif index == self.Length() :
            self.Append(data)
        else :
            i = 0
            while index != i :
                i += 1
                cur = cur.next
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur

    
    def isEmpty(self) :
        return self.Head == None

    def Length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def Display(self):
        cur = self.head.next
        while cur:
            print(cur.data)
            cur = cur.next

    def str_reverse(self):
        cur = self.tail.next
        s = ""
        while cur:
            s += str(cur.data)
            if cur.prev != None:
                s += "->"
            cur = cur.prev
        return s

    def __str__(self):
        cur = self.head.next
        s = ""
        while cur:
            s += str(cur.data)
            if cur.next != None:
                s += "->"
            cur = cur.next
        return s


dllist = Doubly_Linked_List()

dllist.Append(1)
dllist.Append(2)
dllist.Append(3)
dllist.Append(4)
dllist.Prepend(5)
dllist.insert(2, 10)

print(dllist)
print(dllist.str_reverse())
