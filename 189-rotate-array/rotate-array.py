class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n   # handle k > n
        new = [0] * n
        
        for i in range(n):
            new[(i + k) % n] = nums[i]   # ✅ handles wrap-around automatically
        
        for i in range(n):
            nums[i] = new[i]