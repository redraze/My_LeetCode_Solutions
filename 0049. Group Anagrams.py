class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # attempt #2
        dict = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            if sortedWord not in dict:
                dict[sortedWord] = dict.get(sortedWord, [])
            dict[sortedWord].append(word)
        return [arr for arr in dict.values()]

        # # attempt #1
        # # O(n^2) time complexity and O(mn) space compelxity,
        # # where m is the average length of strs[i]
        # dicts = []
        # for s in strs:
        #     tempDict = {}
        #     for ch in s:
        #         tempDict[ch] = tempDict.get(ch, 0) + 1

        #     switch = False
        #     for i, (d, arr) in enumerate(dicts):
        #         if tempDict == d:
        #             dicts[i][1].append(s)
        #             switch = True
        #     if switch == False:
        #         dicts.append((tempDict, [s]))
                    
        # return [arr for (d, arr) in dicts]
