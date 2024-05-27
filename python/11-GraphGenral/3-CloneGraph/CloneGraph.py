
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def buildGraph(adjList):    
    NodeList=[]
    for i in range(1,len(adjList)+1):
        NodeList.append(Node(i))
    for i in range(len(adjList)):
        for index in adjList[i]:
            (NodeList[i]).neighbors.append(NodeList[index-1])
    
    return NodeList[0]

def dfsGraph(node):
    if node.val=='*': return 
    print(node.val)
    node.val='*'
    for i in  range(len(node.neighbors)):
        dfsGraph(node.neighbors[i])


def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    HashTable={}
    def dfsGraph(node):
        if node.val in HashTable: 
            return HashTable[node.val]
        #
        NewNode=Node(node.val)
        HashTable[node.val]=NewNode
        #            
        for i in  range(len(node.neighbors)):
            NewNode.neighbors.append(dfsGraph(node.neighbors[i]))
                        
        return NewNode
    
    return dfsGraph(node)
            
node=buildGraph([[2,4],[1,3],[2,4],[1,3]])

dfsGraph(cloneGraph(node))



