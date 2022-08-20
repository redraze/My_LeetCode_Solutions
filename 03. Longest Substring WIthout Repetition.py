###
#
# today I learned that hashtables have an average O(1) lookup time complexity, which is cool! 
#
###


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashTable = {}
        anchor = 0
        index = 0
        max = 0
        while index < len(s):
            if len(s[anchor:index]) > max:
                max = len(s[anchor:index])
            while s[index] in hashTable:
                hashTable.pop(s[anchor])
                anchor += 1
            hashTable[s[index]] = index
            index += 1

        if len(s[anchor:index]) > max:
            max = len(s[anchor:index])

        return max
