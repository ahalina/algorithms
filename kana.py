from collections import deque

def topological_sort_kahn(graph):
   
    in_degree = {u: 0 for u in graph}
    
  
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    result = []
    
    while queue:
        u = queue.popleft()  
        result.append(u)
        
       
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    return result if len(result) == len(graph) else -1


n = int(input())
graph = {i: [] for i in range(1, n + 1)}

for i in range(1, n + 1):
    parts = list(map(int, input().split()))
    neighbors = parts[1:]
    graph[i] = neighbors

sorted_order = topological_sort_kahn(graph)

if sorted_order == -1:
    print(-1)
else:
    print(' '.join(map(str, sorted_order)))