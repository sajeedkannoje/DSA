class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first_lower_bound = self.find_lower_bound(nums, target)
        first_upper_bound = self.find_upper_bound(nums, target)
        return [ first_lower_bound,first_upper_bound]
    def find_lower_bound(self, nums: list[int], target: int) -> list[int]:
        left = 0
        right = len(nums) -1
        while left < right:
            mid  =  left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid 
        return left if nums and  nums[left] == target else -1


    def find_upper_bound(self, nums: list[int], target: int) -> list[int]:

        left = 0
        right = len(nums) -1
        while left < right:
            mid  = ( left + (right - left) // 2) + 1
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid+ 1
            else:
                left = mid 
        return right if nums and nums[right] == target else -1