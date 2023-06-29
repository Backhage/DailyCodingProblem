from collections import defaultdict, deque


def shortest_path_all_keys(grid):
    m, n = len(grid), len(grid[0])
    queue = deque()

    # seen['key'] is only for BFS with key state equals 'keys'
    seen = defaultdict(set)

    key_set, lock_set = set(), set()
    all_keys = 0
    start_row, start_col = -1, -1
    for i in range(m):
        for j in range(n):
            cell = grid[i][j]
            if cell in "abcdef":
                all_keys += 1 << (ord(cell) - ord("a"))
                key_set.add(cell)
            if cell in "ABCDEF":
                lock_set.add(cell)
            if cell == "@":
                start_row, start_col = i, j

    # [row, column, key_state, distance]
    queue.append((start_row, start_col, 0, 0))
    seen[0].add((start_row, start_col))

    while queue:
        cur_row, cur_col, keys, dist = queue.popleft()
        for delta_row, delta_col in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            new_row, new_col = cur_row + delta_row, cur_col + delta_col

            # If this cell (new_row, new_col) is reachable.
            if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != "#":
                cell = grid[new_row][new_col]

                # If it is a key we haven't picked up yet
                if cell in key_set and not ((1 << (ord(cell) - ord("a"))) & keys):
                    new_keys = keys | (1 << (ord(cell) - ord("a")))

                    # If we collect all keys, return dist + 1.
                    # Otherwise, just add this state to seen and queue.
                    if new_keys == all_keys:
                        return dist + 1
                    seen[new_keys].add((new_row, new_col))
                    queue.append((new_row, new_col, new_keys, dist + 1))

                # If it is a lock and we don't have its key, continue.
                elif cell in lock_set and not (keys & (1 << (ord(cell) - ord("A")))):
                    continue

                # We can walk to this cell if we haven't been here before with the same key state.
                elif (new_row, new_col) not in seen[keys]:
                    seen[keys].add((new_row, new_col))
                    queue.append((new_row, new_col, keys, dist + 1))

    return -1
