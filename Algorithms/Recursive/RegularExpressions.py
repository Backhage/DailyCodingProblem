def matches(string, pattern):
    if not pattern:
        return not string

    first_match = bool(string) and pattern[0] in {string[0], "."}

    if len(pattern) >= 2 and pattern[1] == "*":
        return (
            matches(string, pattern[2:]) or first_match and matches(string[1:], pattern)
        )
    else:
        return first_match and matches(string[1:], pattern[1:])
