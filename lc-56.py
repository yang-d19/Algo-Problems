"""
Merge Intervals
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.
"""

class Solution(object):

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(intervals)

        intervals = sorted(intervals)

        print("sorted intervals: ", intervals)

        merged_intervals = []

        idx = 0

        while idx < n:
            interval = intervals[idx]
            left = interval[0]
            right = interval[1]
            overlap_idx = idx
            init_idx = idx

            right_max = right

            while True:
                while overlap_idx < n and right >= intervals[overlap_idx][0]:
                    right_max = max(right_max, intervals[overlap_idx][1])
                    overlap_idx += 1
                overlap_idx -= 1
                if overlap_idx > init_idx:
                    right = right_max
                    init_idx = overlap_idx
                    # print("right = ", right)
                else:
                    merged_intervals.append([left, right_max])
                    # print("overlap_id = ", overlap_idx)
                    # print(merged_intervals)
                    break
                    # merged_intervals.append([left, max(right, intervals[overlap_idx][1])])
                
            
            idx = overlap_idx + 1
        
        return merged_intervals
    
sol = Solution()

intervals = [[1,3],[0,2],[2,3],[4,6],[4,5],[5,5],[0,2],[3,3]]

result = sol.merge(intervals)

print(result)