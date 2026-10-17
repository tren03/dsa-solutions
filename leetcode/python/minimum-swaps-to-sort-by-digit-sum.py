"""
**Time: O(n log n)**
- Digit sums: O(n·d), d ≤ 10, so O(n)
- Sort tuples: O(n log n), dominates
- Build map: O(n)
- Swap loop: O(n) amortized, since each swap fixes one element permanently (at most n-1 swaps total)

**Space: O(n)**
- Tuple list `s`: O(n)
- Map `m`: O(n)
- `nums` is modified in place: no extra array

(Constants like 2n or 3n drop out in big-O.)
"""
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digisum(nos) -> int:
            ans = 0
            while nos:
                ans += nos % 10
                nos = nos // 10
            return ans
                

        s = []
        for ind, i in enumerate(nums):
            s.append((digisum(i), i))

        s.sort()

        m = {}
        for ind, i in enumerate(s):
            m[i[1]] = ind
        
        ans = 0
        for ind in range(len(nums)):
            while nums[ind] != nums[m[nums[ind]]]:
                print(nums[ind], nums[m[nums[ind]]])
                ans += 1
                cur = nums[ind]
                val_to_swap = nums[m[nums[ind]]]

                nums[ind] = nums[m[nums[ind]]]
                nums[m[cur]] = cur
        return ans


