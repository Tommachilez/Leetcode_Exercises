class Solution:
    def findMedianSortedArrays_approach1(self, nums1: List[int], nums2: List[int]) -> float:
        result = 0
        total = nums1 + nums2
        total.sort()
        n = len(total)
        if (n % 2 == 1):
            result = total[int(n / 2)]
        else:
            result = (total[int(n / 2)] + total[int(n / 2) - 1]) / 2

        return result

    def findMedianSortedArrays_approach2(self, nums1: List[int], nums2: List[int]) -> float:
        n_1 = len(nums1)
        n_2 = len(nums2)
        idx_1, idx_2 = 0, 0
        total = []

        while (idx_1 < n_1 and idx_2 < n_2):
            if nums1[idx_1] <= nums2[idx_2]:
                total.append(nums1[idx_1])
                idx_1 += 1
            else:
                total.append(nums2[idx_2])
                idx_2 += 1

        total.extend(nums1[idx_1:])
        total.extend(nums2[idx_2:])

        n = len(total)
        if (n % 2 == 1):
            result = total[int(n / 2)]
        else:
            result = (total[int(n / 2)] + total[int(n / 2) - 1]) / 2

        return result