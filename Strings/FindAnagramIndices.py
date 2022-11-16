from collections import defaultdict


def del_if_zero(dict, char):
    if dict[char] == 0:
        del dict[char]


def anagram_indices(word, string):
    freq = defaultdict(int)

    for char in word:
        freq[char] -= 1

    for char in string[: len(word)]:
        freq[char] += 1
        del_if_zero(freq, char)

    result = []
    if not freq:
        result.append(0)

    for i in range(len(word), len(string)):
        start_char, end_char = string[i - len(word)], string[i]

        freq[start_char] -= 1
        del_if_zero(freq, start_char)

        freq[end_char] += 1
        del_if_zero(freq, end_char)

        if not freq:
            start_index = 1 + i - len(word)
            result.append(start_index)

    return result
