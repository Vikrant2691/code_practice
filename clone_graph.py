from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #1. create a HashMap
        dict = {}
        #2. pass first node to dfs(node)->node
        def dfs(node: Optional['Node']) -> Optional['Node']:
            #3. if node exists in hash map
            if node.val in dict:
                return dict.get(node.val)
            #else
            #4. create a node
            new_node = Node()
            new_node.val=node.val
            dict[node.val]=new_node
            #6. cpy neighbors by for each neighbor_node append(dfs(neighbor_node))
            for n in node.neighbors:
                new_node.neighbors.append(dfs(n))
                
            return new_node
        
        
                
        return dfs(node) if node else None
                
# Create nodes for each element in the adjacency list
nodes = [Node(i) for i in range(1, 4)]

# Define the adjacency list
adjList = [[2], [1, 3], [2]]

# Populate the neighbors for each node
for i in range(len(adjList)):
    nodes[i].neighbors = [nodes[j-1] for j in adjList[i]]
    
    
res = Solution().cloneGraph(nodes[0])


print(res)