class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        L = len(nums1) + len(nums2)
        
        # empty array
        if not nums1 or not nums2:
            # even
            if L % 2 == 0:
                try:
                    return (nums1[int(L / 2 - 1)] + nums1[int(L / 2)])/2
                except IndexError:
                    return (nums2[int(L / 2 - 1)] + nums2[int(L / 2)])/2
            # odd
            try:
                return nums1[int(L / 2 - .5)]
            except IndexError:
                return nums2[int(L / 2 - .5)]

            
        a = []
        c1 = 0
        c2 = 0

        # even
        if L % 2 == 0:
            while (c1 + c2) < (L / 2 + 1):
                try:
                    if nums1[c1] < nums2[c2]:
                        a.append(nums1[c1])
                        c1 += 1
                    else:
                        a.append(nums2[c2])
                        c2 += 1
                except IndexError:
                    try:
                        a.append(nums1[c1])
                        c1 += 1
                    except IndexError:
                        a.append(nums2[c2])
                        c2 += 1
            return (a[-1] + a[-2]) / 2
        
        
        # odd
        while (c1 + c2) < (L / 2 + .5):
            try:
                if nums1[c1] < nums2[c2]:
                    a.append(nums1[c1])
                    c1 += 1
                else:
                    a.append(nums2[c2])
                    c2 += 1
            except IndexError:
                try:
                    a.append(nums1[c1])
                    c1 += 1
                except IndexError:
                    a.append(nums2[c2])
                    c2 += 1
        return a[-1]
