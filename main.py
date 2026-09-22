import binary_tree
import linked_list
from linked_list import Node, LinkedList
from binary_tree import Node, BinaryTree
'''
n = binary_tree.Node(5, None, None, None)
bt = BinaryTree(n)

bt.treeInsert(2)
bt.treeInsert(7)
bt.treeInsert(5)
bt.treeInsert(9)
bt.treeInsert(10)

bt.inOrderTreeWalk()

'''
n = linked_list.Node(None, 0)
ll = LinkedList()

ll.orderedInsert(2)
ll.orderedInsert(1)
ll.orderedInsert(5)
ll.orderedInsert(3)

ll.walk()
print("---")
print(ll.osrank(0))
