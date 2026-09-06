class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            hayLen = len(haystack)
            needleLen = len(needle)

            if needleLen > hayLen:
                return -1

            for i in range ((hayLen - needleLen) + 1):
                if(haystack[i:i+needleLen] == needle):
                    return i
            return -1
