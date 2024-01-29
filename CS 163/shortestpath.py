# shortest paths algorithms
# corresponds to Week 3 of CS 163 https://ics.uci.edu/~eppstein/163/
# uses adjacency list representations

# see CS 161 graphs-list.py for Djikstra's

def bellman_ford(vertex, graph):
    """
    Bellman Ford Algorithm
    Directed graph with cost values

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
        visited (set): visited nodes
    """
    predecessor = [-1 for _ in range(len(graph))]
    distance = [float('inf') for _ in range(len(graph))]
    distance[vertex] = 0
    
    for _ in range(len(graph)-1): #repeat |V|-1 times
        for vertex in graph.keys():
            for edge in graph[vertex]:
                if distance[vertex] + edge[1] < distance[edge[0]]:
                    distance[edge[0]] = distance[vertex] + edge[1]
                    predecessor[edge[0]] = vertex
    for vertex in graph.keys():
        for edge in graph[vertex]:
            if distance[vertex] + edge[1] < distance[edge[0]]:
                print("Negative Cycle Exists")
    return (distance,predecessor)
            
            
        

def johnson(graph):
    pass 

def suurballe(graph):
    pass 

def a_star(graph, heuristic):
    pass