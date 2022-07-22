###
#
# This problem was absolutely brutal for me. Took a good stretch of time just figuring out how the * worked, and finding all the end cases.
# I also (mistakenly) refused to look at the solution until I solved it on my own. Should have looked at the solution after an hour or two.
# In the end though, I really enjoyed the elegance of the recursive solution.
#
###


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 and len(p) != 0:
            try:
                if p[1] == '*':
                    return self.isMatch(s, p[2::])
                else:
                    return False
            except IndexError:
                return False
        elif len(p) == 0 and len(s) != 0:
            return False
        elif len(s) == len(p) == 0:
            return True

        match = (p[0] in s[0]) or (p[0] == '.')
        try:
            if p[1] == '*':
                return (match and self.isMatch(s[1::], p)) or self.isMatch(s, p[2::])
            return match and self.isMatch(s[1::], p[1::])
        except IndexError:
            return match and self.isMatch(s[1::], p[1::])
            
            
            
            
'''
# my very gross first try

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # simplify pattern
        cp = 0
        while cp < len(p):
            try:
                while (p[cp] == p[cp + 2] == '*') and (p[cp - 1] == p[cp + 1]):
                    p = p[:cp - 1] + p[cp + 1::]
            except IndexError:
                pass
            cp += 1
        
        cs = 0
        cp = 0
        state = 's0'
        
        while cs < len(s):
            if cp == len(p):
                return False
            
            if state == 's0':
                if (p[cp] == '.') or (s[cs] == p[cp]):
                    try:
                        if p[cp + 1] == '*': 
                            if p[cp + 2:cp + 4] == p[cp:cp + 2]:
                                cp += 2
                            else:
                                cases = [
                                    (s[cs + 1::], p[cp +2::]),
                                    (s[cs + 1::], p[cp::]), 
                                    (s[cs::], p[cp + 2::])
                                ]
                                for (i, j) in cases:
                                    if self.isMatch(i, j) == True:
                                        return True
                    except IndexError:
                        cs += 1
                        cp += 2
                        break
                    cp += 1
                    cs += 1
                elif p[cp] == '*':
                    state = 's1'
                else:
                    try:
                        if p[cp + 1] == '*':
                            cp += 2
                            continue
                        return False 
                    except IndexError:
                        return False

            if state == 's1':
                if (p[cp - 1]) == '.' or (p[cp - 1] == s[cs]):
                    cases = [
                        (s[cs::], p[cp + 1::]),
                        (s[cs + 1::], p[cp + 1::])
                    ]
                    for (i, j) in cases:
                        if self.isMatch(i, j) == True:
                            return True
                    cs += 1
                else:
                    cp += 1
                    state = 's0'
        
        # eliminate remainder of pattern, if able
        while cp < len(p):
            try:
                if p[cp + 1] == '*':
                    cp += 2
                else:
                    return False
            except IndexError:
                return False
        
        if cs < len(s):
            return False
        return True
        
'''
