class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 0 :
            return 0
        freq = {}
        left = right = max_len = highest_freq = 0
        
        while right < len(s):

            freq[s[right]] = freq.get(s[right],0) + 1
            highest_freq = max(highest_freq, freq[s[right]])
            number_of_char_to_replace = (right-left + 1)  - highest_freq
            
            if number_of_char_to_replace > k:
                freq[s[left]] -= 1
                left += 1
            
            max_len = right-left + 1
            right += 1

        return max_len