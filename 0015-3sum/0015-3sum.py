class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        i = 0
        while i < n - 2:
            if nums[i] > 0:
                break
                
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
                
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                # Skip all duplicates of nums[i]
                while i < n - 2 and nums[i] == nums[i + 1]:
                    i += 1
                i += 1
                continue
            
            target = -nums[i]
            left, right = i + 1, n - 1
            
            while left < right:
                sum_lr = nums[left] + nums[right]
                
                if sum_lr == target:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicates efficiently
                    left_val, right_val = nums[left], nums[right]
                    while left < right and nums[left] == left_val:
                        left += 1
                    while left < right and nums[right] == right_val:
                        right -= 1
                        
                elif sum_lr < target:
                    left += 1
                else:
                    right -= 1
            
            # Skip duplicates of nums[i]
            while i < n - 2 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        
        return result
