class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #First Search for Minimum aka pivot
        l = 0
        r = len(nums) -1
        while l < r: #because if l ==r ; rw will be constantly set to m and if l = m infinity
            m = (l+r)//2
            if nums[m] > nums[r]: #pivot is between m -r
                l = m+1
            else: #pivot is between l-m could be m
                r = m
        
        pivot = l
        print(pivot)
        def binary_search(l:int, r:int):

            while l <=r: #because search
                m = (l+r) //2
                if nums[m] == target:
                    return m
                if target > nums[m]:
                    l = m +1
                else:
                    r = m -1 #m == target been checked
            
            return -1

        res = binary_search(0, pivot)
        print(res)
        if res == -1:
            return binary_search(pivot, len(nums)-1)
        return res


