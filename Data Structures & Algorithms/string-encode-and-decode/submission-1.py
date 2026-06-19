class Solution:

    def encode(self, strs: List[str]) -> str:
        #Without a special character store lengths first
        if not strs:
            return ""

        sizes = []
        for s in strs:
            sizes.append(len(s))
        result = []

        for sz in sizes:
            result.append(str(sz)+",")
        result.append("#")
        
        result.extend(strs)
        result = "".join(result)
        print(result)
        return result
        
    def decode(self, s: str) -> List[str]:
        #split by some delimiter
        if not s:
            return []
        sizes, result, i = [], [], 0

        while s[i] != '#':
            j=i
            #if , we append sizes
            while s[j] != ",":
                j+=1
            sizes.append(int(s[i:j]))
            i=j+1
        i+=1
        result = []

        for sz in sizes:
            result.append(s[i :i+sz])
            i+=sz



        return result
            