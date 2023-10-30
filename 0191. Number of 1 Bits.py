class Solution:
    # most recent solution
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for _ in range(32):
            # check to see if right-most digit is a 1 or 0
            if n & 1:
                ans += 1
            # bit-shift right
            n = n >> 1
        return ans
    
    # # log base 2 of n runtime and space complexity
    # def hammingWeight(self, n: int) -> int:
    #     # convert to binary string, 
    #     # slice away the '0b' at the beginning of the string,
    #     # remove all zeros from string,
    #     # find length of remaining string
    #     return len(bin(n)[2::].replace('0',''))
