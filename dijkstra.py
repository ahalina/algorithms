import heapq

def dijkstra_with_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start, [start])]

    while priority_queue:
        dist, current, path = heapq.heappop(priority_queue)

        if dist > distances[current]:
            continue

        if current == end:
            return dist, path

        for neighbor, weight in graph.get(current, []):
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor, path + [neighbor]))

    return -1, []

if __name__ == "__main__":
    n, start_node, end_node = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        k = line[0]
        for j in range(1, len(line), 2):
            neighbor = line[j]
            weight = line[j + 1]
            graph[i].append((neighbor, weight))

    distance, path = dijkstra_with_path(graph, start_node, end_node)

    if distance != -1:
        print(distance)
        print(*path)
    else:
        print(-1)