class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i, val in enumerate(nums):
            comlement = target - val 
            
            if comlement in m and m[comlement] != i:
                return [i , m[comlement]] 
            m[val] = i