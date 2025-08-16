class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i,numbere in enumerate(nums):
            ans.insert(i,numbere)
            ans.insert(i+n,numbere)
        return ans