def nth_sevenish_number(n):
    answer = 0
    bit_position = 0

    while n:
        if n & 1:
            answer += 7**bit_position

        n >>= 1
        bit_position += 1

    return answer
