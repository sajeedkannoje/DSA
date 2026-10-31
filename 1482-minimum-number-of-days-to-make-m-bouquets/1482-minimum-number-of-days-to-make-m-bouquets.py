class Solution:
    def possible(self,bloomDay: list[int], m: int, k: int, day:int) -> bool:

        count = 0
        numberOFBouquets = 0
        for bloom in bloomDay:
            if bloom <= day :
                # floower is bloomed
                count += 1
            else:
                numberOFBouquets += (count//k)
                count = 0
        numberOFBouquets += (count//k)
        if numberOFBouquets >= m :
            return True
        else:
            return False

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        
        if m*k >len(bloomDay):
            return -1
        low = min(bloomDay)
        high = max(bloomDay)

        while low < high:
            mid = low + (high  - low ) // 2
            if self.possible(bloomDay, m,k,mid):
                #means possible
                high = mid
            else :
                low= mid + 1
        return low 