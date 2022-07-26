class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ''
        
        # thousands place
        x = num // 1000
        num = num % 1000
        if x != 0:
            ans = ans + self.func(x, 'M', '_V_', '_X_')
        
        # hundreds place
        x = num // 100
        num = num % 100
        if x != 0:
            ans = ans + self.func(x, 'C', 'D', 'M')
        
        # tens place
        x = num // 10
        num = num % 10
        if x != 0:
            ans = ans + self.func(x, 'X', 'L', 'C')
        
        # ones place = num
        if num != 0:
            ans = ans + self.func(num, 'I', 'V', 'X')        

        return ans
        
    def func(self, x: int, one: str, five: str, ten: str) -> str:
        string = ''
        if x == 9:
            string += one + ten
        elif x > 5:
            string += five + one * (x - 5)
        elif x == 5:
            string += five
        elif x == 4:
            string += one + five
        else:   # if x < 4
            string += one * x
        return string    
