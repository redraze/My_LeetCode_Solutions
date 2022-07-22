###
#
# I know this solution is slow, but I just like using the math.log function to find the magnitude of the number
#
###

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if abs(x) != x:
            return False
        
        try:
            mag = int(math.log(x,10))
        except ValueError:
            return True
        
        while mag > 0:
            last = int(round(x/10 - (x/10)//1, 1) * 10)
            first = x//(10**mag)
            if first != last:
                return False
            x = x - first * (10**mag)
            x = int(x/10)
            mag -= 2
            
        return True
