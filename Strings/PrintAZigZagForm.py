def get_spaces(row, desc, k):
    max_spaces = 2 * (k - 1) - 1
    if desc:
        spaces = max_spaces - 2 * row
    else:
        spaces = max_spaces - 2 * (k - 1 - row)
    return spaces


def is_descending(index, k):
    return index % (2 * (k - 1)) < (k - 1)


def zigzag(string, k):
    n = len(string)
    for row in range(k):
        line = [" " for _ in range(n)]
        i = row
        while i < n:
            line[i] = string[i]
            desc = is_descending(i, k)
            spaces = get_spaces(row, desc, k)
            i += spaces + 1

        print("".join(line))


if __name__ == "__main__":
    zigzag("thisisazigzag", 4)
