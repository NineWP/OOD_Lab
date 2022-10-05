
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

    def __str__(self) :
        s = "["
        cur = self.head
        while cur.next :
            s += str(cur.next.data) 
            cur = cur.next
            if cur.next : s += ","
        s += "]"
        return s

def addTwoNumber(l1, l2) :
    result = Linked_List()
    temp = 0
    for i in range(l1.Size()) :
        result.Append((temp + l1.Index(i) + l2.Index(i)) % 10)
        temp = (temp + l1.Index(i) + l2.Index(i)) // 10
    if temp : result.Append(temp)
    print(result)


lst1 = Linked_List()
lst2 = Linked_List()

inp = input().split(', ')
l1 = inp[0][2:]
l2 = inp[1][2:]
l1 = [int(s) for s in [*l1] if s.isdigit()]
l2 = [int(s) for s in [*l2] if s.isdigit()]

for i in l1 : lst1.Append(i)
for i in l2 : lst2.Append(i)

while lst1.Size() < lst2.Size() : 
    lst1.Append(0)
while lst1.Size() > lst2.Size() : 
    lst2.Append(0)

addTwoNumber(lst1, lst2)
