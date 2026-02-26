class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        temp = []
        for n in nums1:
            if n not in temp:
                temp.append(n)
        
        for n in nums2:
            if (n in temp) and (n not in res):
                res.append(n)
        
        return res


            

