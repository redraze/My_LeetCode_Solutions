class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        copy = nums1[0:m]
        i, j = 0, 0
        L1, L2 = len(copy), len(nums2)
        for idx in range(0, len(nums1)):
            if i == L1:
                for idy in range(idx, len(nums1)):
                    nums1[idy] = nums2[j]
                    j += 1
                return
                    
            if j == L2:
                for idy in range(idx, len(nums1)):
                    nums1[idy] = copy[i]
                    i += 1
                return

            if copy[i] < nums2[j]:
                nums1[idx] = copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
        return
