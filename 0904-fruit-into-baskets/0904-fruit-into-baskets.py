class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        bucket = {}
        maxLen = 0

        for right in range(len(fruits)):
            key = fruits[right]
            bucket[key] = bucket.get(key,0) + 1

            while len(bucket) > 2:
                leftKey = fruits[left]
                bucket[leftKey] -= 1
                if bucket[leftKey] == 0 :
                    del bucket[leftKey]
                left += 1
            maxLen = max(maxLen, right - left+1)
        return maxLen