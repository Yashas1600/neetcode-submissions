class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #hashMap
        res = defaultdict(list)
        for str in strs:
            count = [0] * 26
            for letter in str:
                count[ord(letter) - ord('a')] += 1
            res[tuple(count)].append(str)
        return list(res.values())