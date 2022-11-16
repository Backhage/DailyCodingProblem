def is_palindrome(word):
    return word == word[::-1]


def palindrome_pairs(words):
    # Create a dictionary for quick look up
    d = {}
    for i, word in enumerate(words):
        d[word] = i

    result = []
    for i, word in enumerate(words):
        for char_i in range(len(word)):
            prefix, suffix = word[:char_i], word[char_i:]
            reverse_prefix = prefix[::-1]
            reverse_suffix = suffix[::-1]

            if is_palindrome(prefix) and reverse_suffix in d:
                if d[reverse_suffix] != i:
                    result.append((d[reverse_suffix], i))

            if is_palindrome(suffix) and reverse_prefix in d:
                if d[reverse_prefix] != i:
                    result.append((i, d[reverse_prefix]))

    return result
