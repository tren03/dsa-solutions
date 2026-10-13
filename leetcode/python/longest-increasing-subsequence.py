# TC = o(n*log(n))
# SC = o(n)
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # need more intuition understanding
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                continue

            # do bs to find element to replace 
            l = 0
            r = len(dp)-1
            while l<=r:
                mid = (l+r)//2
                v = dp[mid]
                if v == nums[i]:
                    l = mid
                    break
                
                if nums[i] < v:
                    r = mid-1
                else:
                    l = mid+1
            
            # replace with l, as that is value where it should insert
            dp[l] = nums[i]
        
        return len(dp)

# SC = o(n)
# TC = o(n^2) -> n(n-1)(n-2)... approx is equal = n^2
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                dp[i] = 1
                continue
            
            # need to calc dp[i]
            dp[i] = 1
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        print(dp)
        return max(dp)
            
        
