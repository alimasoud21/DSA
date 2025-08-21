class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        gues = 0
        while res <= x:
            res = gues * gues
            gues += 1

        if res == x:
            return gues-1
        else:
            return gues - 2