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
            print("Data cannot be added")
        elif index == 0 :
            self.Prepend(data)
            print("index = 0 and data = {}".format(data))
        elif index == self.Length() :
            self.Append(data)
            print("index = {} and data = {}".format(index, data))
        else :
            i = 0
            while index != i :
                i += 1
                cur = cur.next
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
            new_node.prev = cur
            print("index = {} and data = {}".format(index, data))

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
            
    def Remove(self,data) :
        # print("remove alert")
        if self.head.next == None :
            print("Not Found!")
            return
        cur = self.head.next
        index = 0
        if cur.data == data and cur.next == None and self.Length() == 1:
                self.head.next = None
                self.tail.prev = None
                print("removed : {} from index : 0".format(data, index))
                return
        while cur.next != None :
            if cur.data == data and index == 0:
                # print("if 1")
                self.rmFirst()
                print("removed : {} from index : 0".format(data))
                return
            elif cur.data == data :
                # print("if 2")
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                cur.next == None
                cur.prev == None
                print("removed : {} from index : {}".format(data, index))
                return
            elif cur.next.data == data and cur.next.next == None :
                # print("if 3")
                self.rmLast()
                print("removed : {} from index : {}".format(data, index))
                return
            cur = cur.next
            index += 1
        print("Not Found!")

    def isEmpty(self) :
        return self.Head.next == None

    def Length(self):
        cur = self.head
        total = 0
        while cur.next != None:
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
                s += "->"
            cur = cur.next
        return s


dllist = Doubly_Linked_List()

inp = input("Enter Input : ").split(',')
# print(inp)
for i in range(len(inp)) :
    if 'Ab' in inp[i] :
        temp = inp[i].split()
        dllist.Prepend(int(temp[1]))
    elif 'A' in inp[i] :
        temp = inp[i].split()
        dllist.Append(int(temp[1]))
    elif 'I' in inp[i] :
        temp = inp[i].replace(':', ' ').split()
        dllist.Insert(int(temp[1]), int(temp[2]))
    elif 'R' in inp[i] :
        temp = inp[i].split()
        dllist.Remove(int(temp[1]))
    print("linked list :", dllist)
    print("reverse :", dllist.str_reverse())


# dllist.Prepend(5)
# dllist.Append(1)
# dllist.Append(2)
# dllist.Append(3)
# dllist.Append(4)
# print(dllist)
# print(dllist.str_reverse())
# print(dllist.head.next.data, dllist.tail.prev.data)

# dllist.Insert(2, 10)

# dllist.Remove(3)
# print(dllist)
# print(dllist.str_reverse())
# print(dllist.head.next.data, dllist.tail.prev.data)

