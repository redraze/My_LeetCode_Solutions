class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # attempt #2
        # optimize for time complexity by removing lookups
        # optimize for space complexity by removing arrays
        sMap, tMap = {}, {}
        for sChar, tChar in zip(s, t):
            if(
                sChar in sMap and sMap[sChar] != tChar
                or tChar in tMap and tMap[tChar] != sChar
            ):
                return False
            sMap[sChar] = tChar
            tMap[tChar] = sChar
        return True

        # # attempt #1
        # # O(n) time and O(m + n) space complexity
        # sMap, tMap = {}, {}
        # for i in range(len(s)):
        #     sMap[s[i]] = sMap.get(s[i], [])
        #     sMap[s[i]].append(i)
        #     tMap[t[i]] = tMap.get(t[i], [])
        #     tMap[t[i]].append(i)
        #     if sMap[s[i]] != tMap[t[i]]:
        #         return False
        # return True
