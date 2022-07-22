class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        arr = [''] * numRows
        ch = 0
        rowCounter = 0
        while ch < len(s):
            try:
                while rowCounter < numRows:
                    arr[rowCounter] += s[ch]
                    ch += 1
                    rowCounter += 1
                rowCounter -= 2
                while rowCounter > 0:
                    arr[rowCounter] += s[ch]
                    ch += 1
                    rowCounter -= 1
            except IndexError:
                break
        
        s = ''
        for i in range(len(arr)):
            s += arr[i]
            
        return s
