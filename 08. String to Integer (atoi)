class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ''
        ch = 0
        
        try:
            # skip whitespace
            while s[ch] == ' ':
                ch += 1
        
            # save sign
            if (s[ch] == '-') or (s[ch] == '+'):
                if s[ch + 1].isnumeric() == False:
                    return 0
                ans += s[ch]
                ch += 1
        except IndexError:
            return 0
        
        while (ch < len(s)) and (s[ch].isnumeric() == True):
            ans += s[ch]
            ch += 1
        
        try:
            if int(ans) < -2**31:
                return -2**31
            elif int(ans) > 2**31 - 1:
                return 2**31 - 1
            else:
                return int(ans)
        except ValueError:
            return 0
