class Solution:
    def minWindow(self, s: str, t: str) -> str:

        mp = defaultdict(int)
        for char in t:
            mp[char] +=1 
        l = 0
        res = s[:]
        hasPassed = False
        for r in range (len(s)):

            if s[r] in mp :
                mp[s[r]] -=1

            #Hashmap all Zeroed / All values of T Found
            while all(v <= 0 for v in mp.values()):
                res = min(res, s[l:(r+1)], key = len)
                #print(s[r],"empty", mp, res, s[l:(r+1)])

                #Move Left and Readd Hashmap
                if s[l] in mp:
                    mp[s[l]] +=1   
                l+=1
                hasPassed = True
            
            #IF
            

            #remove duplicates from left
            #print(l)
            if l<len(s) and s[l] not in mp:
                #print("remove", s[l])
                l+=1

            #print(s[r], mp, res, s[l:(r+1)])

        if hasPassed:
            return res
        return ""
