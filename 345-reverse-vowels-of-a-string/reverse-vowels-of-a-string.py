class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        vowels = set("aeiouAEIOU")

        l, r = 0, len(s) - 1
        
        while l < r:

            while l < r and res[l] not in vowels:
                l += 1
            
            while l < r and res[r] not in vowels:
                r -= 1
            
            res[l], res[r] = res[r], res[l]

            l += 1
            r -= 1
        
        return "".join(res)
        

        