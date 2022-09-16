class Solution:
    # store each answer to minimize the number of times
    # 'climbStairs()' is called on the same 'n'
    @cache
    def climbStairs(self, n: int) -> int:
        # when n == 1, there is one way to climb the staircase.
        # when n == 2, there are two ways to climb the staircase,
        # in two single steps or one double step.
        if n < 3:
            return n
        # take one step, then calculate how many distinct 
        # ways to climb the rest of the staircase. add that 
        # number to the number of distinct ways to climb the 
        # staircase after taking two steps
        return self.climbStairs(n-1) + self.climbStairs(n-2)
