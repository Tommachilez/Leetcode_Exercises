"""Two-sum Solution"""

class TwoSum(object):
    def __init__(self, nums: list, target: int) -> None:
        self.nums = nums
        self.target = target

    def solution_1(self) -> list:
        """Use Brute Force"""

        for index, item in enumerate(self.nums):
            for next_index in range(index, len(self.nums)):
                if (index!=next_index) & (item + self.nums[next_index] == self.target):
                    result = [index, next_index]

        return result

arr = [3, 2, 4]
TARGET = 6

test = TwoSum(nums=arr, target=TARGET)
print(test.solution_1())
