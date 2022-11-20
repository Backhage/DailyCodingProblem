from LinkedLists.DoublyLinkedList import DoublyLinkedList
from LinkedLists.DoublyLinkedList import Node


class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.dict = {}
        self.list = DoublyLinkedList()

    def set(self, key, val):
        if key in self.dict:
            self.dict[key].delete()

        n = Node(key, val)
        self.list.add(n)
        self.dict[key] = n

        if len(self.dict) > self.max_size:
            head = self.list.get_head()
            self.list.remove(head)
            del self.dict[head.key]

    def get(self, key):
        if key in self.dict:
            n = self.dict[key]

            # Bumb to the back of the list by removing and adding the node.
            self.list.remove(n)
            self.list.add(n)
            return n.val
