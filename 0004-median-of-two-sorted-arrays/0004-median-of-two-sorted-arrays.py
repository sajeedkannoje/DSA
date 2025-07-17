class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is smaller
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) >> 1
        
        # Handle edge cases first
        if m == 0:
            return nums2[n // 2] if n & 1 else (nums2[n // 2 - 1] + nums2[n // 2]) * 0.5
        
        left, right = 0, m
        
        # Cache array access methods for speed
        nums1_get = nums1.__getitem__
        nums2_get = nums2.__getitem__
        
        while left <= right:
            i = (left + right) >> 1
            j = half - i
            
            # Optimized boundary checks
            maxLeft1 = nums1_get(i - 1) if i else float('-inf')
            minRight1 = nums1_get(i) if i < m else float('inf')
            
            maxLeft2 = nums2_get(j - 1) if j else float('-inf')
            minRight2 = nums2_get(j) if j < n else float('inf')
            
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if total & 1:
                    return float(max(maxLeft1, maxLeft2))
                else:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) * 0.5
            elif maxLeft1 > minRight2:
                right = i - 1
            else:
                left = i + 1
        
        return 0.0
