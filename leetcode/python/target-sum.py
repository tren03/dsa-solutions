class Solution:
	"""
    State: (i, cur_sum) = number of ways to finish from index i given the running sum.
    cur_sum ranges over [-S, S] where S = sum(nums), so there are at most 2S + 1
    distinct sums per index, independent of target.

    TC = O(N * S), each state is computed once with O(1) work
    SC = O(N * S) for the memo, plus O(N) recursion stack
    """"""
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp = {}

        def rec(i , cur_sum):
            if i >= len(nums) and target == cur_sum:
                return 1
            if i >= len(nums):
                return 0
            if dp.get((i, cur_sum)) is not None:
                return dp[(i, cur_sum)]

            cur = nums[i]
            a = rec(i+1, cur_sum+cur)
            b = rec(i+1, cur_sum-cur)
            dp[(i,cur_sum)] = a+b
            return a+b
        return rec(0, 0)


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        
        dp = []
        s = sum(nums)
        for i in range(len(nums)+1):
            dp.append([])
            for j in range(2*sum(nums)+1):
                if j == sum(nums)+target:
                    #print(i,j)
                    dp[i].append(1)
                else:
                    dp[i].append(0)
        # dp[i,cur_sum]
        # = dp[i+1, cur_sum+n[i]] + dp[i+1, cur_sum-n[i]]
        # we need the lower row for calc.

        for i in range(len(nums)-1,-1,-1):
            for j in range(2*sum(nums), -1, -1):
                j_converted = j - sum(nums)
                
                j_add = j_converted + nums[i]
                j_sub = j_converted - nums[i]

                j_add_converted = j_add + sum(nums)
                j_sub_converted = j_sub + sum(nums)

                a = 0
                b = 0
                if j_add_converted <= 2*sum(nums):
                    #print(i+1, j_add_converted)
                    a = dp[i+1][j_add_converted]
                if j_sub_converted >= 0:
                    b = dp[i+1][j_sub_converted]
                dp[i][j] = a+b
        #print(dp)
        return dp[0][sum(nums)]

        
