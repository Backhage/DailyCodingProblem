import heapq

# We want to create a better representation of the network nodes.
# This class makes a graph that maps each node to a list of tuples
# of the form (neighbor, time)
class Network:
    def __init__(self, N, edges):
        self.vertices = range(N + 1)
        self.edges = edges

    def make_graph(self):
        graph = {v: [] for v in self.vertices}

        for u, v, w in self.edges:
            graph[u].append((v, w))

        return graph


# We can then use Dijkstra's algorithm to calculate the minumum time
# to reach each node, and then find the maximum of these times.
def dijkstras(N, edges):
    graph = Network(N, edges).make_graph()
    times = {}

    q = [(0, 0)]  # start time, start node
    while q:
        t, node = heapq.heappop(q)
        if node not in times:
            times[node] = t
            for neighbor, w in graph[node]:
                if neighbor not in times:
                    heapq.heappush(q, (t + w, neighbor))

    return max(times.values())
