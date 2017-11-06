from enum import Enum


class GraphNode:

    def __init__(self, name):
        """
        Creates a node with the given name.

        :param name:
        :type name: str

        """
        self._name = name
        self._children = []

    def add_child(self, node):
        """
        Adds the specified node to be a child of the current node.

        :param node:
        :type node: GraphNode

        """
        self._children.append(node)

    @property
    def name(self):
        """
        :rtype: str
        """
        return self._name

    @property
    def children(self):
        """
        :rtype: list
        """
        return self._children


class NodeState(Enum):
    UNVISITED = 0
    VISITING = 1
    VISITED = 2


class GraphCycleError(ValueError):
    pass


def generate_graph(adj_map, node_start_name):
    """

    Ex.
      A: [B, C]
      C: [D]

    will create a graph that looks like:

            A
           / \
          B   C
              \
               D

    :param adj_map: the adjacency map used as a basis to create the graph.
    :type adj_map: dict

    :param node_start_name
    :type node_start_name: str

    :return: the beginning node pertaining to the specified adjacency map.
    :rtype: GraphNode

    """

    if node_start_name not in adj_map:
        raise ValueError("Could not find starting node in adjacency map")

    node_name_set = set(node_start_name)
    for children_list in adj_map.itervalues():
        child_set = set(children_list)
        node_name_set.update(child_set)

    # Create all nodes as to adjust pointers between them to create the graph.
    node_map = {node_name: GraphNode(node_name) for node_name in node_name_set}

    # Iterate through each node and set its children accordingly.
    for node_name, node_children_name_list in adj_map.iteritems():
        current_node = node_map[node_name]
        for node_child_name in node_children_name_list:
            child_node = node_map[node_child_name]
            current_node.add_child(child_node)

    starting_node = node_map[node_start_name]
    return starting_node


if __name__ == "__main__":

    sample_adj_map = {
        "A": ["B", "C"],
        "C": ["D", "E"],
        "D": ["X"]
    }
    graph = generate_graph(sample_adj_map, node_start_name="A")

