from collections import defaultdict, deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Implement this when it it is time to repeat Count unival trees
def count_unival_subtrees(root):
    count, _ = helper(root)
    return count


def helper(root):
    if root is None:
        return 0, True

    left_count, is_left_unival = helper(root.left)
    right_count, is_right_unival = helper(root.right)
    total_count = left_count + right_count

    if is_left_unival and is_right_unival:
        if root.left is not None and root.val != root.left.val:
            return total_count, False
        if root.right is not None and root.val != root.right.val:
            return total_count, False
        return total_count + 1, True

    return total_count, False


# Implement this when it is time to repeat reconstructing a tree from pre-order
# and in-order traversals
def reconstruct(preorder, inorder):
    if not preorder and not inorder:
        return None

    if len(preorder) == len(inorder) == 1:
        return preorder[0]

    # We assume that elements of the input lists are tree nodes.
    root = preorder[0]
    root_i = inorder.index(root)
    root.left = reconstruct(preorder[1 : 1 + root_i], inorder[0:root_i])
    root.right = reconstruct(preorder[1 + root_i :], inorder[root_i + 1 :])

    return root


# Implement this when it is time to repeat evaluate arithmetic tree
def evaluate(root):
    if root.val == "+":
        return evaluate(root.left) + evaluate(root.right)
    elif root.val == "-":
        return evaluate(root.left) - evaluate(root.right)
    elif root.val == "*":
        return evaluate(root.left) * evaluate(root.right)
    elif root.val == "/":
        return evaluate(root.left) / evaluate(root.right)
    else:
        return root.val


# Implement this when it is time to repeat min sum level
def smallest_level(root):
    queue = deque([])
    queue.append((root, 0))

    # Create a map di accumulate the sum for each level
    level_to_sum = defaultdict(int)

    while queue:
        node, level = queue.popleft()
        level_to_sum[level] += node.val

        if node.right:
            queue.append((node.right, level + 1))

        if node.left:
            queue.append((node.left, level + 1))

    return min(level_to_sum, key=level_to_sum.get)
