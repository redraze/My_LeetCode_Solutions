class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        List = []
        if len(s) < 2:
            List.append(s.upper())
            if s[0].isalpha() == True:
                List.append(s.lower())
            return List
        perms = self.letterCasePermutation(s[1::])
        for perm in perms:
            List.append(s[0].upper() + perm)
            if s[0].isalpha() == True:
                List.append(s[0].lower() + perm)
        return List
