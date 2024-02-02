# Week 3 Shortest Paths testing

import unittest
from src.shortestpath import dijkstra, bellman_ford, johnson, suurballe, a_star

class TestMinSpanTrees(unittest.TestCase):
    # Dijkstra's Algorithm
    def test_dijkstra_null(self):
        graph = {}
        distances,predecessors = dijkstra('', graph)
        self.assertEqual(None, distances)
        self.assertEqual(None, predecessors)