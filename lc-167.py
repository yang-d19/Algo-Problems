class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                break
            elif curr_sum > target:
                right -= 1
            else:
                left += 1
        return [left + 1, right + 1]
