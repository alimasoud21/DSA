class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        res = -1
        for i in range(len(haystack)):
            p1 = i
            p2 = 0
            if len(needle) > len(haystack):
                break
            while p1 < len(haystack) and p2 < len(needle) and haystack[p1] == needle[p2]:
                if p2 == len(needle) - 1:
                    return i
                p1 += 1
                p2 += 1
        return res