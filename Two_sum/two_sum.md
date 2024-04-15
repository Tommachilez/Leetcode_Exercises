### Input:
- An array of integers: nums
- An integer: target
### Output:
- Indices of the two numbers such that they add up to target
- Each input would have exactly one solution, and may not use the same element twice
- Return the answer in any order
### Constraints:
- `` 2 <= nums.length <= 10^4 ``

- `` -10^9 <= nums[i] <= 10^9 ``

- `` -10^9 <= nums[i] <= 10^9 ``
# **Approach 1**
## Pseudo code
```
twoSum_approach_1(nums, target):
    for first_num_idx in range(length(nums) - 1):
        for second_num_idx in range(first_num_idx + 1, length(nums)):
            if nums[first_num_idx] + nums[second_num_idx] == target:
                return [first_num_idx, second_num_idx]

```

# **Approach 2**
## Pseudo code
````
twoSum_approach_2(nums, target):
    pair_dict = {}
    for index, num in enumerate(nums):
        if (target - num) in pair_dict:
            return [index, pair_dict[target - num]]
        pair_dict[num] = index

````

# **Approach 3**
## Pseudo code
````
twoSum_approach_3(nums, target):
    for second_num_idx in range(1, length(nums)):
        first_num_list = []
        for first_num_idx in range(0, second_num_idx):
            if target - nums[first_num_idx] == nums[second_num_idx]:
                add first_num_idx to first_num_list
        if length(first_num_list) > 0:
            return [first_num_list[0], second_num_idx]

````