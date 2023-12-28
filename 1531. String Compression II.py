class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        # deconstruct string into letter-count combinations
        arr = []
        currentLetter = s[0]
        count = 1

        for ch in s[1:] + "_":
            if ch == currentLetter:
                count += 1
            else:
                if count:
                    arr.append(currentLetter + str(count))
                else:
                    arr.append(currentLetter)
                currentLetter = ch
                count = 1

        return min([
            self.deleteChars(arr, k, len(''.join(arr)), i)
            for i in range(len(s))
        ])

    # find optimal min length after deletion
    def deleteChars(self, s: List[str], k: int, L: int, idx: int) -> int:
        if k == 0 or idx >= len(s):
            return L

        curCount = int(s[idx][1:]) if len(s[idx]) > 1 else 1

        # deletion possible at current index
        if k >= curCount:
            k -= curCount
            s = s[0:idx] + s[idx + 2:]

            # try joining prev and next chars together
            try:
                nextCh = s[idx][0]
                nextCount = int(s[idx][1:]) if len(s[idx][1:]) > 1 else 1
                prevCh = s[idx - 1][0]
                prevCount = int(s[idx - 1][1:]) if len(s[idx - 1][1:]) > 1 else 1

                if prevCh == nextCh:
                    s[idx - 1] = prevCh + str(prevCount + nextCount)

            except IndexError:
                pass

            try:
                return min([
                    self.deleteChars(s, k, len(''.join(s)), i)
                    for i in range(idx, len(s))
                ])
            except ValueError:
                print(s, k, idx)
                return 0

        # deletion impossible at current index
        return L
