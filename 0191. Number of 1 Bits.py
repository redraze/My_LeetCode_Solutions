class Solution:
    # log base 2 of n runtime and space complexity
    def hammingWeight(self, n: int) -> int:
        # convert to binary string, 
        # slice away the '0b' at the beginning of the string,
        # remove all zeros from string,
        # find length of remaining string
        return len(bin(n)[2::].replace('0',''))
