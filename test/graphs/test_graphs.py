import unittest

from graphs.traversals import breadth_first_search, depth_first_search, contains_path
from util.graph_util import generate_graph, GraphCycleError


class TestGraph(unittest.TestCase):

    def test_basic_bfs(self):
        graph = TestGraph.create_basic_adjacency_map_1()
        actual = breadth_first_search(graph)
        expected = ["A", "B", "C", "D", "E", "X"]
        self.assertTrue(actual == expected)

    def test_basic_dfs(self):
        graph = TestGraph.create_basic_adjacency_map_1()
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

    def test_contains_path_from_root(self):
        graph = TestGraph.create_basic_adjacency_map_1()
        valid_paths = contains_path(graph, "A", "X")
        expected_path = ["A", "C", "D", "X"]
        self.assertTrue(expected_path in valid_paths)
        self.assertTrue(len(valid_paths) == 1)

    def test_contains_multiple_paths(self):
        graph = TestGraph.create_basic_adjacency_map_3()

        valid_paths = contains_path(graph, "C", "Z")

        expected_path_1 = ["C", "D", "X", "Z"]
        expected_path_2 = ["C", "D", "Y", "Z"]
        expected_path_3 = ["C", "E", "X", "Z"]

        self.assertTrue(expected_path_1 in valid_paths)
        self.assertTrue(expected_path_2 in valid_paths)
        self.assertTrue(expected_path_3 in valid_paths)
        self.assertTrue(len(valid_paths) == 3)

    def test_contains_no_path(self):
        graph = TestGraph.create_basic_adjacency_map_1()

        valid_paths = contains_path(graph, "B", "X")
        self.assertTrue(not valid_paths)

    def test_contains_dne(self):
        graph = TestGraph.create_basic_adjacency_map_1()

        valid_paths = contains_path(graph, "dne1", "dne2")
        self.assertTrue(not valid_paths)

    def test_contains_same_start_and_end(self):
        graph = TestGraph.create_basic_adjacency_map_1()

        valid_paths = contains_path(graph, "C", "C")
        self.assertTrue(not valid_paths)

    @staticmethod
    def create_basic_adjacency_map_3():
        """

           Sample adjacency map
                    A
                   / \
                  B   C
                      /\
                     D  E
                    / \ /
                    Y  X
                     \/
                     Z

        """
        sample_adj_map = {
            "A": ["B", "C"],
            "C": ["D", "E"],
            "D": ["X", "Y"],
            "E": ["X"],
            "X": ["Z"],
            "Y": ["Z"]
        }
        graph = generate_graph(sample_adj_map, node_start_name="A")
        return graph

    @staticmethod
    def create_basic_adjacency_map_2():
        """

           Sample adjacency map
                    A
                   / \
                  B   C
                      /\
                     D  E
                     \ /
                      X

        """
        sample_adj_map = {
            "A": ["B", "C"],
            "C": ["D", "E"],
            "D": ["X"],
            "E": ["X"]
        }
        graph = generate_graph(sample_adj_map, node_start_name="A")
        return graph

    @staticmethod
    def create_basic_adjacency_map_1():
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
                         /\\
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
