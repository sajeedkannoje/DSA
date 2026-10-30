class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        left = 0
        freq = {'a': 0, 'b': 0, 'c': 0}

        for right in range(n):
            freq[s[right]] += 1
            #valid windows
            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                count += n - right
                freq[s[left]] -= 1
                left +=1
        
        return count 
        