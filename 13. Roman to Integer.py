# saw the dictionary in a few other solutions and thought it was a good idea

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = d[s[0]]
        ch = 1
        while ch < len(s):
            if d[s[ch - 1]] < d[s[ch]]:
                print(1)
                ans -= 2 * d[s[ch - 1]]
                ans += d[s[ch]]
                ch += 1
            else:
                print(2)
                ans += d[s[ch]]
                ch += 1
            
        return ans
