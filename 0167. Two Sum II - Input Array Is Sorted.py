class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 4
        # binary search algorithm
        # runtime O(n log n)
        # memory optimized
        for i, x in enumerate(numbers):
            L = i + 1
            R = len(numbers) - 1
            complement = target - x
            while L <= R:
                M = L + int((R - L)/2)
                if numbers[M] == complement:
                    return [i+1, M+1]
                if complement < numbers[M]:
                    R = M - 1
                else:
                    L = M + 1
        return []
        
        '''
        # Solution 3
        # memoization algorithm
        # runtime O(n)
        cache = {}
        for i,x in enumerate(numbers):
            complement = target - x
            if complement in cache:
                return[cache[complement]+1, i+1]
            cache[x] = i
        return []
        '''
        
        '''
        # Solution 2
        # two-pointer algorithm
        # runtime O(n), memory optimized
        i, j = (0, len(numbers)-1)
        while i <= j:
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return []
        '''
        
        '''
        # Solution 1
        # runtime O(n^2)
        for i, x in enumerate(numbers[0:-1]):
            for j, y in enumerate(numbers[i+1::]):
                if x + y == target:
                    return [i+1,j+i+2]
        return []
        '''
