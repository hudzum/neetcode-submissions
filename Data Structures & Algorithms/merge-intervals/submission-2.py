class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda inter: inter[0])

        #okay so we sort

        #compare current with next 
        #if current.start between next,start set 
            #new interval with min(next.start and end) & max(next.end and start)
        #else next end
        print(intervals)
        i = 0
        while i < len(intervals) -1:
            cur = intervals[i]
            nex = intervals[i+1]
         
            #if cur.end or start is between next
            if (cur[0] <= nex[1] and cur[0] >= nex[0]) or (cur[1] <=nex[1] and cur[1] >= nex[0]) or(nex[0] <= cur[1] and nex[0] >= cur[0]) or (nex[1] <=cur[1] and nex[1] >= cur[0]):
                newinterval = [min(cur[0], nex[0]), max(cur[1], nex[1])]       
                intervals.pop(i)
                intervals.pop(i)
                intervals.insert(i, newinterval)

            else:
                i+=1

        return intervals

