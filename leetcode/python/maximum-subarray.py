class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # if my sum goes negetive, 
        # there is no point of me moving it forward, as it 
        # always reduces the max answer
        # so we can just skip the running sum and start freshk
        ans = nums[0]
        temp = 0
        i = 0

        for i in nums:
            temp += i
            if temp < 0:
                # discard running sum
                ans = max(ans, temp)
                temp = 0
            else:
                ans = max(ans, temp)
        return ans
