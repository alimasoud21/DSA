class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = 0, 0
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        if len(ransomNote) > len(magazine):
            return False
        for r in range(len(ransomNote)):
            if ransomNote[r] in magazine:
                magazine.remove(ransomNote[r])
                r += 1 
            else:
                return False
        return True

