class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashMap = {}
        res = []
        for i in range(len(s)):
                hashMap[s[i]] = i
            
        furthest = 0
        start = 0
        for i in range(len(s)):  
            furthest = max(furthest, hashMap[s[i]])
            if furthest == i:
                res.append(furthest - start + 1)
                start = i + 1
        return res


        