### Input:
- Two sorted arrays ``nums1`` and ``nums2`` of size ``m`` and ``n`` respectively
### Output:
- The median of the two sorted arrays.
  - The overall run time complexity should be ``O(log (m+n))``.
### Constraints:
- ``nums1.length == m``
- ``nums2.length == n``
- ``0 <= m <= 1000``
- ``0 <= n <= 1000``
- ``1 <= m + n <= 2000``
- ``-10^6 <= nums1[i], nums2[i] <= 10^6``
# **Approach 1**
## Pseudo code
```
Algorithm findMedianSortedArrays_approach1
  Input: nums1, nums2 (both are lists of integers)
  Output: median (a float value representing the median)

  Begin
      Combine nums1 and nums2 into a single list total
      Sort the list total
      Calculate the length of total and store it in n

      If n is odd Then
          Set result to the middle element of total
      Else
          Set result to the average of the two middle elements of total
      End If

      Return result
  End

```
# **Approach 2**
## Pseudo code
```
Algorithm findMedianSortedArrays_approach2
  Input: nums1, nums2 (both are lists of integers)
  Output: median (a float value representing the median)

  Begin
      Initialize n_1 to the length of nums1
      Initialize n_2 to the length of nums2
      Initialize idx_1 and idx_2 to 0
      Initialize an empty list total

      While idx_1 is less than n_1 and idx_2 is less than n_2 Do
          If the element at idx_1 of nums1 is less than or equal to the element at idx_2 of nums2 Then
              Append the element at idx_1 of nums1 to total
              Increment idx_1 by 1
          Else
              Append the element at idx_2 of nums2 to total
              Increment idx_2 by 1
          End If
      End While

      Extend total with the remaining elements of nums1 starting from idx_1
      Extend total with the remaining elements of nums2 starting from idx_2

      Calculate the length of total and store it in n

      If n is odd Then
          Set result to the middle element of total
      Else
          Set result to the average of the two middle elements of total
      End If

      Return result
  End

```