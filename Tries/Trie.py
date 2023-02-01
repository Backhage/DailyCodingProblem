ENDS_HERE = "#"


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, string):
        trie = self.trie

        for char in string:
            if char not in trie:
                trie[char] = {}
            trie = trie[char]

        trie[ENDS_HERE] = True

    def find(self, prefix):
        trie = self.trie

        for char in prefix:
            if char in trie:
                trie = trie[char]
            else:
                return []

        return self._elements(trie)

    def _elements(self, trie):
        elements = []

        for c, v in trie.items():
            if c == ENDS_HERE:
                subresult = [""]
            else:
                subresult = [c + s for s in self._elements(v)]
            elements.extend(subresult)

        return elements


def autocomplete(query, strings):
    trie = Trie()

    for string in strings:
        trie.insert(string)

    suffixes = trie.find(query)
    return [query + suffix for suffix in suffixes]


# ENDS_HERE = "#"


# class Trie:
#     def __init__(self):
#         self._trie = {}

#     def insert(self, text):
#         trie = self._trie
#         for char in text:
#             if char not in trie:
#                 trie[char] = {}
#             trie = trie[char]
#         trie[ENDS_HERE] = True

#     def find(self, prefix):
#         trie = self._trie
#         for char in prefix:
#             if char in trie:
#                 trie = trie[char]
#             else:
#                 return []
#         return self._elements(trie)

#     def _elements(self, trie):
#         result = []
#         for c, v in trie.items():
#             if c == ENDS_HERE:
#                 subresult = [""]
#             else:
#                 subresult = [c + s for s in self._elements(v)]
#             result.extend(subresult)
#         return result


# def autocomplete(s, words):
#     trie = Trie()

#     for word in words:
#         trie.insert(word)

#     suffixes = trie.find(s)
#     return [s + w for w in suffixes]
