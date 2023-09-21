# most recent attempt: sliding window -- O(n) time and O(1) space complexity
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letterSet, j, ans = set(), 0, 0
        for i, val in enumerate(s):
            while val in letterSet:
                letterSet.remove(s[j])
                j += 1
            letterSet.add(val)
            ans = max(ans, i - j + 1)
        return ans

# # attempt #1
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         hashTable = {}
#         anchor = 0
#         index = 0
#         max = 0
#         while index < len(s):
#             if len(s[anchor:index]) > max:
#                 max = len(s[anchor:index])
#             while s[index] in hashTable:
#                 hashTable.pop(s[anchor])
#                 anchor += 1
#             hashTable[s[index]] = index
#             index += 1

#         if len(s[anchor:index]) > max:
#             max = len(s[anchor:index])

#         return max
