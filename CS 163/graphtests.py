"""
For now, unittesting for graph algorithms
will assume the input is an adjacency list, with or 
without costs depending on the algorithm. If the algorithm
relies on a graph being undirected, the algorithm itself runs
this verification currently. In the future, graph representations
will be abstracted to a class that allows multiple representations, and
the algorithms ideally will be all made to work with each representation.
File will likely be split into each week with each week being a Python module.
"""

import unittest


class TestGraphAlgorithms(unittest.TestCase):
    # Week 1
    def test_tarjan(self):
        self.assertEqual(-1,-1)
        
    # Week 2
    def test_prim(self):
        self.assertEqual(-1,-1)
        
    def test_boruvka(self):
        self.assertEqual(-1,-1)
        
    def test_kruskall(self):
        self.assertEqual(-1,-1)
        
    # Week 3
    
    def test_dijkstra(self):
        self.assertEqual(-1,-1)
        
    def test_bellmanford(self):
        self.assertEqual(-1,-1)
        
    def test_johnson(self):
        self.assertEqual(-1,-1)
        
    def test_surballe(self):
        self.assertEqual(-1,-1)

    def test_astar(self):
        self.assertEqual(-1,-1)

        
if __name__ == '__main__':
    unittest.main()