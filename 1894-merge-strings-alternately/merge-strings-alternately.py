class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        P1, P2 = len(word1) , len(word2) 
        res = ""
        
        for i in range(len(word1 + word2)):
            if i < P1:
                res += word1[i]
            if i < P2:
                res += word2[i]
            #if i > P1 and i > P2:
             #   break
        return res
            
