from collections import deque
from sys import maxsize as maxint

def test_bfs(graph, start, target, color, pred, depth, capacity, flow):
    """Breadth-First Search between start and target"""
 

    BLACK = 2
    GRAY = 1
    WHITE = 0 

    V = len(graph)

    for u in range(V):
        color[u] = WHITE
        depth[u] = -1

    q = deque()
    q.append(start)
    depth[start] = 0

    pred[start] = -1

    while q:
        u = q.popleft()
        color[u] = BLACK

        for v in range(V):
            if color[v] == WHITE and capacity[u,v] - flow[u, v] > 0:
                color[v] = GRAY
                q.append(v)
                pred[v] = u
                depth[v] = depth[u] + 1

    return (color[target] == BLACK, color, pred, depth)

def test_max_flow(graph, source, sink, color, pred, depth, flow):
    """Find maximum flow / minimum cut between source and sink with Ford Fulkerson"""

    V = len(graph)

    capacity = {}
    for i in range(V):
        for j in range(V):
            capacity[i, j] = graph[i][j]

    max_flow = 0

    

    for i in range(V):
        for j in range(V):
            flow[i, j] = 0

    result, color, pred, depth = test_bfs(graph, source, sink, color, pred, depth, capacity, flow)
    while result:
        increment = maxint

        u = sink

        while pred[u] != -1:
            increment = min(
                increment, capacity[pred[u], u] - flow[pred[u], u])
            u = pred[u]

        u = sink

        while pred[u] != -1:
            flow[pred[u], u] += increment
            flow[u, pred[u]] -= increment
            u = pred[u]

        max_flow += increment

        result, color, pred, depth = test_bfs(graph, source, sink, color, pred, depth, capacity, flow)

    return (max_flow, color, pred, depth, flow)
