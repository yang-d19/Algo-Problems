# import copy

def get_opt(sub_nums, player):
    if len(sub_nums) == 1:
        return {
            player: sub_nums[0], 
            1 - player: 0
        }

    if len(sub_nums) == 2:
        return {
            player: max(sub_nums[0], sub_nums[1]),
            1 - player: min(sub_nums[0], sub_nums[1])
        }

    sums_case1 = get_opt(sub_nums[1:], 1 - player)
    sums_case2 = get_opt(sub_nums[:-1], 1 - player)

    if sub_nums[0] + sums_case1[player] > sub_nums[-1] + sums_case2[player]:
        sums_case1[player] += sub_nums[0]
        return sums_case1
    else:
        sums_case2[player] += sub_nums[-1]
        return sums_case2


class Solution(object):
    
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        player_sums = get_opt(nums, 0)
        if player_sums[0] >= player_sums[1]:
            return True
        else:
            return False

sol = Solution()

ret = sol.predictTheWinner([1,5,2])

print(ret)