class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        # iterate thtough each bit of the 32-bit integer
        for i in range(32):
            # create space in 'ans' for another bit by bit-shifting left
            ans <<= 1
            # get the last bit in 'n' by using the bit operator 'and'
            temp = n & 1
            # append that bit to the end of ans
            ans += temp
            # remove the last bit from 'n' using the right bit-shift operator 
            n = n >> 1
        return ans
