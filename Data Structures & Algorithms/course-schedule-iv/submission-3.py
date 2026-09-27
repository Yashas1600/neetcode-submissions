class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        numCourses - 0 indexed
        [prereq][course]
        *indirect: self explanatory a -> b -> c
        bacially say if uj is a pre of vj [uj,vj]
        so basically need to maintain chained pre requisites 
        i think this can be solved in a hashMap
        () = indirect pre req

        [[1,0],[2,1],[3,2]],
        crs: pre
        0: 1 (2) (3)
        1: 2 (3)
        2: 3
        3: 
        """

        adj = defaultdict(list)
        for pre,crs in prerequisites:
            adj[crs].append(pre)


        def dfs(crs):
            if crs in preMap:
                return preMap[crs]
            else:
                preMap[crs] = set()
                for pre in adj[crs]:
                    preMap[crs].add(pre)
                    preMap[crs] |= dfs(pre)
                return preMap[crs]
            

        #map crs -> hashset of indirect pre reqs
        preMap = {}

        for crs in range(numCourses):
            dfs(crs)

        return [u in preMap[v] for u, v in queries]
        
            
            
        
