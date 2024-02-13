# Week 3 Shortest Paths testing

import unittest
from src.shortestpath import dijkstra, bellman_ford, johnson, suurballe, a_star

class TestMinSpanTrees(unittest.TestCase):
    # Dijkstra's Algorithm
    def test_dijkstra_null(self):
        graph = {}
        distances,predecessors = dijkstra('', graph)
        self.assertEqual([], distances)
        self.assertEqual([], predecessors)
        
    def test_dijkstra_straightgraph(self):
        graph = {1: [(2, 1), (0, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1), (4, 1)], 4: [(3, 1), (5, 1)], 5: [(4, 1), (6, 1)], 6: [(5, 1), (7, 1)], 7: [(6, 1)], 0: [(1, 1)]}
        distances,predecessors = dijkstra(1, graph)
        self.assertEqual([1, 0, 1, 2, 3, 4, 5, 6], distances)
        self.assertEqual([1, None, 1, 2, 3, 4, 5, 6], predecessors)
        
    # Johnson's Algorithm
    def test_johnson_null(self):
        graph = {}
        distances,predecessors = johnson('', graph)
        self.assertEqual([], distances)
        self.assertEqual([], predecessors)
        
    def test_johnson_straightgraph(self):
        graph = {1: [(2, 1), (0, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1), (4, 1)], 4: [(3, 1), (5, 1)], 5: [(4, 1), (6, 1)], 6: [(5, 1), (7, 1)], 7: [(6, 1)], 0: [(1, 1)]}
        distances,predecessors = johnson(1, graph)
        self.assertEqual([1, 0, 1, 2, 3, 4, 5, 6], distances)
        self.assertEqual([1, None, 1, 2, 3, 4, 5, 6], predecessors)
        
    # A* Algorithm
    def test_astar_null(self):
        graph = {}
        distances,predecessors = a_star('', graph, lambda x,y:1)
        self.assertEqual([], distances)
        self.assertEqual([], predecessors)
        
    def test_astar_straightgraph_empty_heuristic(self):
        graph = {1: [(2, 1), (0, 1)], 2: [(1, 1), (3, 1)], 3: [(2, 1), (4, 1)], 4: [(3, 1), (5, 1)], 5: [(4, 1), (6, 1)], 6: [(5, 1), (7, 1)], 7: [(6, 1)], 0: [(1, 1)]}
        distances,predecessors = a_star(1, graph, lambda x,y:1)
        self.assertEqual([1, 0, 1, 2, 3, 4, 5, 6], distances)
        self.assertEqual([1, None, 1, 2, 3, 4, 5, 6], predecessors)
        
if __name__ == '__main__':
    unittest.main()