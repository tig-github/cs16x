# shortest paths algorithms
# corresponds to Week 3 of CS 163 https://ics.uci.edu/~eppstein/163/
# uses adjacency list representations
import heapq 


# copied from CS 161/graphs-list.py for use as a primitive in Johnson's Algorithm
def dijkstra(vertex, graph):
    """
    Dijkstra's Shortest Paths Algorithm
    DAG with cost values, unlike the other algorithms, in format below
    Analysis: O(mlogn) | O(m + nlogn) with fibonacci heap
    
    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    if not graph: return ([],[])
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
    Analysis: O(nm)

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
                return ([],[])
            
    return (distance,predecessor)
            
            
def johnson(graph):
    """
    Johnson's Algorithm
    Directed graph with cost values
    Analysis: O(mn + n^2logn)

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    graph[len(graph)] = [(graph[0], 0)] # add new vertex
    new_vertex = len(graph)-1
    distance = bellman_ford(new_vertex, graph)
    for vertex in graph: # reweighting the graph
        for edge in graph[vertex]:
            edge[1] = edge[1] + distance[vertex] + distance[edge[0]]
    del graph[len(graph)-1] # remove the new vertex
    final_distance,predecessor = dijkstra(graph)
    # implement distance fix here
    return (final_distance,predecessor)
    

def suurballe(graph):
    """
    Suurballe's Algorithm - Special Case of Network Flow
    Directed graph with cost values
    Analysis: O(m + nlogn)

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    pass 


def a_star(vertex, graph, heuristic):
    """
    A* Algorithm
    Directed graph with cost values
    Analysis: O(mlogn) | O(m + nlogn) with fibonacci heap

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
                if (distance[child] > distance[current_vertex] + cost + heuristic(vertex,child)):
                    distance[child] = distance[current_vertex] + cost
                    predecessor[child] = current_vertex
                    heapq.heappush(priority_queue, (distance[child], child))
                    
    return (distance,predecessor)