class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]
        i = 0
        j = 0

        while i < m and j < n:
            if nums3[i] <= nums2[j]:
                nums1[i + j] = nums3[i]
                i += 1
            else:
                nums1[i + j] = nums2[j]
                j += 1
        
        while i < m:
            nums1[i + j] = nums3[i]
            i += 1
        
        while j < n:
            nums1[i + j] = nums2[j]
            j += 1


sol = Solution()

nums1 = [1, 2, 3, 0, 0, 0]

nums2 = [2, 5, 6]

sol.merge(nums1, 3, nums2, 3)

print(nums1)