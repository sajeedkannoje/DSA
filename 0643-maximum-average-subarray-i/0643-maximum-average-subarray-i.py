class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        left = 0 
        right = 0
        total_of_window = 0
        max_avrg =  max_avrg = float("-inf")
        while right < len(nums):
            total_of_window += nums[right]

            if (right - left) == k-1 :
                max_avrg = max(max_avrg,(total_of_window/k)) 
                total_of_window-=nums[left]
                left += 1                
            right+=1
        return max_avrg