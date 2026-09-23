from typing import override

from binary_tree import Node, BinaryTree

class AVLNode(Node):
    def __init__(self, key, left=None, right=None, p=None, height=1):
        super().__init__(key, left, right, p)
        self.height = height


class AVLTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)

    @staticmethod
    def _h(x):
        # A node pointing to None should return height = 0
        return x.height if x is not None else 0

    def _leftRotate(self, x):
        # BEFORE EXECUTION: x.right is not None
        y = x.right
        x.right = y.left
        x.height = max(self._h(x.left), self._h(x.right)) + 1
        if y.left is not None:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        y.height = max(self._h(y.left), self._h(y.right)) + 1
        x.p = y

    def _rightRotate(self, x):
        # BEFORE EXECUTION: x.left is not None
        y = x.left
        x.left = y.right
        x.height = max(self._h(x.left), self._h(x.right)) + 1
        if y.right is not None:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        y.height = max(self._h(y.left), self._h(y.right)) + 1
        x.p = y

    def _avlInsertFixup(self, x):
        x = x.p
        while x is not None:
            x.height = max(self._h(x.left), self._h(x.right)) + 1
            if self._h(x.left) - self._h(x.right) == 2:
                if self._h(x.left.left) - self._h(x.left.right) == -1:
                    self._leftRotate(x.left)
                self._rightRotate(x)
                x = x.p
            elif self._h(x.left) - self._h(x.right) == -2:
                if self._h(x.right.left) - self._h(x.right.right) == 1:
                    self._rightRotate(x.right)
                self._leftRotate(x)
                x = x.p
            x = x.p

    @override
    def treeInsert(self, z):
        y = None
        x = self.root
        w = AVLNode(z)
        while x is not None:
            y = x
            if w.key < x.key:
                x = x.left
            else:
                x = x.right
        w.p = y
        if y is None:
            self.root = w
        elif w.key < y.key:
            y.left = w
        else:
            y.right = w
        w.left = None
        w.right = None
        w.height = 1
        self._avlInsertFixup(w)

    @override
    def treeDelete(self, z):
        if z.left is None:
            fixup_start = z.p
            self._transplant(z, z.right)
        elif z.right is None:
            fixup_start = z.p
            self._transplant(z, z.left)
        else:
            y = self.treeMinimum(z.right)
            if y.p is z:
                # y is z.right itself: it slides directly into z's spot,
                # so its own height is what changes first.
                fixup_start = y
            else:
                # the real "gap" is left at y's old spot, filled by
                # y.right; that's where the height change starts.
                fixup_start = y.p
                self._transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._transplant(z, y)
            y.left = z.left
            y.left.p = y
        self._avlDeleteFixup(fixup_start)

    def _avlDeleteFixup(self, x):
        # Unlike insert, a rotation here can still shorten the subtree,
        # so - unlike _avlInsertFixup - we never skip past the node we
        # just rotated: every ancestor up to the root must be re-checked.
        while x is not None:
            x.height = max(self._h(x.left), self._h(x.right)) + 1
            if self._h(x.left) - self._h(x.right) == 2:
                if self._h(x.left.left) - self._h(x.left.right) == -1:
                    self._leftRotate(x.left)
                self._rightRotate(x)
            elif self._h(x.left) - self._h(x.right) == -2:
                if self._h(x.right.left) - self._h(x.right.right) == 1:
                    self._rightRotate(x.right)
                self._leftRotate(x)
            # x is now a child (or unchanged, if no rotation happened);
            # x.p is either the rotated subtree's new root, or - if no
            # rotation occurred - x's real parent. Either way this is the
            # correct next node to check, so we deliberately do NOT skip
            # it the way _avlInsertFixup does.
            x = x.p

class AugmentedAVLNode(AVLNode):
    def __init__(self, key, left=None, right=None, p=None, height=1, size=1):
        super().__init__(key, left, right, p, height)
        self.size = size

class AugmentedAVLTree(AVLTree):
    def __init__(self, root=None):
        super().__init__(root)

    @staticmethod
    def _s(x):
        """Metodo di supporto per ottenere la size di un nodo in sicurezza, analogo a _h(x)."""
        return x.size if x is not None else 0

    @override
    def _leftRotate(self, x):
        super()._leftRotate(x)
        y = x.p
        x.size = self._s(x.left) + self._s(x.right) + 1
        y.size = self._s(y.left) + self._s(y.right) + 1

    @override
    def _rightRotate(self, x):
        super()._rightRotate(x)
        y = x.p
        x.size = self._s(x.left) + self._s(x.right) + 1
        y.size = self._s(y.left) + self._s(y.right) + 1

    @override
    def _avlInsertFixup(self, x):
        x = x.p
        while x is not None:
            x.height = max(self._h(x.left), self._h(x.right)) + 1

            x.size = self._s(x.left) + self._s(x.right) + 1

            if self._h(x.left) - self._h(x.right) == 2:
                if self._h(x.left.left) - self._h(x.left.right) == -1:
                    self._leftRotate(x.left)
                self._rightRotate(x)
                x = x.p
            elif self._h(x.left) - self._h(x.right) == -2:
                if self._h(x.right.left) - self._h(x.right.right) == 1:
                    self._rightRotate(x.right)
                self._leftRotate(x)
                x = x.p
            x = x.p

    @override
    def _avlDeleteFixup(self, x):
        # Stesso concetto dell'insert: aggiorniamo la size risalendo
        while x is not None:
            x.height = max(self._h(x.left), self._h(x.right)) + 1

            # NUOVO: Calcolo size
            x.size = self._s(x.left) + self._s(x.right) + 1

            if self._h(x.left) - self._h(x.right) == 2:
                if self._h(x.left.left) - self._h(x.left.right) == -1:
                    self._leftRotate(x.left)
                self._rightRotate(x)
            elif self._h(x.left) - self._h(x.right) == -2:
                if self._h(x.right.left) - self._h(x.right.right) == 1:
                    self._rightRotate(x.right)
                self._leftRotate(x)

            x = x.p

    @override
    def treeInsert(self, z):
        y = None
        x = self.root

        w = AugmentedAVLNode(z)

        while x is not None:
            y = x
            if w.key < x.key:
                x = x.left
            else:
                x = x.right
        w.p = y
        if y is None:
            self.root = w
        elif w.key < y.key:
            y.left = w
        else:
            y.right = w
        w.left = None
        w.right = None
        w.height = 1

        w.size = 1

        self._avlInsertFixup(w)

    def _osselectWalk(self, x, i):
        if x is None:
            return None
        r = self._s(x.left) + 1
        if i == r:
            return x
        elif i < r:
            return self._osselectWalk(x.left, i)
        else:
            return self._osselectWalk(x.right, i-r)

    def osselect(self, i):
        return self._osselectWalk(self.root, i)

