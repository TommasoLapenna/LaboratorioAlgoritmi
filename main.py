import random
from linked_list import LinkedList
from binary_tree import BinaryTree, OrderStatisticTree
from avl_tree import AVLTree, AugmentedAVLTree
'''
bt = BinaryTree()

bt.treeInsert(2)
bt.treeInsert(7)
bt.treeInsert(5)
bt.treeInsert(9)
bt.treeInsert(10)

bt.inOrderTreeWalk()


ost = OrderStatisticTree()
ost.treeInsert(7)
ost.treeInsert(2)
ost.treeInsert(5)
ost.treeInsert(8)
ost.treeInsert(9)
ost.treeInsert(1)
ost.treeInsert(12)
ost.treeInsert(3)
ost.treeInsert(65)
ost.treeInsert(31)
ost.treeInsert(18)

ost.printTree()

print("---")

print(ost.osrank(80))

n = linked_list.Node(None, 0)
ll = LinkedList()

ll.orderedInsert(2)
ll.orderedInsert(1)
ll.orderedInsert(5)
ll.orderedInsert(3)

ll.walk()
print("---")
print(ll.osrank(0))
'''

avl = AugmentedAVLTree()

for i in range(50):
    avl.treeInsert(random.randint(0, 1000))

avl.treeInsert(0)

avl.printTree()
avl.inOrderTreeWalk()

print("-----")
print(avl.osselect(51).key)