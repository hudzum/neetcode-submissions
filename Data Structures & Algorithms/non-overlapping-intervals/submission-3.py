class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda inter: inter[0])

        res = [intervals[0]]
        fin = 0
        for start, end in intervals[1:]:
            last = res[-1]
            if start < last[1]:
                # print("Overlap", start, end, last )
                #we have overlap
                if  last[1] > end:
                    res[-1] = [start, end]
                fin +=1
            else:
                res.append([start,end])
            # print("Res", res)
        #considering comparing range larger range gets removed

        return fin