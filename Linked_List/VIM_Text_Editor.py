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
        if self.head.next is None :
            new_node = Node(data)
            new_node.prev = None
            self.head.next = new_node
            self.tail.prev = new_node
        else :
            new_node = Node(data)
            self.tail.prev = None
            self.tail.prev = new_node
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None
            # print(self.head.next.data)

    def Prepend(self, data) :  # add data to the start of list
        if self.head.next is None :
            new_node = Node(data)
            new_node.prev = None
            self.head.next = new_node
            self.tail.prev = new_node
        else :
            new_node = Node(data)
            self.head.next = None
            self.head.next = new_node
            cur = self.tail
            while cur.prev != None:
                cur = cur.prev
            cur.prev = new_node
            new_node.next = cur
            new_node.prev = None

    def Insert(self, index, data) :
        cur = self.head
        new_node = Node(data)
        if index < 0 or index > self.Length() :
            # print("Data cannot be added")
            return
        elif index == 0 :
            self.Prepend(data)
            # print("index = 0 and data = {}".format(data))
        elif index == self.Length() :
            self.Append(data)
            # print("index = {} and data = {}".format(index, data))
        else :
            i = 0
            while index != i :
                i += 1
                cur = cur.next
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur
            # print("index = {} and data = {}".format(index, data))

    def rmFirst(self) :
        if self.head.next != None :
            # print("if in rmFirst work")
            cur = self.head.next
            self.head.next = None
            self.head.next = cur.next
            cur.next = None
            self.head.next.prev = None

    def rmLast(self) :
        if self.tail.prev != None :
            cur = self.tail.prev
            self.tail.prev = None
            self.tail.prev = cur.prev
            cur.prev = None
            self.tail.prev.next = None

    def RemoveIndex(self, index) :
        # print("remove alert")
        if self.head.next == None :
            # print("Not Found!")
            return
        cur = self.head.next
        ind = 0
        if index == ind and cur.next == None and self.Length() == 1:
                self.head.next = None
                self.tail.prev = None
                return
        while ind < self.Length() :
            if index == ind and ind == 0:
                # print("if 1")
                self.rmFirst()
                return
            elif index == ind and cur.next != None:
                # print("if 2")
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.next == None
                cur.prev == None
                return
            elif index == ind and cur.next == None :
                # print("if 3")
                self.rmLast()
                return
            cur = cur.next
            ind += 1
        # print("Not Found!")

    def isEmpty(self) :
        return self.Head.next == None

    def Length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

    def cursorIndex(self):
        cur = self.head
        total = 0
        while cur.next.data != '|':
            total += 1
            cur = cur.next
        return total

    def Display(self):
        cur = self.head.next
        while cur.next != None:
            print(cur.data)
            cur = cur.next

    def str_reverse(self):
        cur = self.tail.prev
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
                s += " "
            cur = cur.next
        return s

dllist = Doubly_Linked_List()

inp = input("Enter Input : ").split(',')
dllist.Append('|')
# print(dllist.cursorIndex())

for i in range(len(inp)) :
    temp = inp[i].split()
    # print("temp = ", temp)
    if 'I' in temp[0] :
        dllist.Insert(dllist.cursorIndex(), temp[1])
        # print(dllist)
    elif 'L' in temp[0] :
        cur_index = dllist.cursorIndex()
        if cur_index != 0 :
            dllist.RemoveIndex(dllist.cursorIndex())
            dllist.Insert(cur_index - 1, '|')
            # print(dllist)
    elif 'R' in temp[0] :
        if dllist.cursorIndex() != dllist.Length() - 1 :
            cur_index = dllist.cursorIndex()
            dllist.RemoveIndex(dllist.cursorIndex())
            dllist.Insert(cur_index + 1, '|')
            # print(dllist)
    elif 'B' in temp[0] :
        if dllist.cursorIndex() != 0 :
            dllist.RemoveIndex(dllist.cursorIndex() - 1)
            # print(dllist)
    elif 'D' in temp[0]:
        if dllist.cursorIndex() != dllist.Length() - 1 :
            dllist.RemoveIndex(dllist.cursorIndex() + 1)
print(dllist)

