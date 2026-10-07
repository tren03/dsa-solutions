TC =
SC = 
# the top down solution 5:51 min
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def rec(i, j):
            if dp.get((i, j)) is not None:
                return dp[(i,j)]
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            
            a = rec(i, j+1)
            b = rec(i+1, j)

            dp[(i,j)] = a+b
            return a + b
        return rec(0,0)


TC = O(MN)
SC = O(MN)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up soln
        dp = []
        for i in range(m):
            dp.append([])
            for j in range(n):
                dp[i].append(0)
        dp[m-1][n-1] = 1

        for i in range(m-1,-1,-1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                nos_right = 0
                if j+1 < n:
                    nos_right = dp[i][j+1]

                nos_down = 0
                if i+1 < m:
                    nos_down = dp[i+1][j]
                
                dp[i][j] = nos_right + nos_down

        print(dp)
        
        return dp[0][0]
                

TC = O(MN)
SC = o(N)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up soln space optimzied
        cur = 1
        right = 0
        down = []
        for i in range(n):
            down.append(0)
        down[-1] = 1
        
        for i in range(m-1,-1,-1):
            right = 0
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    right = cur
                    continue
                cur = right + down[j]
                right = cur
                down[j] = cur
                print(i,j,cur, down)
        return cur
        
