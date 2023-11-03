class Solution:
    # my most recent solution
    # O(n^2) time and O(n) space complexity
    def longestPalindrome(self, s: str) -> str:
        ans = s[0]
        for i in range(len(s)):
            palindrome_1 = self.expandPalindrome(s, i, i)
            palindrome_2 = self.expandPalindrome(s, i, i + 1)
            ans = max(
                [ans, palindrome_1, palindrome_2],
                key=lambda x: len(x)
            )
        return ans

    def expandPalindrome(self, s: str, L: int, R: int) -> str:
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1
            R += 1
        return s[L + 1:R]

#     # my previous solutions
#     def longestPalindrome(self, s: str) -> str:
#         # insert '|' between every character in s, including at beginning and end
#         s1 = []
#         for i in range(len(s)):
#             s1.append('|')
#             s1.append(s[i])
#         s1.append('|')
        
#         palindrome_radii = {}
#         center = 0
#         radius = 0
#         while center < len(s1):
#             while (center - (radius + 1) >= 0) and (center + (radius + 1) < len(s1)) and (s1[center - (radius + 1)] == s1[center + (radius + 1)]):
#                 radius += 1
#             palindrome_radii[center] = radius
            
#             # set proceeding palindrome's radii withing curent palindrome equal to preceeding palindrome's radii if certain conditions are met
#             old_center = center
#             old_radius = radius
#             center += 1
#             radius = 0
#             while center <= old_center + old_radius:
#                 reflected_center = old_center - (center - old_center)
#                 # set radius of current center to radius of reflected center if 
#                 # radius of reflected center is within (and does not border) radius of old center
#                 if reflected_center - palindrome_radii[reflected_center] > old_center - palindrome_radii[old_center]:
#                     palindrome_radii[center] = palindrome_radii[reflected_center]
#                     center += 1
#                 # set radius variable to radius of reflected center if
#                 # radius of reflected center has same border as old center's radius, or
#                 # reflected center radius reaches beyond old radius from old center
#                 else:
#                     radius = old_center + old_radius - center
#                     break
        
#         s1_center = max(palindrome_radii, key=palindrome_radii.get)
#         s1_radius = palindrome_radii[s1_center]

#         s_center = (s1_center - 1) / 2
#         s_radius = int((s1_radius - 1) / 2)
        
#         return s[int(s_center - s_radius):int(ceil(s_center) + s_radius + 1)]
        
        
# '''
# # this is what I was going for on my first attempt (never got it to work properly) before looking at the solutions

# class Solution:
#     def check(self, s: str, p: str, start: int, end: int) -> str:
#         if end - start > len(p):
#             p = s[i:j]
#         return p
    
#     def longestPalindrome(self, s: str) -> str:
#         p = s[0]
#         for i in range(len(s)):
            
#             single_switch   = 1
#             multi_switch    = 1
#             for j in range(i+1, len(s)):
#                 if single_switch == 0 and multi_switch == 0:
#                     break

#                 # single char palindrome
#                 if single_switch == 1:
#                     if s[i] != s[j]:
#                         p = check(s, p, i, j)
#                         single_switch = 0
                
#                 # multi char palindrome
#                 if multi_switch == 1:
#                     # catch negative index
#                     if j - i > i:
#                         check(s, p, 2*i - j + 1, j)     #  j - 2(j-i) + 1    =    j -2j + 2i + 1     =    2i - j + 1
#                         multi_switch = 0
#                         continue
#                     if s[j] != s[2*i - j]:              #  j - 2(j-i)        =    j -2j -2i          =    2i - j
#                         p = check(s, p, 2*i - j + 1, j) #  same as check for negative index
#                         multi_switch = 0
                
#         return p
# '''
