class Solution:
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        s = list(s)
        
        for ch in s:
            unique[ch] = unique.get(ch, 0) + 1
        
        for i, ch in enumerate(s):
            if unique[ch] == 1:
                return i
        
        return -1