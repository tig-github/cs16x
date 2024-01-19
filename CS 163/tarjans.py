# tarjans algorithm
# first with an adjacency list, with the wikipedia algorithm
# handles bookkeeping independently of vertices

def strong_connect(vertex, graph, stack, stack_members, smallest_index, index, lowlink):
    index[vertex] = smallest_index
    lowlink[vertex] = smallest_index
    smallest_index += 1
    for edges in graph[vertex]:
        for successor in edges:
            if index[successor] == 'unknown':
                strong_connect(successor)
                lowlink[vertex] = min(lowlink[vertex], lowlink[successor])
            elif successor in stack_members:
                lowlink[vertex] = min(lowlink[vertex], index[successor])

    if lowlink[vertex] == index[vertex]:
        SCC = []
        def subroutine(SCC):
            successor = stack.pop()
            stack_members.remove(successor)
            SCC.append(successor)
            return successor
        while vertex != successor:
            successor = subroutine(SCC)
        print(SCC)

def tarjan(graph):
    smallest_index = 0
    index = ['unknown' for _ in range(len(graph))]
    lowlink = [float('inf') for _ in range(len(graph))] # smallest idx of nodes predecessor
    stack = []
    stack_members = {} # for easy lookup
    for v in graph:
        if index[v] == 'unknown':
            strong_connect(v, graph, stack, stack_members, smallest_index, index, lowlink)