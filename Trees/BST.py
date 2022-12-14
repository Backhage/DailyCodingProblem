class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, x):
        if not self.root:
            self.root = Node(x)
        else:
            self._insert(x, self.root)

    def _insert(self, x, root):
        if x < root.data:
            if not root.left:
                root.left = Node(x)
            else:
                self._insert(x, root.left)
        else:
            if not root.right:
                root.right = Node(x)
            else:
                self._insert(x, root.right)

    def find(self, x):
        if not self.root:
            return False
        else:
            self._find(x, self.root)

    def _find(self, x, root):
        if not root:
            return False
        elif x == root.data:
            return True
        elif x < root.data:
            return self._find(x, root.left)
        else:
            return self._find(x, root.right)


# Implement this when it is time to repeat Find floor and ceiling
def get_bounds(root, x, floor=None, ceil=None):
    if not root:
        return floor, ceil

    if x == root.data:
        return x, x

    elif x < root.data:
        floor, ceil = get_bounds(root.left, x, floor, root.data)

    elif x > root.data:
        floor, ceil = get_bounds(root.right, x, root.data, ceil)

    return floor, ceil


# Implement this when it is time to repeat Convert sorted array to BST
def make_bst(array):
    if not array:
        return None

    mid = len(array) // 2
    root = Node(array[mid])
    root.left = make_bst(array[:mid])
    root.right = make_bst(array[mid + 1 :])

    return root


# Implement this when it is time to repeat Construct all BSTs with n nodes
def make_trees(low, high):
    trees = []

    if low > high:
        trees.append(None)
        return trees

    for i in range(low, high + 1):
        left = make_trees(low, i - 1)
        right = make_trees(i + 1, high)

        for l in left:
            for r in right:
                node = Node(i, left=l, right=r)
                trees.append(node)

    return trees


def construct_trees(N):
    return make_trees(1, N)
