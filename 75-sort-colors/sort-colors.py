class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 0 - red
        # 1 - white
        # 2 - blue
        # 0 - 1 - 2
        count = {
            0 : 0,
            1 : 0,
            2 : 0,
        }

        for number in nums:
            count[number] += 1
        
        index = 0

        for number in range(0,3):
            while count[number] > 0:
                nums[index] = number
                index += 1
                count[number] -= 1

        