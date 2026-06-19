class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Adding all to hashmap
        #with value as num - 1 itself

        #We only add a value if n -1 doesn't exist
        onlyStart = set()
        all = set()
        for n in nums:
            onlyStart.add(n)
            all.add(n)

        rmlist = []
        for n in onlyStart:
            if n-1 in onlyStart:
                rmlist.append(n)
        for rm in rmlist:
            onlyStart.remove(rm)
        longestconsect = 0 
        for n in onlyStart:
            
            i=0
            while n + i in all:
                i+=1
            if i > longestconsect:
                longestconsect = i
        return longestconsect
                
                

