import graph

social = [("Jill", "New York"), ("Jill", "Toronto"), ("Jill", "London"), ("Jack", "France"), ("Jack", "New York"),
          ("John", "Berlin"), ("John", "London"), ("Jacob", "New York"), ("Joan", "Toronto")]

city_graph = {}

for (x,y) in social: print graph.make_link(city_graph, x, y)


def short_path(G, node1, node2):
    """
    :return: shortest path from node1 to node2
    """
    dist_from_start = {}
    stackoverflow = [node1]
    dist_from_start[node1] = [node1]
    while len(stackoverflow) > 0:
       current = stackoverflow[0]
       del stackoverflow[0]
       for neighbor in G[current].keys():
           if neighbor not in dist_from_start:
               dist_from_start[neighbor] = dist_from_start[current] + [neighbor]
               if neighbor == node2:
                   return dist_from_start[node2]
               stackoverflow.append(neighbor)
    return False


def centrality(G, node):
    """
    :return: The average distance from the node to all other nodes in the graph
    """
    dist_from_start = {}
    stackoverflow = [node]
    dist_from_start[node] = 0
    while len(stackoverflow) > 0:
       current = stackoverflow[0]
       del stackoverflow[0]
       for neighbor in G[current].keys():
           if neighbor not in dist_from_start:
               dist_from_start[neighbor] = dist_from_start[current] + 1
               stackoverflow.append(neighbor)
    return (sum(dist_from_start.values()) + 0.0) / len(dist_from_start)


print short_path(city_graph, "Joan", "John")

print centrality(city_graph, "Joan")
print centrality(city_graph, "Jill")
