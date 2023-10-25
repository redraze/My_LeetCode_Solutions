class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def dp(s: str, open: int, closed: int) -> None:
            if closed == n:
                ans.append(s)
                return
            if open < n:
                dp(s + '(', open + 1, closed)
            if closed < open:
                dp(s + ')', open, closed + 1)            
            return

        dp('', 0, 0)
        return ans
