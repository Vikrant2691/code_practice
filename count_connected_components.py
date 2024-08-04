from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = {i:[] for i in range(n)}

        for n1,n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        visited= set()
        res=0
        
        def dfs(node,prev)->int:
            if node in visited:
                return 0
            visited.add(node)
            for adj_n in adj_list[node]:
                if adj_n==prev:
                    continue
                dfs(adj_n,node)
            return 1
            

        for node in range(n):
            res+=dfs(node,-1)
        
        return res