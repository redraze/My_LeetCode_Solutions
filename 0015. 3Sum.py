# My most recent solution
# still O(n^2) time and O(n) space complexity
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()

        if (
            (nums[0] < 0 and nums[-1] < 0)
            or (nums[0] > 0 and nums[-1] > 0)
        ):
            return []

        for i, val in enumerate(nums):
            if val == nums[i - 1] and i > 0:
                continue

            L, R = i + 1, len(nums) - 1
            while L < R:
                sum = val + nums[L] + nums[R]
                if sum < 0:
                    L += 1
                    continue
                if sum > 0:
                    R -= 1
                    continue
                trip = tuple(sorted((val, nums[L], nums[R])))
                if trip not in ans:
                    ans.add(trip)
                L += 1

        return list(ans)


# Solution 3:
# two-pointer alogorithm with some checks for repeated numbers
# (the checks make the algorithm run much faster during the current tests)
# Runtime is still O(n^2), though
# Space complexity is O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        Set = set(nums)
        if (
            (nums[0] < 0 and nums[-1] < 0)
            or (nums[0] > 0 and nums[-1] > 0)
        ):
            return []
        for j,y in enumerate(nums[1:-1]):
            if nums[j] == y:
                if y != 0 and -2*y in Set:
                        ans.add((tuple(sorted([y,y,-2*y]))))
                if y == 0 and nums[j+2] == 0:
                    ans.add((0,0,0))
                continue
            i,k = 0,len(nums)-1
            while i < j+1 and k > j+1:
                x,z = nums[i],nums[k]
                Sum = x + y + z
                if Sum < 0:
                    i += 1
                    continue
                if Sum > 0:
                    k -= 1
                    continue
                ans.add((tuple(sorted([x,y,z]))))
                i += 1
        return list(ans)


'''
My first attempt.

Basically a brute force algorithm with a frequency dictionary and dictionary of already searched pairs.
The idea behind the dictionary of searched pairs was to be able to skip pairs that have already been searched,
and the idea behind the frequency dictionary was to be able to quickly find out if the complement to a pair existed in enough quantity to form a triplet.

frequency table time complexity:    O(len(array))
loop time complexity:               O(len(array)^3)      [worst case]
overall time complexity:            O(len(array) + len(array)^3) --> O(len(array)^3)

'''
# its runtime is over 9000!!!
# Memory Usage: a lot lol
# incredible work

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        searched_pairs = {}
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        for i in range(0,len(nums)):
            for j in range(i + 1,len(nums)):
                if (
                    (nums[i],nums[j]) not in searched_pairs 
                    and (nums[j],nums[i]) not in searched_pairs
                ):
                    searched_pairs[nums[i],nums[j]] = 0

                    # c for complement! ;D
                    c = -1 * (nums[i] + nums[j])
                    if (c in freq
                        and (
                            (c != nums[i] and c != nums[j] and nums[i]!= nums[j])
                            or ((nums[i] == c or nums[j] == c) and nums[i] != nums[j] and freq[c] > 1) 
                            or (c == nums[i] and c == nums[j] and nums[i] == nums[j] and freq[c] > 2)
                        )
                    ):
                        triplets.append([nums[i],nums[j],c])
                        searched_pairs[nums[i],c] = 0
                        searched_pairs[nums[j],c] = 0
        return triplets


'''

I did have another idea to use two moving markers on a sorted array 

Something like this:

sorted_array:        [    negative numbers        0        positive numbers     ]
markers:                              <- i        j        k ->

# imcomplete pseudo-code:
for j in range(0, len(sorted_array)):
    i = j - 1
    k = j + 1
    while True:
        if (i + j + k) == 0 and [i,j,k] not in triplets:
           triplets.append([i,j,k])
           i -= 1
        if (i + j + k) > 0:
           i -= 1
        if (i + j + k) < 0:
           k += 1

(after looking for solutions online, it seems like I was onto something!)

Once sorted, the array would need to be iterated over len(array) times, and for each of those iterations another len(array) iterations.
Making the time complexity O(sort time + len(array)^2)

'''

# my second attempt!
# chose a heapsort algorithm because it looked neat and I hadn't written one before
# my heapsort algo also utiliuzes Floyd's heap construction
# also, Fibonacci's heapsort looks awesome!

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = self.heapsort(nums)
        return self.find_triplets(nums)
    
    # heapsort algorithm (n*log(n) runtime)
    def heapsort(self, nums:List[int]) -> List[int]:
        def swap(x, y):
            nums[x] += nums[y]
            nums[y] = nums[x] - nums[y]
            nums[x] -= nums[y]
            return
        def downsift(li, i):
            # both children nodes exist
            try:
                if (
                    li[2*i + 1] > li[2*i + 2] 
                    and li[2*i + 1] > li[i]
                ):
                    swap(2*i + 1, i)
                    downsift(nums[0:len(li)], 2*i + 1)
                elif li[2*i + 2] > li[i]:
                    swap (2*i + 2, i)
                    downsift(nums[0:len(li)], 2*i + 2)
            except IndexError:
                # only one child node exists
                try:
                    if li[2*i + 1] > li[i]:
                        swap(2*i + 1, i)
                        downsift(nums[0:len(li)], 2*i + 1)
                # no children nodes exist
                except IndexError:
                    return
            return
        # build max heap (Floyd's heap construction)
        for i in range(int(len(nums)/2)-1, -1, -1):
            downsift(nums, i)
        # extract and downsift until array is sorted
        for i in range(len(nums) - 1, 0, -1):
            swap(0, i)
            downsift(nums[0:i], 0)
        return nums
    
    # two pointer algorithm (n^2 runtime)
    def find_triplets(self, nums:List[int]) -> List[int]:
        # so, sets are pretty useful lol
        triplets = set()        
        for j in range(1, len(nums) - 1):
            i = j - 1
            k = j + 1
            while i >= 0 and k < len(nums):
                if nums[i] + nums[j] + nums[k] == 0:
                    t = triplets.add((
                            tuple(sorted(
                                (nums[i], nums[j], nums[k])
                            ))
                        ))
                    i -= 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    i -= 1
                else:
                    k += 1
        return list(triplets)
