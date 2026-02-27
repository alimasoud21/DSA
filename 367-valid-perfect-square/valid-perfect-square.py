class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while True:
            power = i * i
            if power == num:
                return True
            elif power > num:
                return False
            else:
                i += 1
