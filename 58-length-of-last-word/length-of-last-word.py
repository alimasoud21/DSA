class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        text = s.strip()
        if len(text) == 1:
            return 1
        for i in range(len(text) - 1 , -1, -1):
            if text[i] != " " :
                count += 1
            else:
                break
        return count