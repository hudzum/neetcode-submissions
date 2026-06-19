class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #is the left side acending
            #if so, is the target greater than mid or less than num l
            #Aka is it on the right side of the array
            #if full aray is acesnging target will be greater than mid l = mid
            # if right half is acesnding target will be 
        l = 0
        r = len(nums)-1
        while l <= r: 
            
            m = (l+r)//2
            print(l, m, r)
            if nums[m] == target:
                return m
            
            if nums[l] <= nums[m]: #is left side acesending
                if target > nums[m] or target < nums[l]: #target on right
                    l = m +1
                else:
                    r = m -1 # on left side
            else: #right side is acending
                if target < nums[m] or target > nums[r]:#is target on left
                    r = m -1
                else:
                    l = m +1
        
        return -1

