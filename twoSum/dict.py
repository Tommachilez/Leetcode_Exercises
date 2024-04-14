class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        output = []
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in num_dict:
                output.append(num_dict[temp])
                output.append(i)
            else:
                num_dict[nums[i]] = i
        return output