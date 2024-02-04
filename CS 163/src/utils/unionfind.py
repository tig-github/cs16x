class UnionFind:
    """
    UnionFind class implementation
    """
    def __init__(self, forest = []) -> None:
        self.forest = forest
    
    def find(self, forest, node):
        # determines root of the node's tree
        # with path compression
        if forest[node] == -1:
            return node
        else:
            root =  self.find(forest, forest[node])
            forest[node] = root
            return root

    def union(self, forest, node1, node2):
        # merges two trees
        root1 = self.find(forest, node1)
        root2 = self.find(forest, node2)
        if root1 != root2:
            forest[root1] = root2