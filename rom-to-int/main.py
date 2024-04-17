"""Roman to Integer Problem"""

class RomanToInt:
    """Convert a roman numeral to an integer."""
    def __init__(self, string):
        self.string = string

    def solution_1(self):
        """Use string properties and conditions"""
        result = 0
        for index, char in enumerate(self.string):
            if (index < len(self.string) - 1) and (roman_dict[char] < roman_dict[self.string[index+1]]):
                result -= roman_dict[char]
            else:
                result += roman_dict[char]

        return result

    def solution_2(self):
        """Change the roman numeral"""
        result = 0
        self.string = self.string.replace("IV", "IIII").replace("IX", "VIIII")
        self.string = self.string.replace("XL", "XXXX").replace("XC", "LXXXX")
        self.string = self.string.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in self.string:
            result += roman_dict[char]
        return result

roman_dict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

STRING = "MCMXCIV"
RESULT = 0

test = RomanToInt(STRING)
result1 = test.solution_1()
result2 = test.solution_2()

print(result1)
print(result2)
