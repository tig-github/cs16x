# min-span tree algorithms
# corresponds to Week 2 of CS 163 https://ics.uci.edu/~eppstein/163/
# uses adjacency list representations with weights
import heapq
from collections import defaultdict


def verify_undirected(graph):
    """
    Verifies that the graph is undirected, ie it is a DAG where every vertex with an edge to another has a corresponding return edge
    Used for testing the input is valid
    
    Args:
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    members = defaultdict(list)
    for vertex,edges in graph.items():
        for edge in edges:
            members[vertex].append(edge[0])
            
    for vertex,edges in graph.items():
        for edge in edges:
            if vertex not in members[edge[0]]:
                return False
    return True


def prim(start_vertex, graph):
    """
    Prim's Minimum Spanning Tree Algorithm
    Undirected graph with cost values
    Analysis: O(mlogn) | O(m + nlogn) with fibonacci heap

    Args:
        start_vertex (int): vertex to initialize prim's on
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    if not graph: return None
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
        
        
# Union Find Primitives - abstracted into a class later
def find(forest, node):
    # determines root of the node's tree
    # with path compression
    if forest[node] == -1:
        return node
    else:
        root =  find(forest, forest[node])
        forest[node] = root
        return root

def union(forest, node1, node2):
    # merges two trees
    root1 = find(forest, node1)
    root2 = find(forest, node2)
    if root1 != root2:
        forest[root1] = root2
        

def boruvka(graph):
    """
    Boruvka's Minimum Spanning Tree Algorithm
    Undirected graph with cost values
    Assumes keys form a total order in this implementation
    Analysis: O(mlogn)

    Args:
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    assert verify_undirected(graph), 'Ensure the input is an undirected graph, and not a directed graph'
    
    min_span_forest = [(v,{}) for v in graph]
    completed = False


def kruskal(graph):
    """
    Kruskal's Minimum Spanning Tree Algorithm
    Undirected graph with cost values
    Assumes keys form a total order in this implementation
    Analysis: O(mlogn)

    Args:
        graph (dict[list(tuple)]): adjacency list of form vertex: (outgoing vertex, weight)
    """
    assert verify_undirected(graph), 'Ensure the input is an undirected graph, and not a directed graph'

    ids = {k:i for i,k in enumerate(graph.keys())} # maps to keys
    forest = [-1 for _ in range(len(graph))] # -1 implies no parent
    edges = []
    for vertex,E in graph.items():
        for edge in E:
            edges.append((vertex, edge))    
    pruned_edges = []
    covered_edges = set()
    for edge in sorted(edges, key=lambda x:x[1]): # prune for repeated more expensive edges
        if (edge[0], edge[1][0]) not in covered_edges:
            pruned_edges.append(edge)
            covered_edges.add((edge[0], edge[1][0]))
            covered_edges.add((edge[1][0], edge[0]))        
    for edge in pruned_edges:
        union(forest, ids[edge[0]], ids[edge[1][0]])
    return forest
    
if __name__ == '__main__':
    graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
    mst = prim('A', graph)
    #mst = kruskal(graph)
    print('mst=', mst) # two valid MSTs for this graph