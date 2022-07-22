class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = abs(x)
            neg = True
        
        x = str(x)
        ans = ''
        for i in range(len(x)):
            ans += (x[len(x) - i - 1])

        if neg == True:
            if -int(ans) < -2**31:
                return 0
            return -int(ans)
        
        if int(ans) > 2**31 - 1:
            return 0
        return int(ans)
