from collections import deque

def count_connected_components(graph, n):
    visited = [False] * (n + 1)
    components = 0
    
    for node in range(1, n + 1):
        if not visited[node]:
            components += 1
            queue = deque()
            queue.append(node)
            visited[node] = True
            
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    return components


n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    neighbors = parts[1:]
    graph[i] = neighbors

print(count_connected_components(graph, n))