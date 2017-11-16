from collections import deque

from util.graph_util import NodeState, GraphCycleError, GraphNode


class Graph:

    def __init__(self, starting_graph_node):
        self._starting_graph_node = starting_graph_node

    @property
    def start(self):
        return self._starting_graph_node


def breadth_first_search(starting_graph_node):
    """
    Performs breadth-first search

    :param starting_graph_node:
    :type: starting_graph_node: GraphNode

    :return: the path that bfs follows on the specified graph node head.
    :rtype: list
    """

    # Keep track of visited nodes to avoid cycles.
    visited_map = dict()

    # Keep track of path
    current_path = []

    # Using deque here for the faster O(1) pop, queue for its LIFO properties.
    queue = deque()
    queue.append(starting_graph_node)

    # Evaluate the children of the starting node.
    while queue:

        # Track the state of the children graph nodes.
        node = queue.popleft()
        process_node(visited_map, node)

        current_path.append(node.identifier)

        # Append the rest of the children to the queue.
        for child in node.children:
            queue.append(child)
        visited_map[starting_graph_node.identifier] = NodeState.VISITED

    return current_path


def depth_first_search(starting_graph_node):
    """
    Performs depth-first-search

    :param starting_graph_node:
    :type: starting_graph_node: GraphNode

    :return: the path that bfs follows on the specified graph node head.
    :rtype: list
    """

    # Keep track of visited nodes to avoid cycles.
    visited_map = dict()

    # Keep track of path
    current_path = []

    # Using stack here for its FIFO properties.
    stack = list()
    stack.append(starting_graph_node)

    # Evaluate the children of the starting node.
    while stack:

        # Track the state of the children graph nodes.
        node = stack.pop()
        process_node(visited_map, node)

        current_path.append(node.identifier)

        # Append the rest of the children to the stack.
        for child in node.children[::-1]:
            stack.append(child)
        visited_map[starting_graph_node.identifier] = NodeState.VISITED

    return current_path


def process_node(visited_map, graph_node):
    # Check for cycles.
    visited_state = visited_map.get(graph_node.identifier)
    if visited_state is not None and visited_state == NodeState.VISITING:
        raise GraphCycleError()
    visited_map[graph_node.identifier] = NodeState.VISITING


def contains_path_recursive_helper(current_node, start, end, current_path, valid_paths, visited_map):
    """
    :param current_node: the current node that is being evaluated by DFS.
    :param start: the start node for which to find a path for
    :param end: the end node for which to find a path for
    :param current_path: the current valid path of a traversal. Note this is empty if it has not found the start yet.
    :param valid_paths: a list of valid paths.
    :param visited_map: map used for cycle detection and tracking visit states.
    :return:
    """

    process_node(visited_map, current_node)

    # Check if a path has been found.
    if end == current_node.identifier and current_path:
        valid_paths.append(current_path)

    # Start tracking the path if the start node has been found.
    if start == current_node.identifier or current_path:
        current_path.append(current_node.identifier)

    # Iterate over all children and use the call stack for its LIFO properties.
    for child in current_node.children:
        child_path = current_path[:]
        contains_path_recursive_helper(child, start, end, child_path, valid_paths, visited_map)

    visited_map[current_node.identifier] = NodeState.VISITED


def contains_path(graph_start_node, start_node_id, end_node_id):
    """
    Tries to find a path given two nodes in this tree. Returns all valid appended paths in a list.
    Uses depth first search with cycle detection. Note that if the start and the end node id we consider it
    to have a trivial empty path since they are the same node.

    :param graph_start_node: The starting graph node.
    :type graph_start_node: GraphNode

    :param start_node_id: the starting node for which to find a path for.
    :type start_node_id: str

    :param end_node_id: the ending node for which to find a path for.
    :type end_node_id: str

    :return: a list of valid paths starting from the start_node_id to the end_node_id
    :rtype: list

    :raises: GraphCycleError
    """

    # Keep track of visited nodes to avoid cycles.
    visited_map = dict()

    # Keep track of the current path
    current_path = []

    # Keep track of the valid path
    valid_paths = []

    contains_path_recursive_helper(graph_start_node, start_node_id, end_node_id, current_path, valid_paths,
                                   visited_map)
    return valid_paths


