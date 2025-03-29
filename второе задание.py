class Graph():
    def __init__(self, vertices):
        self.V = vertices  # Количество вершин
        self.edges = []  # Список рёбер


    def add_edge(self, u, v, weight):
        """Добавить ребро (u -> v) с весом weight"""
        self.edges.append((u, v, weight))


    def bellman_ford(self, start):
        dist = {v: float('inf') for v in range(self.V)}
        dist[start] = 0

        # Повторяем V-1 раз (где V - число вершин)
        for _ in range(self.V - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
        return dist

graph = Graph(6)
graph.add_edge(0, 1, 3)
graph.add_edge(0, 2, 9)
graph.add_edge(1, 2, 5)
graph.add_edge(2, 4, 1)
graph.add_edge(1, 3, 8)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 5, 4)
graph.add_edge(4, 5, 6)

a = 0

result = graph.bellman_ford(a)
print(f"Кратчайшее расстояние от вершины 0 до вершины 5: {result[5]}")
