class Solution:
    def maxArea(self, heights: List[int]) -> int:
        vol = 0
        l, r = 0, len(heights)-1
        #we take the smallest of two bars calculate the area r-l * small bar height - other bars
        while l < r:
            print((heights[r],heights[l]))
            print(r-l-1)
            vol = max(vol, min(heights[r],heights[l]) * (r-l))
            print(vol)
            if heights[r] > heights[l]:
                l+=1
            else:
                r-=1

        return vol