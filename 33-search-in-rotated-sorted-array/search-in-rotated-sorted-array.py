class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # Left sorted portion
            if nums[l] <= nums[m]:
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1 
            
            # Right sorted portion 
            else: 
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1