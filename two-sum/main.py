"""Two-sum Solution"""

import time

class TwoSum(object):
    """
    Two-sum class containing the problem details and solutions.
    """
    def __init__(self, nums: list, target: int) -> None:
        self.nums = nums
        self.target = target

    def solution_1(self) -> list:
        """
        Use Brute Force
        """

        for index, item in enumerate(self.nums):
            for next_index in range(index, len(self.nums)):
                if (index!=next_index) & (item + self.nums[next_index] == self.target):
                    return [index, next_index]

        return []

    def solution_2(self) -> list:
        """
        Use Hash Map(Dictionary). 
        """

        num_to_index = {}
        for index, item in enumerate(self.nums):
            if self.target - item in num_to_index:  # Check the keys of num_to_index dictionary
                return [num_to_index[self.target - item], index]
            num_to_index[item] = index
        return []

arr = [2, 11, 15, 7]
TARGET = 9

test = TwoSum(nums=arr, target=TARGET)

start_time_1 = time.time()
print(test.solution_1())
end_time_1 = time.time()

start_time_2 = time.time()
print(test.solution_2())
end_time_2 = time.time()

elapsed_time_1 = round(end_time_1 - start_time_1, 4)
elapsed_time_2 = round(end_time_2 - start_time_2, 4)

print(f"Time execution for 1st solution: {elapsed_time_1}")
print(f"Time execution for 2nd solution: {elapsed_time_2}")
