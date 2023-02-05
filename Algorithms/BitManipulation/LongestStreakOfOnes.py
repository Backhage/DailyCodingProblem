# Computes the longest consecutive string of ones in the binary representation
# of a number.
def find_length(number):
    max_length = 0

    while number:
        max_length += 1
        number = number & (number << 1)

    return max_length
