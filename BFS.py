graph = {
    "A": ["B", "C", "E", "F"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "F"],
    "D": ["B", "Z"],
    "E": ["A"],
    "F": ["A", "C"],
    "Z": ["D"]
}
visited = []


def bfs(graph, node, visited):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        current = queue.pop(0)
        for i in range(len(graph[current])):
            if graph[current][i] not in visited:
                visited.append(graph[current][i])
                queue.append(graph[current][i])
                print(graph[current][i], "Added to queue")
                print("VISITED IS: ", visited)
        print("QUEUE IS : ", queue)


bfs(graph, "A", visited)
