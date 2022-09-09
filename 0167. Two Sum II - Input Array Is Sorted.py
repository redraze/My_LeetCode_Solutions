class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Solution 3
        # runtime O(n), uses same amount of memory as solution 2???
        Set = set(numbers)
        for i,x in enumerate(numbers):
            complement = target - x
            if complement in Set:
                for j,y in enumerate(numbers):
                    if (
                        y == complement 
                        and i != j
                    ):
                        return [i+1,j+1]
        return []
        
        '''
        # Solution 2
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
