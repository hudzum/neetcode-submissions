class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #HOW the fuck was i ssupose to kjow that the thye were in order bruch
        # Detecting Cycles
        preMap = {i:[] for i in range(numCourses)}

        for cor, pre in prerequisites:
            preMap[cor].append(pre)
            
        #store course purely for current DFS recursion stack 
        visitSet = set()

        def dfs(cor):
            if cor in visitSet:
                return False # nod is in current recursion path cycle
            if preMap[cor] == []:
                return True #alreadyed processed no cycle

            visitSet.add(cor)
            
            for pre in preMap[cor]:
                if not dfs(pre):
                    return False
            
            #Without this if a node is reachable by two others
            #if it has two parents the second pass will incorrectly return false
            visitSet.remove(cor)
            #By popping it off we removed it from current path
            preMap[cor] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        #This is incase we have something like
        #[2,1] and [3,4] completeling disconnected
        #
        return True