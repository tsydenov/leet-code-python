class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # step from a merge sort
        i = 0
        j = 0
        c = []
        if len(nums1) == 0:
            c = nums2
        elif len(nums2) == 0:
            c = nums1
        else:
            while i < len(nums1) or j < len(nums2):
                if nums1[i] <= nums2[j]:
                    c.append(nums1[i])
                    i += 1
                else:
                    c.append(nums2[j])
                    j += 1
                if i == len(nums1):
                    c += nums2[j:]
                    break
                elif j == len(nums2):
                    c += nums1[i:]
                    break
        return (c[int(len(c) / 2)] + c[int(len(c) / 2) - 1]) / 2 if len(c) % 2 == 0 else c[len(c) // 2]
