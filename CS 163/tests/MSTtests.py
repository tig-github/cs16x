# Week 2 Minimum Span Trees testing

import unittest
from src.minspantrees import prim, boruvka
from src.utils.graph import Graph

class TestMinSpanTrees(unittest.TestCase):
    # Prim's Algorithm
    def test_prim_null(self):
        graph = {}
        MST = prim('', graph)
        self.assertEqual(None, MST)
    
    def test_prim_simplegraph(self):
        # Note that while multiple MST do exist for the graph, the algorithm only provides one
        graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
        MST = prim('A', graph)
        self.assertEqual(MST, [('A', 'D'), ('A', 'B'), ('D', 'C')])
        
    # Boruvka's Algorithm
    def test_boruvka_null(self):
        graph = {}
        MST = boruvka('', graph)
        self.assertEqual(None, MST)
    
    def test_boruvka_simplegraph(self):
        graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
        MST = boruvka('A', graph)
        self.assertEqual(MST, [('A', 'D'), ('A', 'B'), ('D', 'C')])
        
    # Kruskall's Algorithm
    def test_kruskall_null(self):
        graph = {}
        MST = boruvka('', graph)
        self.assertEqual(None, MST)
    
    def test_kruskall_simplegraph(self):
        graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
        MST = boruvka('A', graph)
        self.assertEqual(MST, [('A', 'D'), ('A', 'B'), ('D', 'C')])

        
if __name__ == '__main__':
    unittest.main()