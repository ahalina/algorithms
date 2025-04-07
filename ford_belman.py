import sys

def solve_ford_bellman():
    n, m, start_node, end_node = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((u - 1, v - 1, w))

    start_node -= 1
    end_node -= 1

    distance = [float('inf')] * n
    parent = [-1] * n
    distance[start_node] = 0

    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if distance[u] != float('inf') and distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break

    # Проверка на наличие отрицательных циклов, достижимых из start_node
    for u, v, w in edges:
        if distance[u] != float('inf') and distance[u] + w < distance[v]:
            # Обнаружен отрицательный цикл, влияющий на кратчайший путь
            print(-1)
            return

    if distance[end_node] == float('inf'):
        print(-1)
        return
    else:
        print(distance[end_node])
        path = []
        curr = end_node
        while curr != -1:
            path.append(curr + 1)
            curr = parent[curr]
        print(*path[::-1])

if __name__ == "__main__":
    solve_ford_bellman()