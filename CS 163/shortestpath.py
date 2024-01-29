# shortest paths algorithms
# corresponds to Week 3 of CS 163 https://ics.uci.edu/~eppstein/163/
# uses adjacency list representations
import heapq 


# copied from CS 161/graphs-list.py for use as a primitive in Johnson's Algorithm
def djikstra(vertex, graph):
    """
    Djikstra's Shortest Paths Algorithm
    DAG with cost values, unlike the other algorithms, in format below

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    visited = [False for _ in range(len(graph))]
    predecessor = [-1 for _ in range(len(graph))]
    distance = [float('inf') for _ in range(len(graph))]
    
    predecessor[vertex] = None 
    distance[vertex] = 0
    
    priority_queue = []
    heapq.heappush(priority_queue, (0, vertex))
    
    while priority_queue:
        _,current_vertex = heapq.heappop(priority_queue)
        if visited[current_vertex] == False:
            visited[current_vertex] = True 
            for child,cost in graph[current_vertex]:
                if (distance[child] > distance[current_vertex] + cost):
                    distance[child] = distance[current_vertex] + cost
                    predecessor[child] = current_vertex
                    heapq.heappush(priority_queue, (distance[child], child))
                    
    return (distance,predecessor)

def bellman_ford(vertex, graph):
    """
    Bellman Ford Algorithm
    Directed graph with cost values

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
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