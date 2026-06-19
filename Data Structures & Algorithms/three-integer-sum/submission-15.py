class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Brute Force Triple four loop
        #Sorting [-1,0,1,2,-1,-4]
        #[-4, -1, -1, 0, 1, 2]
        #[-1,0,1] and [-1,-1,2].
        n = sorted(nums)
        res = []
        i=0
        while i < len(n) - 1:
            #-nums[i] = nums[j] + nums[k]
            #j& k should add up to be -num[1]
            j, k = i+1, len(n)-1
            #-num[i] is target 
            while j<k:
                if n[j] + n[k] > -n[i]:
                    k-=1
                elif n[j] + n[k] < -n[i]:
                    j+=1
                else:
                    if [n[i], n[j], n[k]] not in res:
                        res.append([n[i], n[j], n[k]])
                    j+=1
                    
            i+=1


        return res
                