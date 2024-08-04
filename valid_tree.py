from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        conn_map={i:[] for i in range(n)}

        for node,edge in edges:
            conn_map[node].append(edge)
            conn_map[edge].append(node)

        visit=set()
        def dfs(node,prev):
            if node in visit:
                return False
            
            visit.add(node)

            for adj in conn_map[node]:
                if adj == prev:
                    continue
                if not dfs(adj,node):
                    return False
            return True
            
        return dfs(0,-1) and n==len(visit)
    
    
print(Solution().validTree(5,[[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().validTree(5,[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
# print(Solution().validTree(5,[[0,1],[2,1],[3,2],[3,1],[4,1]]))