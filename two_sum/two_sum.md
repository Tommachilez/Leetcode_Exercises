### Input
- An array of integers: nums
- An integer: target
### Output
- Indices of the two numbers such that they add up to target
- Each input would have exactly one solution, and may not use the same element twice
- Return the answer in any order
# **Approach 1**
## Pseudo code
```
i <- 0
while lenght of nums > 0:
    result <- empty list
    add i to result
    for j from 1 -> lenght of nums - 1:
        if nums[j] is equal to (target - nums[0]):
            add (j+i) to result
            return result
    delete the first element of nums
    increase i by 1
```
## Source code
```
i = 0
while len(nums) > 0:
    result = []
    result.append(i)
    for j in range(1, len(nums)):
        if nums[j] == target - nums[0]:
            result.append(j + i)
            return result
    del nums[0]
    i += 1
```
# **Approach 2**
## Pseudo code
```
for i from 1 to length of nums - 1:
    part <- empty list
    for j from 0 to i:
        if nums[j] is equal to target - nums[i]:
            add j to part
    if length of part is greater than 0:
        result <- list of part[0] and i
        return result
```
## Source code
```
for i in range(1, len(nums)):
    part = [j for j in range(0, i) if nums[j] == target - nums[i]]
    if len(part) > 0:
        result = [part[0], i]
        return result
```
# **Approach 3**
## Pseudo code 
```
dic <- empty dictionary
for i from 0 to length of nums - 1:
    if target - nums[i] is in dic:
        result <- list of dic[target - nums[i]] and i
        return result
    save index of nums[i] to dic
```
## Source code
```
dic = {}
for i in range(len(nums)):
    if target - nums[i] in dic:
        result = [dic[target - nums[i]], i]
        return result
    dic[nums[i]] = i
```