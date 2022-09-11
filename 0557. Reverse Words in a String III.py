class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        for i, word in enumerate(s):
            s[i] = s[i][::-1]
        return ' '.join(s)
