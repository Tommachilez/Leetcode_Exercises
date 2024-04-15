class Solution:
    def twoSum_approach_1(self, nums: List[int], target: int) -> List[int]:
        for first_num_idx in range(len(nums) - 1):
            for second_num_idx in range(first_num_idx + 1, len(nums)):
                if nums[first_num_idx] + nums[second_num_idx] == target:
                    return [first_num_idx, second_num_idx]

    def twoSum_approach_2(self, nums: List[int], target: int) -> List[int]:
        pair_dict = {}

        for i, num in enumerate(nums):
            if target - num in pair_dict:
                return [i, pair_dict[target - num]]
            pair_dict.update({num: i})

    def twoSum_approach_3(self, nums: List[int], target: int) -> List[int]:

        for second_num_idx in range(1, len(nums)):
            first_num_list = [first_num_idx for first_num_idx in range(0, second_num_idx) if
                              target - nums[first_num_idx] == nums[second_num_idx]]
            if len(first_num_list) > 0:
                return [first_num_list[0], second_num_idx]
