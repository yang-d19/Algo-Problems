class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_pos = 0
        check_pos = 0
        prev_val = nums[check_pos]
        same_cnt = 0
        n = len(nums)

        while check_pos < n:
            if nums[check_pos] == prev_val:
                same_cnt += 1
            else:
                prev_val = nums[check_pos]
                same_cnt = 1

            if same_cnt <= 2:
                nums[curr_pos] = nums[check_pos]
                curr_pos += 1

            check_pos += 1
        
        return curr_pos


sol = Solution()

nums = [0,0,1,1,1,1,2,3,3]

k = sol.removeDuplicates(nums)

print(k, nums)