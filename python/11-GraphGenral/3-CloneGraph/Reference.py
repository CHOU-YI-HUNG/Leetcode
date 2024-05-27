
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = [False] * 200
        old_graph = [None for i in range(200)]
        new_graph = []
        for i in range(200):
            new_graph.append(Node(val = i))
        if node == None:
            return
        add_nodes(node, old_graph, visited)
        for i in range(200):
            if visited[i]:
                for neighbor in old_graph[i].neighbors:
                    new_graph[i].neighbors.append(new_graph[neighbor.val])
        return new_graph[node.val]
    
def add_nodes(node, old_graph, visited):
    if visited[node.val]:
        return
    old_graph[node.val] = node
    visited[node.val] = True
    for neighbor in node.neighbors:
        add_nodes(neighbor, old_graph, visited)