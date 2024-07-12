class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n<=3: return n
        
        n0=2
        n1=3
        end=3
        
        while end<n:
            n2= n0+n1
            n0=n1
            n1=n2
            end+=1
        
        return n1
        


for i in range(0,7):        
    res = Solution().climbStairs(i)
    print(res)