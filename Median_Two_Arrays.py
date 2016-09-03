import math


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        nums3 = nums1 + nums2
        nums3.sort()
        length = len(nums3)

        if length % 2 == 0:
            y = length // 2
            z = float(nums3[y] + nums3[y - 1])
            x = z / 2
            return x

        else:
            y = (length // 2)
            z = nums3[y]
            return z