class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next


# Implement this when it is time to repeat reversing singly linked list
def reverse(head):
    curr, prev = head, None
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev


# Implement this when it is time to repeat adding two linked lists
def add(node0, node1, carry=0):
    if not node0 and not node1 and not carry:
        return None

    node0_val = node0.data if node0 else 0
    node1_val = node1.data if node1 else 0
    total = node0_val + node1_val + carry

    node0_next = node0.next if node0 else None
    node1_next = node1.next if node1 else None
    carry_next = 1 if total >= 10 else 0

    return Node(total % 10, add(node0_next, node1_next, carry_next))


# Implement this when it is time to repeat alternative high-low form
def alternate(head):
    prev, curr = head, head.next

    while curr:
        if prev.data > curr.data:
            prev.data, curr.data = curr.data, prev.data

        if not curr.next:
            break

        if curr.next.data > curr.data:
            curr.next.data, curr.data = curr.data, curr.next.data

        prev = curr.next
        curr = curr.next.next

    return head


# Implement this when it is time to repeat finding intersecting node
def length(head):
    if not head:
        return 0
    return 1 + length(head.next)


def intersection(a, b):
    len_a, len_b = length(a), length(b)
    cur_a, cur_b = a, b

    if len_a > len_b:
        for _ in range(len_a - len_b):
            cur_a = cur_a.next

    if len_b > len_a:
        for _ in range(len_b - len_a):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next

    return cur_a
