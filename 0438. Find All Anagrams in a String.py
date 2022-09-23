from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        ori,opp = Counter(p),Counter()
        index = 0
        for i,ch in enumerate(s):
            if ch not in p:
                # reset both the original and opposite Counters
                ori,opp = Counter(p),Counter()
                index = i + 1
                continue
            if ch in ori:
                # pass ch from original to opposite
                ori[ch] -= 1
                if ori[ch] == 0:
                    del ori[ch]
                opp[ch] += 1
            else:
                # increment index until similar ch is found
                while s[index] != ch:
                    opp[s[index]] -= 1
                    ori[s[index]] += 1
                    index += 1
                index += 1
            if ori == {}:
                ans.append(index)
        return ans
