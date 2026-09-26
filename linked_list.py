class Node:
    def __init__(self, key, next=None, prev= None):
        self.next = next
        self.key = key
        self.prev = prev

class LinkedList:
    def __init__(self, head = None):
        self.head = head
        self.nodeVisited = 0

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def orderedInsert(self, x):
        n = Node(x)
        if self.head is None or n.key <= self.head.key:
            n.next = self.head
            self.head = n
            return
        y = self.head
        while y.next is not None and y.next.key < n.key:
            y = y.next
        n.next = y.next
        n.prev = y
        if y.next is not None:
            y.next.prev = n
        y.next = n


    def delete(self, x):
        if x is None:
            return
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def walk(self):
        x = self.head
        while x is not None:
            print(f"{x.key} ")
            x = x.next


    # ORDER STATISTICS METHODS
    def osselect(self, i):
        self.nodeVisited = 0
        if i < 1:
            return None
        x = self.head
        self.nodeVisited += 1
        count = 1
        while x is not None and count != i:
            self.nodeVisited += 1
            x = x.next
            count+=1
        return x

    def osrank(self, x):
        y = self.head
        self.nodeVisited = 0
        count = 1
        while y is not None:
            self.nodeVisited += 1
            if y.key == x:
                break
            count +=1
            y = y.next
        if y is None:
            return 0
        return count


