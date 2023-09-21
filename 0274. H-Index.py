class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h, L = 0, len(citations)
        for i, val in enumerate(sorted(citations)):
            remainingPapers = len(citations) - i
            if remainingPapers >= val:
                h = val
            else:
                h = max(h, remainingPapers)
        return h
