### Input
- Given two sorted arrays nums1 and nums2 of size m and n respectively.
### Output
- Return the median of the two sorted arrays.
- The overall run time complexity should be O(log (m+n)).
# Approach 1
## Pseudo code
```
FUNCTION find_median_sorted_arrays_approach_1(nums1: list, nums2: list) -> float:
    DECLARE i as 0
    DECLARE j as 0
    DECLARE combined_list as an empty list

    WHILE i is less than length of nums1 AND j is less than length of nums2:
        IF nums1[i] is less than nums2[j]:
            ADD nums1[i] to combined_list
            INCREMENT i by 1
        ELSE:
            ADD nums2[j] to combined_list
            INCREMENT j by 1

    IF i is less than length of nums1:
        ADD remaining elements of nums1 starting from index i to combined_list
    ELSE IF j is less than length of nums2:
        ADD remaining elements of nums2 starting from index j to combined_list

    DECLARE result as 0
    IF length of combined_list is even:
        SET result to (element at middle index of combined_list + element at index before middle) / 2
    ELSE:
        SET result to element at middle index of combined_list

    RETURN result
```
## Source code
```
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
```
# Approach 2
## Pseudo code
```
FUNCTION find_median_sorted_arrays_approach_2(nums1: list, nums2: list) -> float:
    ADD all elements of nums2 to nums1
    SORT nums1

    DECLARE result as 0
    IF length of nums1 is even:
        SET result to (element at middle index of nums1 + element at index before middle) / 2
    ELSE:
        SET result to element at middle index of nums1

    RETURN result
```
## Source code
```
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
```