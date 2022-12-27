def matches_first_char(s, r):
    if len(s) > 0 and len(r) > 0:
        return s[0] == r[0] or r[0] == "."
    else:
        return False


def matches(s, r):
    if r == "":
        return s == ""

    if len(r) == 1 or r[1] != "*":
        # The first character in the regex is not succeeded by a *.
        if matches_first_char(s, r):
            return matches(s[1:], r[1:])
        else:
            return False
    elif r[1] == "*":
        # The first character is succeeded by a *.
        # First, try zero length.
        if matches(s, r[2:]):
            return True

        # If that doesn't match straight away, try globbing more prefixes
        # until the first character of the string doesn't match anymore.
        i = 0
        while matches_first_char(s[i:], r):
            if matches(s[i + 1 :], r[2:]):
                return True
            i += 1
    else:
        # r is empty but not s
        return False
