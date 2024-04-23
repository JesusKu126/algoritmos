INF = float('inf')

def floyd_warshall(graph):

    V = len(graph)
    

    dist = [[0]*V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    

    for k in range(V):
        for i in range(V):
            for j in range(V):
               
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

distances = floyd_warshall(graph)

for row in distances:
    print(row)