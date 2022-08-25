###
#
# Something I have been doing to help me with problems is sketch them out on a sheet of notebook paper and rip out little peices for variables. 
# This way I can follow the interpreter and catch any bugs/exceptions that may arise.
#
# Update! Started using pbd
#
###


class Solution:
    def trap(self, height: List[int]) -> int:
        
        # get index of largest value in height
        tallest = max([x for x in enumerate(height)], key=lambda x:x[1])[0]
        
        # runtime: O(n)
        def iterate(prev: int, tallest: int, step: int) -> int:
            volume = 0
            for i in range(prev, tallest, step):
                if height[i] > height[prev]:
                    prev = i
                else:
                    volume += height[prev] - height[i]
            return volume
                
        return (
            iterate(0, tallest, 1) 
            + iterate(len(height)-1, tallest, -1)
        )
