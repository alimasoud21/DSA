class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        prev_nums = {}
        
        for i,number in enumerate(nums) :
            diff = target - number
            if diff in prev_nums:
                return [prev_nums[diff], i]
            prev_nums[number] = i

