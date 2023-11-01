# my recent solution, with a custom build memory cache
class Solution:
    def __init__(self) -> None:
        self.cache = {0: 1}
        return
    def climbStairs(self, n: int) -> int:
        if n < 0:
            return 0
        if n not in self.cache:
            self.cache[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            print(n, self.hash[n])
        return self.hash[n]

# # my old suolution, using a cache function wrapper
# class Solution:
#     # store each answer to minimize the number of times
#     # 'climbStairs()' is called on the same 'n'
#     @cache
#     def climbStairs(self, n: int) -> int:
#         # when n == 1, there is one way to climb the staircase.
#         # when n == 2, there are two ways to climb the staircase,
#         # in two single steps or one double step.
#         if n < 3:
#             return n
#         # take one step, then calculate how many distinct 
#         # ways to climb the rest of the staircase. add that 
#         # number to the number of distinct ways to climb the 
#         # staircase after taking two steps
#         return self.climbStairs(n-1) + self.climbStairs(n-2)
