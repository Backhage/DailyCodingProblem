# This is listed under the Recursive chapter in the book but the
# optimal solution is actually not recursive.
def nim(heaps):
    a, b, c = heaps
    if a == b == c == 1:
        return False

    return a ^ b ^ c != 0
