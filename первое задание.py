#Вариант №22

import heapq
graph = {
1: [(2, 1), (3, 2), (5, 3)],
2: [(4, 4), (5, 3)],
3: [(4, 3)],
4: [(5, 5)],
5: []
}


def dijkstra(graph, start):
    """Функция алгоритма дейкстра"""
    distances = {node: float('inf') for node in graph} #Инициализация словаря вида: (Вершина - расстояние от стартовой вершины)
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)


        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances



start_vertex = 1 #Стартовая вершина
shortest_paths = dijkstra(graph, start_vertex)

print(f"Кратчайшее расстояние от вершины {start_vertex} довершины 5: {shortest_paths[5]}")
