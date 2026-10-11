class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        prev_indexes = {}
        left = 0 
        right = 0
        while (right < len(s)):

            if s[right] in prev_indexes  and prev_indexes[s[right]] >= left :
                left = prev_indexes[s[right]] + 1
            
            max_len = max(max_len , right - left + 1)
            prev_indexes[s[right]] = right
            right = right + 1

        return max_len