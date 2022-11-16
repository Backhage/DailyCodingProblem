def get_best_word(string, k):
    string = list(string)
    if k == 1:
        best = string
        for i in range(1, len(string)):
            if string[i:] + string[:i] < best:
                best = string[i:] + string[:i]

        return "".join(best)

    return "".join(sorted(string))
