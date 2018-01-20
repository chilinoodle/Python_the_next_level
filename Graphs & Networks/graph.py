def make_link(Graph, node1, node2):
    """
    Graph: dict, key is actual node, values: neighboring nodes.
    These nodes will be a dictionary of neighbor nodes.
    The nodes' dict's key will be the neighbor node and its value will be 1
    :returns: updated graph
    """
    if node1 not in Graph:
        Graph[node1] = {}
    (Graph[node1])[node2] = 1
    if node2 not in Graph:
        Graph[node2] = {}
    (Graph[node2])[node1] = 1
    return Graph


connected_letters = []
G = {}
connected_letters.append(("a","g"))
connected_letters.append(("a","d"))
connected_letters.append(("d","g"))
connected_letters.append(("g","c"))
connected_letters.append(("b","f"))
connected_letters.append(("f","e"))
connected_letters.append(("e","h"))


for (x,y) in connected_letters: print make_link(G,x,y)


def marked_node(Graph, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in Graph[node]:
        if neighbor not in marked:
            total_marked += marked_node(Graph, neighbor, marked)
    return total_marked


def list_node_sizes(Graph):
    marked = {}
    for node in Graph.keys():
        if node not in marked:
            print "Graph containing", node, ":", marked_node(Graph, node, marked)


list_node_sizes(G)