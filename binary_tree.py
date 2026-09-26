class Node:
    def __init__(self, key, left=None, right=None, p=None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p
class BinaryTree:
    def __init__(self, root = None):
        self.root = root
        self.nodeVisited = 0

    def _walk(self, x):
        if x is not None:
            self._walk(x.left)
            print(x.key)
            self._walk(x.right)

    def inOrderTreeWalk(self):
        self._walk(self.root)

    def iterativeTreeSearch(self, k):
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
        n = Node(z)
        while x is not None:
            y = x
            if n.key < x.key:
                x = x.left
            else:
                x = x.right
            n.p = y
        if y is None:
            # Empty tree
            self.root = n
        elif n.key < y.key:
            y.left = n
        else:
            y.right = n

    def _transplant(self, u, v):
        if u.p is None:
            self.root = v
        elif u is u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v is not None:
            v.p = u.p

    def _treeMinimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def _treeMaximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def treeDelete(self, z):
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self._treeMinimum(z.right)
            if y.p is not z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._transplant(z,y)
            y.left = z.left
            y.left.p = y

    def _display(self, x):
        """Returns (lines, width, height, x-coord of x's label midpoint)."""
        if x is None:
            return [], 0, 0, 0

        label = str(x.key)
        width = len(label)

        if x.right is None and x.left is None:  # leaf
            return [label], width, 1, width // 2

        if x.right is None:  # only left child
            lines, n, p, x_mid = self._display(x.left)
            first_line = (n + 1) * ' ' + label
            second_line = n * ' ' + '/' + width * ' '
            shifted = [line + width * ' ' for line in lines]
            return [first_line, second_line] + shifted, n + width + 1, p + 2, n + width // 2

        if x.left is None:  # only right child
            lines, n, p, x_mid = self._display(x.right)
            first_line = label + (n + 1) * ' '
            second_line = width * ' ' + '\\' + n * ' '
            shifted = [width * ' ' + line for line in lines]
            return [first_line, second_line] + shifted, n + width + 1, p + 2, width // 2

        # two children
        left, n, p, x_mid = self._display(x.left)
        right, m, q, y_mid = self._display(x.right)

        first_line = (x_mid + 1) * ' ' + (n - x_mid - 1) * '_' + label + y_mid * '_' + (m - y_mid) * ' '
        second_line = x_mid * ' ' + '/' + (n - x_mid - 1 + width + y_mid) * ' ' + '\\' + (m - y_mid - 1) * ' '

        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)

        merged = [a + width * ' ' + b for a, b in zip(left, right)]
        return [first_line, second_line] + merged, n + m + width, max(p, q) + 2, n + width // 2

    def printTree(self):
        if self.root is None:
            print("(empty tree)")
            return
        lines, *_ = self._display(self.root)
        for line in lines:
            print(line)

class OrderStatisticTree (BinaryTree):
    def __init__(self, root = None):
        super().__init__(root)


    def osselect(self, i):
        self.nodeVisited = 0
        if self.root is None or i <= 0:
            return None

        stack = []
        current = self.root

        while len(stack) > 0 or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
                self.nodeVisited += 1

            current = stack.pop()
            i-=1

            if i == 0:
                return current
            current = current.right
        return None

    def osrank(self, x):
        self.nodeVisited = 0
        if self.root is None:
            return 0
        i=0
        stack = []
        current = self.root

        while len(stack) > 0 or current is not None:
            while current is not None:
                stack.append(current)
                current = current.left
                self.nodeVisited += 1

            current = stack.pop()
            i +=1
            if current.key == x:
                return i
            current = current.right
        return 0


