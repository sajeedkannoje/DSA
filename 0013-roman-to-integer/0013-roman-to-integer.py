class Solution:
    def romanToInt(self, s: str) -> int:
            romanMap = {
                "I" : 1,
                "V" : 5,
                "X" : 10,
                "L" : 50,
                "C" : 100,
                "D" : 500,
                "M" : 1000
            }
            n = len(s)
            total = 0

            for i in range(n):
                if(i+1 < n and romanMap[s[i]] < romanMap[s[i+1]]  ):
                    total = total - romanMap[s[i]]
                else:
                    total = total + romanMap[s[i]]
            return total