class Solution:
    # solution 1: using python types and string slicing
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
