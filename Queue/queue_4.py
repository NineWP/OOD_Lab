# Canteen

class Queue :

    def __init__(self, list = None):
        if list == None :
            self.items = []
        else :
            self.items = list

    def isEmpty(self) :
        return self.items == []

    def enQueue(self, i) :
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty() : return self.items.pop(0)
        else : return "Empty"

    def size(self) :
        return len(self.items)

    def __str__(self) :
        s = ""
        if not self.isEmpty() : 
            for i in self.items :
                s += i + " "
        else :
            s = "Empty"
        return s


memberq = Queue()
q2 = Queue()
mainq = Queue()

inp = input("Enter Input : ").split('/')
member_list = [int(x) for x in inp[0].replace(',', ' ').split()]
q2.items = [x for x in inp[1].replace(',', ' ').split()]

i = 1
while len(member_list)/2 != memberq.size() :
    for j in range(len(member_list)) :
        if i == member_list[j] :
            memberq.enQueue(member_list[j + 1])
    i += 1

for i in range(len(q2.items)) :
    if q2.items[i] == 'D' :
        print(mainq.deQueue())
    elif q2.items[i] == 'E' :
        for j in range(len(memberq.items)) :
            if memberq.items[j] == int(q2.items[i+1]) :
                mainq.enQueue(memberq.items[j])
                memberq.items.remove(int(q2.items[i+1]))
                break


