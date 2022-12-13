from collections import defaultdict


# Implement these functions when it is time to repeat checking if an undirected graph has a cycle
def search(graph, vertex, visited, parent):
    visited[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if search(graph, neighbor, visited, vertex):
                return True
        elif parent != neighbor:
            return True

    return False


def has_cycle(graph):
    visited = {v: False for v in graph.keys()}

    for vertex in graph.keys():
        if not visited[vertex]:
            if search(graph, vertex, visited, None):
                return True

    return False


# Implement this when it if time to repeat checking max number of edges that can be removed to create even trees
def traverse(graph, curr, result):
    descendants = 0

    for child in graph[curr]:
        num_nodes, result = traverse(graph, child, result)
        result[child] += num_nodes - 1
        descendants += num_nodes

    return descendants + 1, result


def max_edges(graph):
    start = list(graph)[0]
    vertices = defaultdict(int)

    _, descendants = traverse(graph, start, vertices)

    return len([val for val in descendants.values() if val % 2 == 1])
