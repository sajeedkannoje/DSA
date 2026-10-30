class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:        
        n = len(s)
        left = 0
        counterMap = {}
        right = 10
        while right <= n:
            key = s[left:right]
            if key in counterMap:
                counterMap[key] += 1
            else :
                counterMap[key] = 1
            left +=1
            right +=1
        return [key for key, value in counterMap.items() if value >= 2]            