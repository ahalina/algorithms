from collections import deque

def bfs(graph, start, n):
    visited = [False] * (n + 1)
    queue = deque()
    result = []
    
    queue.append(start)
    visited[start] = True
    
    while queue:
        vertex = queue.popleft()
        result.append(str(vertex))
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

n = int(input())
graph = {i: [] for i in range(1, n+1)}

for i in range(1, n+1):
    parts = list(map(int, input().split()))
    k = parts[0]
    neighbors = parts[1:]
    graph[i] = neighbors

result = bfs(graph, 1, n)
print(' '.join(result))