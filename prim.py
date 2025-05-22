import heapq

def prim_algorithm(n, edges):
    
    adj = [[] for _ in range(n+1)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    visited = [False] * (n+1)
    min_heap = []

    heapq.heappush(min_heap, (0, 1, -1)) 
    
    total_weight = 0
    mst_edges = []
    
    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if parent != -1:
          
            if parent < u:
                mst_edges.append((parent, u))
            else:
                mst_edges.append((u, parent))
        
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))
    if sum(visited[1:]) != n:
        return -1, []
    
    return total_weight, mst_edges

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx += 2
    
    edges = []
    for _ in range(m):
        u, v, w = int(data[idx]), int(data[idx+1]), int(data[idx+2])
        edges.append((u, v, w))
        idx += 3
    
    total_weight, mst_edges = prim_algorithm(n, edges)
    
    if total_weight == -1:
        print(-1)
    else:
        print(total_weight)
        mst_edges_sorted = sorted(mst_edges, key=lambda x: (x[0], x[1]))
        print(' '.join(f"{u} {v}" for u, v in mst_edges_sorted))

if __name__ == "__main__":
    main()
