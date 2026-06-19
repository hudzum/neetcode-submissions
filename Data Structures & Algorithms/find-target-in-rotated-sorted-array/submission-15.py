class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:#whats happens when l == r: r is set to m -> infinite loop
            m = (l+r)//2

            if nums[m] > nums[r]: # Not Ascending pivot between m and r
                l = m + 1
            else:
                r = m #have not checked m 
            
        pivot = l 

        l = 0 
        r = len(nums)-1
        print(pivot)
        #Checked if target is between one first
        #is my target between pivot and r
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot -1

        print(l , r)
        while l <= r: #beause when l == r 
            m = (l+r) //2

            if nums[m] == target:
                return m
            if target < nums[m]:
                r = m -1 #because we alr checked m 
            else:
                l = m + 1

        return -1
            

