def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # First entry in each row and col represents the "empty string"
    # which is has a length of zero.
    lengths = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Start iterating from 1 since we already know that the length of
    # the empty string is zero.
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                lengths[i][j] = lengths[i - 1][j - 1] + 1
            else:
                lengths[i][j] = max(lengths[i - 1][j], lengths[i][j - 1])

    return build_sequence(lengths, str2)


def build_sequence(lengths, string):
    sequence = []
    i = len(lengths) - 1
    j = len(lengths[0]) - 1

    while i > 0 and j > 0:
        if lengths[i][j] == lengths[i - 1][j]:
            i -= 1
        elif lengths[i][j] == lengths[i][j - 1]:
            j -= 1
        else:
            sequence.append(string[j - 1])
            i -= 1
            j -= 1

    return list(reversed(sequence))
