class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
       l, sum = 0, 0
       res = float("inf")

       for r in range(len(nums)):
        sum += nums[r]
        while sum >= target:
            res = min(r - l + 1, res)
            sum -= nums[l]
            l += 1
           
       return 0 if res == float("inf") else res