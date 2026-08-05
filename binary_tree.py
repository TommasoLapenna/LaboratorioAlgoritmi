class Node:
    def __init__(self, key, left, right, p):
        self.key = key
        self.left = left
        self.right = right
        self.p = p

class BinaryTree:
    def __init__(self, root):
        self.root = root

    def _walk(self, x):
        if x is not None:
            self._walk(x.left)
            print(x.key)
            self._walk(x.right)

    def inOrderTreeWalk(self):
        self._walk(self.root)

    def treeMinimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def treeMaximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def iterativeSearch(self, k):
        x = self.root
        while x is not None and k  is not x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def treeInsert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
            z.p = y
        if y is None:
            # Empty tree
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def _transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def treeDelete(self, z):
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            if y.p is not z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._transplant(z,y)
            y.left = z.left
            y.left.p = y

