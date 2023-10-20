class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # flatten board into a straightforward path
        path = [None]
        for i, row in enumerate(board[::-1]):
            if i % 2:
                path += row[::-1]
            else:
                path += row
        
        seen = {1}
        q = deque([1])
        end = len(path)
        ans = 0

        while q:
            for _ in range(len(q)):
                pos = q.popleft()
                if pos == end - 1:
                    return ans

                for i in range(pos + 1, min(pos + 7, end)):
                    if path[i] + 1:
                        next = path[i]
                    else:
                        next = i
                    if next not in seen:
                        seen.add(next)
                        q.append(next)

            ans += 1

        return -1
