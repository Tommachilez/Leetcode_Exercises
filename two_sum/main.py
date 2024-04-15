class Solution:
    def twosum_approach_1(self, nums: list[int], target: int) -> list[int]:
        i = 0
        result = []
        while len(nums) > 0:
            result.append(i)
            for j in range(1, len(nums)):
                if nums[j] == target - nums[0]:
                    result.append(j + i)
                    break
            del nums[0]
            result = []
            i += 1
        return result

    def twosum_approach_2(self, nums: list[int], target: int) -> list[int]:
        result = []
        for i in range(1, len(nums)):
            part = [j for j in range(0, i) if nums[j] == target - nums[i]]
            if len(part) > 0:
                result = [part[0], i]
                break
        return result

    def twosum_approach_3(self, nums: list[int], target: int) -> list[int]:
        result = []
        dic = {}
        for i in range(len(nums)):
            if target - nums[i] in dic:
                result = [dic[target - nums[i]], i]
                break
            dic[nums[i]] = i
        return result
