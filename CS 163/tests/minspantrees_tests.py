# Week 2 Minimum Span Trees testing
import unittest
from src.minspantrees import prim, boruvka, kruskal

class TestMinSpanTrees(unittest.TestCase):
    # Prim's Algorithm
    # Note that while multiple MST do exist for the graph, the algorithm only provides one
    def test_prim_null(self):
        graph = {}
        MST = prim('', graph)
        self.assertEqual([], MST)

    def test_prim_straightgraph(self):
        # straight graph with same weights, very straightforward
        graph = {'A': [('B', 1)], 'B': [('A', 1), ('C', 1)], 'C': [('B', 1), ('D', 1)], 'D': [('C', 1), ('E', 1)], 'E': [('D', 1), ('F', 1)], 'F': [('E', 1), ('G', 1)], 'G': [('F', 1)]}
        MST = prim('A', graph)
        self.assertEqual(MST, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])
        
    def test_prim_simplegraph(self):
        graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
        MST = prim('A', graph)
        self.assertEqual(MST, [('A', 'D'), ('A', 'B'), ('D', 'C')])
        
    def test_prim_complexgraph_one(self):
        graph = {'A': [('B', 1), ('D', 2)], 'B': [('A', 1), ('C', 1)], 'C': [('B', 1), ('D', 1), ('F', 2)], 'D': [('C', 1), ('E', 1), ('A', 2), ('G', 2)], 'E': [('D', 1), ('F', 1), ('G', 3)], 'F': [('E', 1), ('G', 1), ('C', 2)], 'G': [('F', 1), ('D', 2), ('E', 3)]}
        MST = prim('A', graph)
        self.assertEqual(MST, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])
        
    def test_prim_complexgraph_two(self):
        graph = {'A': [('B', 3), ('D', 1)], 'B': [('A', 3), ('C', 3)], 'C': [('B', 3), ('D', 3), ('F', 1)], 'D': [('C', 3), ('E', 3), ('A', 3), ('G', 1)], 'E': [('D', 3), ('F', 3), ('G', 2)], 'F': [('E', 3), ('G', 3), ('C', 1)], 'G': [('F', 3), ('D', 1), ('E', 2)]}
        MST = prim('A', graph)
        self.assertEqual(MST, [('A', 'D'), ('D', 'G'), ('G', 'E'), ('A', 'B'), ('B', 'C'), ('C', 'F')])

    # Boruvka's Algorithm
    def test_boruvka_null(self):
        graph = {}
        MST = boruvka(graph)
        self.assertEqual([], MST)
    
    def test_boruvka_simplegraph(self):
        graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
        MST = boruvka(graph)
        self.assertEqual(MST, [('A', 'D'), ('A', 'B'), ('D', 'C')])
        
    # Kruskall's Algorithm
    def test_kruskall_null(self):
        graph = {}
        MST = kruskal(graph)
        self.assertEqual([], MST)
        
    def test_kruskal_straightgraph(self):
        graph = {'A': [('B', 1)], 'B': [('A', 1), ('C', 1)], 'C': [('B', 1), ('D', 1)], 'D': [('C', 1), ('E', 1)], 'E': [('D', 1), ('F', 1)], 'F': [('E', 1), ('G', 1)], 'G': [('F', 1)]}
        MST = kruskal(graph)
        self.assertEqual(MST, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])
    
    def test_kruskall_simplegraph(self):
        graph = {'A': [('B', 2), ('D', 1)], 'B': [('A', 2), ('D', 2)], 'C': [('D', 3)], 'D': [('A', 1), ('B', 2), ('C', 3)]}
        MST = kruskal(graph)
        self.assertEqual(MST, [('A', 'D'), ('A', 'B'), ('C', 'D')])

    def test_kruskal_complexgraph_one(self):
        graph = {'A': [('B', 1), ('D', 2)], 'B': [('A', 1), ('C', 1)], 'C': [('B', 1), ('D', 1), ('F', 2)], 'D': [('C', 1), ('E', 1), ('A', 2), ('G', 2)], 'E': [('D', 1), ('F', 1), ('G', 3)], 'F': [('E', 1), ('G', 1), ('C', 2)], 'G': [('F', 1), ('D', 2), ('E', 3)]}
        MST = kruskal(graph)
        self.assertEqual(MST, [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'G')])
        
    def test_kruskal_complexgraph_two(self):
        graph = {'A': [('B', 3), ('D', 1)], 'B': [('A', 3), ('C', 3)], 'C': [('B', 3), ('D', 3), ('F', 1)], 'D': [('C', 3), ('E', 3), ('A', 3), ('G', 1)], 'E': [('D', 3), ('F', 3), ('G', 2)], 'F': [('E', 3), ('G', 3), ('C', 1)], 'G': [('F', 3), ('D', 1), ('E', 2)]}
        MST = kruskal(graph)
        self.assertEqual(MST, [('A', 'D'), ('C', 'F'), ('D', 'G'), ('E', 'G'), ('A', 'B'), ('B', 'C')])
        
if __name__ == '__main__':
    unittest.main()