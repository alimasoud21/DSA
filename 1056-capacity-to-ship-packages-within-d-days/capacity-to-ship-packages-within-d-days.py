class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights) 
        res = r

        while l <= r:
            m = (l + r) // 2
            d = 1
            curr = 0
            for w in weights:
                curr += w
                if curr > m:
                    d += 1
                    curr = w   # start new day with this package

            if d <= days:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res