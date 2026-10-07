# top down solution
TC
o(N.M) - since each step reached only once due to memoization

SC
dp dict: O(N·M)
stack: O(N+M)
total: O(N·M + N + M) = O(N·M)
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = {}

        def rec(i, cur_amt):
            if dp.get((i,cur_amt)) is not None:
                return dp[(i, cur_amt)]
            if i >= len(coins):
                return 0
            if cur_amt > amount:
                return 0
            if cur_amt == amount:
                return 1
            a = rec(i, cur_amt+coins[i])
            b = rec(i+1, cur_amt)
            dp[(i, cur_amt)] = a+b
            return a+b

        return rec(0,0)

# bottom up solution
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = []
        for i in range(len(coins)):
            dp.append([])
            for j in range(amount+1):
                if j == amount:
                    dp[i].append(1)
                else:
                    dp[i].append(0)

        for i in range(len(coins)-1, -1, -1):
            for j in range(amount-1, -1, -1):
                a = 0
                b = 0
                if i+1 < len(coins):
                    a = dp[i+1][j]
                if j+coins[i] <= amount:
                    b = dp[i][j+coins[i]]
                dp[i][j] = a + b
        return dp[0][0]

# bottom up space optimzed
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = []
        for j in range(amount+1):
            if j == amount:
                dp.append(1)
            else:
                dp.append(0)

        for i in range(len(coins)-1, -1, -1):
            cur_coin = coins[i]
            for j in range(amount-1,-1,-1):
                a = 0
                b = 0
                if j+coins[i] <= amount:
                   a = dp[j+coins[i]]
                b = dp[j] # row i holds the prev value before update
                dp[j] = a+b
        return dp[0]


        
