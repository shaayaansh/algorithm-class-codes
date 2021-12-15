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
    distance = {}
    distance[node] = "0"
    counter = 0
    while queue:
        current = queue.pop(0)
        for i in range(len(graph[current])):
            if graph[current][i] not in visited:
                visited.append(graph[current][i])
                queue.append(graph[current][i])
                distance[graph[current][i]] = int(distance[current]) + 1
                print(graph[current][i], "Added to queue")
                print("VISITED IS: ", visited)
        print("QUEUE IS : ", queue)
        print("DISTANCES ARE : ", distance)


bfs(graph, "E", visited)
