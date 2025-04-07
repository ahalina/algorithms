from collections import deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        curr, path = queue.popleft()
        if curr == end:
            return len(path) - 1, path
        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return -1, []

if __name__ == "__main__":
    n, start_node, end_node = map(int, input().split())
    adj = {}
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        adj[i] = line[1:]

    length, path = shortest_path(adj, start_node, end_node)

    if length != -1:
        print(length)
        print(*path)
    else:
        print(-1)