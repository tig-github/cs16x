# graph algorithms implemented
# uses adjacency list
from collections import deque
import heapq

def depth_first_traversal(vertex, graph, visited, action):
    """
    DFT on adjacency list

    Args:
        vertex (int): current vertex
        graph (list[list]): adjacency list
        visited (set): visited nodes
        action (func): action function on visited node
    """
    action(vertex)
    visited.add(vertex)
    for child in graph[vertex]:
        if child not in visited:
            depth_first_traversal(child, graph, visited, action)
            

def breadth_first_traversal(vertex, graph, visited, action):
    """
    BFT on adjacency list

    Args:
        vertex (int): current vertex
        graph (list[list]): adjacency list
        visited (set): visited nodes
        action (func): action function on visited node
    """
    queue = deque()
    queue.append(vertex)
    visited.add(vertex)
    while queue:
        vertex = queue.popleft()
        action(vertex)
        for child in graph[vertex]:
            if child not in visited:
                queue.append(child)
                visited.add(child)


def topological_order(vertex, graph, visited):
    pass


def djikstra(vertex, graph):
    """
    Djikstra's Shortest Paths Algorithm
    DAG with cost values, unlike the other algorithms, in format below

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
        visited (set): visited nodes
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


if __name__ == '__main__':
    visited = set()
    # depth_first_traversal(0, [[1,2],[0,2],[3],[2]], visited, print)
    # depth_first_traversal(2, [[1,2],[0,2],[3],[2]], visited, print)
    # breadth_first_traversal(0, [[1,2],[0,2],[3],[2]], visited, print)
    paths1 = djikstra(0, {0: [(1, 1), (2, 4)], 1: [(0, 1)], 2: [(0, 2)], 3:[], 4: [(3, 5), (0, 4)]})
    paths2 = djikstra(4, {0: [(1, 1), (2, 4)], 1: [(0, 1)], 2: [(0, 2)], 3:[], 4: [(3, 5), (0, 4)]})
    print(paths1, paths2)