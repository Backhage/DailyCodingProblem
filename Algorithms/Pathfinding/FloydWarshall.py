# Traditionally Floyd-Warshall is used for finding the shortest path between all
# vertices in a weighted graph.
# Since we are not concerned with the cost, we use a modified version to only check
# whether it is possible to get from node i to node j.
def transitive_closure(graph):
    n = len(graph)
    reachable = [[0 for _ in range(n)] for _ in range(n)]

    for i, v in enumerate(graph):
        for neighbor in v:
            reachable[i][neighbor] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If it is possible to reach node k from node i and node j from
                # node k, then it is possible to reach node j from node i.
                reachable[i][j] |= reachable[i][k] and reachable[k][j]

    return reachable
