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


def topological_order(vertex, graph, visited, action):
    pass

def djikstra(vertex, graph, visited, action):
    pass


if __name__ == '__main__':
    visited = set()
    depth_first_traversal(0, [[1,2],[0,2],[3],[2]], visited, print)
    depth_first_traversal(2, [[1,2],[0,2],[3],[2]], visited, print)
    breadth_first_traversal(0, [[1,2],[0,2],[3],[2]], visited, print)
