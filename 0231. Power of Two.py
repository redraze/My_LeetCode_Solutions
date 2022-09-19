class Solution:
    # Solution 2:
    # bit magic
    # O(n) runtime and space complexity
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        # using the bitwise 'and' operator (denoted as '&' in python)
        # on any power of two and its immediatelly smaller integer,
        # ie: 8 & 7,
        # will result in a zero. any non-power of two integer will not 
        # result in a zero.
        # for example:
        # bin(8) = '0b1000' --> 1000
        # bin(7) = '0b111'  --> 0100
        # 8 & 7 = 0
        # the and operator will return a one in each digit's place only if both 
        # places from bin(7) and bin(8) are one's, otherwise that digit's place
        # will be zero
        return not bool(n&n-1)
    
    
    # Solution 1:
    # examining binary equivalents
    # O(n) runtime and space complexity
    def isPowerOfTwo(self, n: int) -> bool:
        # check for zero and negative numbers
        if n < 1:
            return False
        # first, I convert 'n' to a string containing its binary equivalent
        b = bin(n)[2::]
        # next, I check to see if its equivalent is a power of two by examining its bits.
        # All powers of two in binary form are 1's followed by any number of zeros.
        # ie:
        # bin(2**0) = 0b1
        # bin(2**1) = 0b10
        # bin(2**2) = 0b100
        # bin(2**3) = 0b1000
        # bin(2**4) = 0b10000
        # bin(2**5) = 0b100000
        if (
            b[0] == '1'
            and '1' not in b[1::]
        ):
            return True
        return False
