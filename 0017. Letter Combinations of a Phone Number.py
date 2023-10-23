class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        trans = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }        

        ans = deque([''])

        for num in digits:
            for _ in range(len(ans)):
                base = ans.popleft()
                for letter in trans[num]:
                    ans.append(base + letter)

        return ans
