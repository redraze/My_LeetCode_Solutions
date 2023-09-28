# solution #2
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            n = sum([pow(int(val), 2) for val in str(n)])
            if n in seen:
                return False
            seen.add(n)
        return True

# # solution #1
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         seen = set()
#         num = n
#         while True:
#             sum = 0
#             for val in str(num):
#                 sum += pow(int(val), 2)
#             print(sum)
#             if sum == 1:
#                 return True
#             if sum in seen:
#                 return False
#             seen.add(sum)
#             num = sum
#         return
