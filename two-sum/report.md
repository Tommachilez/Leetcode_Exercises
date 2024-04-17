# Two-Sum Problem

## Input
- An array of integers `nums`
- An integer `target`

## Output
- The indices of the two numbers such that they add up to `target`.

## Constraints
- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- <code>2 <= nums.length <= 10<sup>4</sup></code>
- <code>10<sup>-9</sup> <= nums[i] <= 10<sup>9</sup></code>
- <code>10<sup>-9</sup> <= target <= 10<sup>9</sup></code>
- Only one valid answer exists.

## Solution
### Brute-Force
    FOR index, item IN enumerate(nums):
        FOR next_index IN range(index, len(nums)):
            IF (index NOT EQUALS next_index) & (item + nums[next_index] EQUALS target):
                RETURN [index, next_index]

Pros:
- Easy to code and understand

Cons:
- Computationally expensive
- Time complexity is O(n^2)

### Hash Map
    SET num_to_index TO {}
        FOR index, item IN enumerate(nums):
            IF target - item IN num_to_index:
                RETURN [num_to_index[target - item], index]
            SET num_to_index[item] TO index

Pros:
- Reduces time complexity from O(n^2) to O(n)

Cons:
- Requires additional space for the hash map
- If there are multiple items with the same value in the array, 
only one will be stored in the hash map