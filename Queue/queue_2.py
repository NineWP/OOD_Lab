# คอยนาน

class Queue :

    def __init__(self, list = None):
        if list == None :
            self.items = []
        else :
            self.items = list
        self.time = 0

    def isEmpty(self) :
        return self.items == []

    def enQueue(self, i) :
        self.items.append(i)

    def deQueue(self):
        if not self.isEmpty() : return self.items.pop(0)
        else : return -1

    def size(self) :
        return len(self.items)

    def Time(self) :
        return self.time
    
    def timeReset(self) :
        self.time = 0

    def __str__(self) :
        s = str(self.items)
        return s


def add_to_cashier() :
    if q1.size() + 1 < 6 : 
        q1.enQueue(main_q.deQueue())
    elif q2.size() + 1 < 6 : 
        q2.enQueue(main_q.deQueue())
    if not q1.isEmpty() : q1.time += 1
    if not q2.isEmpty() : q2.time += 1

main_q = Queue()
q1 = Queue()
q2 = Queue()

inp = [*input("Enter people : ")]

main_q.items = inp
# print(main_q.items)

for i in range(1, len(inp) + 1) :
    if not q1.isEmpty() and q1.Time() == 3 :
        q1.deQueue()
        q1.timeReset()
    if not q2.isEmpty() and q2.Time() == 2 :
        q2.deQueue()
        q2.timeReset()
    add_to_cashier()
    print(i, main_q, q1, q2)
