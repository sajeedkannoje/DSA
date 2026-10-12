import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left ) // 2  
            if self.canEat(piles, h, mid):
               right = mid 
            else:
               left = mid + 1  
        return left

    def canEat(self, piles: list[int], h: int, numberOfBanana: int) -> bool:

        totalHours = 0
        for pile in piles:
            if pile > numberOfBanana:
                totalHours += math.ceil(pile / numberOfBanana)
            else:
                totalHours += 1
        return  h >= totalHours 
