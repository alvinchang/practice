from collections import deque

from graph_util import GraphNode, generate_graph, NodeState, GraphCycleError


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

        current_path.append(node.name)

        # Append the rest of the children to the queue.
        for child in node.children:
            queue.append(child)
        visited_map[starting_graph_node.name] = NodeState.VISITED

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

        current_path.append(node.name)

        # Append the rest of the children to the stack.
        for child in node.children[::-1]:
            stack.append(child)
        visited_map[starting_graph_node.name] = NodeState.VISITED

    return current_path


def process_node(visited_map, graph_node):
    # Check for cycles.
    visited_state = visited_map.get(graph_node.name)
    if visited_state is not None and visited_state == NodeState.VISITING:
        raise GraphCycleError()
    visited_map[graph_node.name] = NodeState.VISITING


if __name__ == "__main__":
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

    path = breadth_first_search(graph)
    expected = ["A", "B", "C", "D", "E", "X"]
    assert(path == expected)

    path = depth_first_search(graph)
    expected = ["A", "B", "C", "D", "X", "E"]
    assert(path == expected)


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

    try:
        breadth_first_search(graph)
    except GraphCycleError as e:
        print 'pass cycle test'
        pass

    try:
        depth_first_search(graph)
    except GraphCycleError as e:
        print 'pass cycle test'
        pass
