import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we need to define the number of bananas she can eat all of them in h hours
        # [3,6,7,11] 4 4 4
        # find totall number of piles 3 9 16 27
        #  min = 1
        # get max 30
        # 1 2 2 3
        # 1 1 2 2
        minspeed = 1
        maxspeed = max(piles)
        result = maxspeed        # worst case — eat fastest

        while minspeed <= maxspeed:
            mid = minspeed + (maxspeed - minspeed) // 2

            hours = 0
            for x in piles:
                hours += math.ceil(x / mid)  # total hours at speed mid

            if hours <= h:
                result = mid             # valid speed — record it, try slower
                maxspeed = mid - 1
            else:
                minspeed = mid + 1       # too slow — try faster

        return result

            

