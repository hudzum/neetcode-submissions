class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)+1 != n:
            return False
        #We can create a adjancent map, run dfs and check for cycles using a set

        adjmap = {i:[] for i in range(n)}
        for edg, adj in edges:
            adjmap[edg].append(adj)
            adjmap[adj].append(edg) #Un ordered

        visiting = set() #purely for current dfs stack

        #beacause we are looping through adj and edj we need to have parents
        #other wise [[1,0]] would fail lol cauase after we check 0, 1 we need to go again cause we also added 1, 0 for unordered checking
        def dfs(node,par):
            print(visiting)
            if node in visiting:
                return False
            #if found on stack trace

            # if adjmap[node] == []: #means uhh leaf
            #     return True
            #we actually dont want this it prevents us from adding leaf nodes

            visiting.add(node)
            for adj in adjmap[node]:
                if adj == par:
                    continue
                if not dfs(adj, node): #As Soon as one turns false automatically end it
                    return False

            #now we head back up the recursive stack
            return True


        return dfs(0, -1) and len(visiting) == n