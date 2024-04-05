# first attempt (fails a few test cases)
# O(n log n) time and O(n) space complexity

import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.present = set()

    def popSmallest(self) -> int:
        if len(self.heap) == 0:
            self.heap = [1]
            self.present.add(1)
            return 1

        # find next smallest num in heap who's num - 1 isn't in heap
        maxNum = 0
        stack = [0]
        n = len(self.heap)
        while stack:
            idx = stack.pop()

            if idx >= n:
                continue

            num = self.heap[idx]
            if num > 1 and num - 1 not in self.present:
                heapq.heappush(self.heap, num - 1)
                self.present.add(num - 1)
                return num - 1
            
            maxNum = max(maxNum, num)
            stack.append(idx * 2 + 2)
            stack.append(idx * 2 + 1)

        heapq.heappush(self.heap, maxNum + 1)
        self.present.add(maxNum + 1)
        return maxNum + 1

    def addBack(self, num: int) -> None:
        if num in self.present:
            self.present.remove(num)
            
            stack = [0]
            n = len(self.heap)
            while stack:
                idx = stack.pop()

                if idx >= n:
                    continue

                if self.heap[idx] == num:
                    self.heap[idx] = 0
                    heapq.heapify(self.heap)
                    heapq.heappop(self.heap)
                    break

                stack.append(idx * 2 + 2)
                stack.append(idx * 2 + 1)

        return



# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
