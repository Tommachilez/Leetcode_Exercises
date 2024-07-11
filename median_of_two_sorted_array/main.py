class Solution:
    def find_median_sorted_arrays_approach_1(self, nums1, nums2) -> float:
        i = 0
        j = 0
        combined_list = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                combined_list.append(nums1[i])
                i += 1
            else:
                combined_list.append(nums2[j])
                j += 1

        if i < len(nums1):
            combined_list = combined_list + nums1[i:]
        elif j < len(nums2):
            combined_list = combined_list + nums2[j:]

        result = 0
        if len(combined_list) % 2 == 0:
            result = (combined_list[int(len(combined_list) / 2)]
                      + combined_list[int(len(combined_list) / 2) - 1]) / 2
        else:
            result = combined_list[len(combined_list) // 2]

        return result

    def find_median_sorted_arrays_approach_2(self, nums1, nums2) -> float:
        nums1 += nums2
        nums1.sort()

        result = 0
        if len(nums1) % 2 == 0:
            result = (nums1[int(len(nums1) / 2)]
                      + nums1[int(len(nums1) / 2) - 1]) / 2
        else:
            result = nums1[len(nums1) // 2]

        return result
