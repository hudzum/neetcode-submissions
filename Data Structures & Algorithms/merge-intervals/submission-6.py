class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda inter: inter[0])

        # #After Sorting cur.start <= end.start

        # res = [intervals[0]]

        # for start, end in intervals[1:]:
        #     last = res[-1]

        #     #basically after sort we dont need to check if start > last[0]
        #     if start <= last[1]: #does current overlap with prev
        #         last[1] = max(end, last[1])

        #     else:
        #         res.append([start,end])

        # return res
    

        res = [intervals[0]]

        for start, end in intervals[1:]:

            if start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])

            else:
                res.append([start,end])

        return res












