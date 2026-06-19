class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        allnums = set(nums)
        onlyStart = set(nums)

        for n in allnums:
            if n - 1 in onlyStart:
                onlyStart.remove(n)


        longestConsect = 1
        for n in onlyStart:
            i = 0 
            while n + i in allnums:
                i+=1
            longestConsect = max(longestConsect, i)

        return longestConsect