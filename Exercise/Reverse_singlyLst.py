class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class Linked_List :
    def __init__(self) :
        self.head = Node()

    def Append(self, data) :
        cur = self.head
        new_node = Node(data)
        while cur.next :
            cur = cur.next
        cur.next = new_node

    def isEmpty(self) :
        return self.head.next == None

    def Search(self, item) :
        index = 0
        cur = self.head
        while cur.next :
            if cur.next.data == item :
                return index
            index += 1
            cur = cur.next
        return None

    def Index(self, index) :
        cur = self.head
        count = 0
        while count != index :
            cur = cur.next
            count += 1
        return cur.next.data

    def Insert(self, index, item) :
        new_node = Node(item)
        cur = self.head
        for i in range(index) :
            if cur.next == None : break
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def Size(self) :
        cur = self.head
        count = 0
        while cur.next :
            count += 1
            cur = cur.next
        return count

    def Pop(self, index = None) :
        cur = self.head
        nextdata = None
        if index == None or index > self.Size() - 1 : index = self.Size() - 1
        for i in range(index):
            cur = cur.next
        nextdata = cur.next
        cur.next = cur.next.next
        return nextdata.data

    def Reverse(self) :
        prev = None
        next = None 
        cur = self.head.next
        while cur :
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head.next = prev

    def __str__(self) :
        s = "["
        cur = self.head
        while cur.next :
            s += str(cur.next.data) 
            cur = cur.next
            if cur.next : s += ","
        s += "]"
        return s\

lst = Linked_List()

lst.Append(1)
lst.Append(2)
lst.Append(3)
lst.Append(4)
lst.Reverse()

print(lst)
print(lst.head.next.data)