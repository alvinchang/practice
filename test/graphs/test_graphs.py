import unittest

from graphs.traversals import breadth_first_search, depth_first_search
from util.graph_util import generate_graph, GraphCycleError


class TestGraph(unittest.TestCase):

    def test_basic_bfs(self):
        graph = TestGraph.create_basic_adjacency_map()
        actual = breadth_first_search(graph)
        expected = ["A", "B", "C", "D", "E", "X"]
        self.assertTrue(actual == expected)

    def test_basic_dfs(self):
        graph = TestGraph.create_basic_adjacency_map()
        actual = depth_first_search(graph)
        expected = ["A", "B", "C", "D", "X", "E"]
        self.assertTrue(actual == expected)

    def test_basic_bfs_handles_cycle(self):
        cyclic_graph = TestGraph.create_basic_cyclic_adjacency_map()
        try:
            breadth_first_search(cyclic_graph)
            self.fail("Did not detect a cycle.")
        except GraphCycleError:
            pass

    def test_basic_dfs_handles_cycle(self):
        cyclic_graph = TestGraph.create_basic_cyclic_adjacency_map()
        try:
            depth_first_search(cyclic_graph)
            self.fail("Did not detect a cycle.")
        except GraphCycleError:
            pass

    @staticmethod
    def create_basic_adjacency_map():
        """

           Sample adjacency map
                    A
                   / \
                  B   C
                      /\
                     D  E
                    /
                    X

        """
        sample_adj_map = {
            "A": ["B", "C"],
            "C": ["D", "E"],
            "D": ["X"]
        }
        graph = generate_graph(sample_adj_map, node_start_name="A")
        return graph

    @staticmethod
    def create_basic_cyclic_adjacency_map():
        """

           Sample graph with cycle
                       A
                      / \
                     B   C
                         /\
                        D-E
        """
        sample_adj_map = {
            "A": ["B", "C"],
            "C": ["D"],
            "D": ["E"],
            "E": ["C"]
        }
        graph = generate_graph(sample_adj_map, node_start_name="A")
        return graph





