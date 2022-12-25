def tower_of_hanoi(k, a=1, b=2, c=3, solution=[]):
    if k >= 1:
        tower_of_hanoi(k - 1, a, c, b)
        solution.append((a, c))
        tower_of_hanoi(k - 1, b, a, c)

    return solution
