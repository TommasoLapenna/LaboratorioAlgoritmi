class Node:
    def __init__(self, prev, next, key):
        self.prev = prev
        self.next = next
        self.key = key

class LinkedList:
    def __init__(self):
        self.head = None
    def __init__(self, head):
        self.head = head

    def search(self, k):
        x = self.head
        while x is not None and x.key != k:
            x = x.next
        return x

    def insert(self, x):
        x.next = self.head
        if self.head is not None:
            self.head.prev = x
        self.head = x
        x.prev = None

    def delete(self, x):
        if x.prev is not None:
            x.prev.next = x.next
        else:
            self.head = x.next
        if x.next is not None:
            x.next.prev = x.prev

    def print(self):
        x = self.head
        while x is not None:
            print(f"{x.key} ")
            x = x.next


