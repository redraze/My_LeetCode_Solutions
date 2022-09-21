class Solution:
    # Solution 1:
    # two pointers
    # Runtime O(n + m) where n = len(s) and m = len(t)
    # Space complexity O(1)
    def backspaceCompare(self, s: str, t: str) -> bool:
        # pointers
        ps,pt = len(s)-1,len(t)-1
        # count backspaces
        bs,bt = 0,0
        
        while ps >= 0 or pt >= 0:
            # save backspaces
            while s[ps] == '#' and ps >= 0:
                ps,bs = ps-1,bs+1
            while t[pt] == '#' and pt >= 0:
                pt,bt = pt-1,bt+1
            # use backspaces
            while bs > 0 and s[ps] != '#':
                ps,bs = ps-1,bs-1
            while bt > 0 and t[pt] != '#':
                pt,bt = pt-1,bt-1
            # iterate through character matches
            while (
                s[ps] == t[pt] 
                and s[ps] != '#'
                and ps >= 0 and pt >= 0
            ):
                ps,pt = ps-1,pt-1
            # check end conditions
            if ps < 0 and pt < 0:
                return True
            if (
                (s[ps] == '#' and ps >= 0)
                or (t[pt] == '#' and pt >= 0)
            ):
                continue
            return False
