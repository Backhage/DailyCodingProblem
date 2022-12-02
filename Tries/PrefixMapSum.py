class TrieNode:
    def __init__(self):
        self.letters = {}
        self.total = 0


class PrefixMapSum:
    def __init__(self):
        self._trie = TrieNode()
        self.map = {}

    def insert(self, key, value):
        # If the key already exist, increment prefix totals by
        # the difference of old and new values.
        diff = value - self.map.get(key, 0)
        self.map[key] = value

        trie = self._trie
        for char in key:
            if char not in trie.letters:
                trie.letters[char] = TrieNode()
            trie = trie.letters[char]
            trie.total += diff

    def sum(self, prefix):
        trie = self._trie
        for char in prefix:
            if char in trie.letters:
                trie = trie.letters[char]
            else:
                return 0
        return trie.total
