def value(letter, power):
    # The power depends on the position of the letter
    # in the sliding window. It is unclear why a power of
    # 26 was chosen; possibly because there are 26 letters
    # in the english alphabet.
    # ord(letter) - 96 maps the letters a-z to 1-26.
    return (26**power) * (ord(letter) - 96)


def rabin_hash(prev, start, new, k):
    # 1. Subtract the value of the first letter of the current hash.
    # 2. Multiply the current hash value by 26.
    # 3. Add the value of the last letter in the shifted window.
    return (
        prev
        - value(
            start,
            k - 1,
        )
    ) * 26 + value(new, 0)


def find_matches(pattern, string):
    matches = []
    k = len(pattern)

    pattern_val = 0
    for i, char in enumerate(pattern):
        pattern_val += value(char, k - i - 1)

    hash_val = 0
    for i, char in enumerate(string[:k]):
        hash_val += value(char, k - i - 1)

    if pattern_val == hash_val:
        if string[:k] == pattern:
            matches.append(0)

    for i in range(len(string) - k):
        hash_val = rabin_hash(hash_val, string[i], string[i + k], k)
        if pattern_val == hash_val:
            if string[i + 1 : i + k + 1] == pattern:
                matches.append(i + 1)

    return matches
