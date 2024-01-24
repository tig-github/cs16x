# min-span tree algorithms
# corresponds to Week 2 of CS 163 https://ics.uci.edu/~eppstein/163/
# uses adjacency list representations with weights
import heapq

def verify_undirected(graph):
    """
    Verifies that the graph is undirected, ie it is a DAG where every vertex with an edge to another has a corresponding return edge
    Used for testing the input is valid
    
    Args:
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    return True

def prim(start_vertex, graph):
    """
    Prim's Minimum Spanning Tree Algorithm
    Undirected graph with cost values

    Args:
        vertex (int): current vertex
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
        visited (set): visited nodes
    """
    assert verify_undirected(graph), 'Ensure the input is an undirected graph, and not a directed graph'
    
    min_span_tree = [] # list of edges in form (A, B) for vertices A,B with an edge
    tree_members = {start_vertex} # tracks visited
    previous_vertex = start_vertex
    priority_queue = []
    heapq.heappush(priority_queue, (0, start_vertex, start_vertex))
    n = len(graph)
    while priority_queue:
        if len(min_span_tree) == n: # n-1, but it has an extra edge
            break
        _,current_vertex,previous_vertex = heapq.heappop(priority_queue) # we no longer need the 'score' gotten via the edge weight
        if current_vertex not in tree_members:
            min_span_tree.append((previous_vertex, current_vertex))
            tree_members.add(current_vertex)
        for neighbor in graph[current_vertex]:
            if neighbor[0] not in tree_members:
                heapq.heappush(priority_queue, (neighbor[1], neighbor[0], current_vertex))
        
        
    return min_span_tree[0:] # we don't need the first self edge
        

def boruvka(graph):
    pass

def kruskal(graph):
    pass


if __name__ == '__main__':
    visited = set()
    mst = prim('A', {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]})
    print('mst=', mst) # two valid MSTs for this graph