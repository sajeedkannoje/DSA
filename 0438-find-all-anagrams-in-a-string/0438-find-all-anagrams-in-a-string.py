class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_s , len_p = len(s) ,len(p)
        output = []
        if len_p > len_s:
            return output
        
        expexted_freq, window_freq = [0]* 26, [0]* 26
        for c in p:
            expexted_freq[ord(c) - ord('a') ] += 1

        left = 0 
        right = 0
        
        while right < len_s:
            window_freq[ord( s[right] ) - ord('a') ] += 1
            
            if  right - left +1 == len_p:
                if expexted_freq == window_freq:
                    output.append(left)
                window_freq[ord(s[left]) - ord('a')] -= 1
                left +=1
            right +=1
        return output   