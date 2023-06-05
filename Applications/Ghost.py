ENDS_HERE = "#"


class Trie:
    def __init__(self, words):
        self.trie = {}
        for word in words:
            self.insert(word)

    def insert(self, text):
        trie = self.trie

        for char in text:
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
                return None

        return trie


def is_winning(trie, prefix):
    root = trie.find(prefix)

    if ENDS_HERE in root:
        return False

    next_moves = [prefix + letter for letter in root]
    if any(is_winning(trie, move) for move in next_moves):
        return False

    return True


def optimal_starting_letters(words):
    trie = Trie(words)
    winners = []

    starts = trie.trie.keys()
    for letter in starts:
        if is_winning(trie, letter):
            winners.append(letter)

    return winners
