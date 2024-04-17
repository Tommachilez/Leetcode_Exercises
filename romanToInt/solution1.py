class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {}
        roman_dict['I'] = 1
        roman_dict['V'] = 5
        roman_dict['X'] = 10
        roman_dict['L'] = 50
        roman_dict['C'] = 100
        roman_dict['D'] = 500
        roman_dict['M'] = 1000
        value = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                value += roman_dict[s[i]]
            elif roman_dict[s[i]] < roman_dict[s[i+1]]:
                value -= roman_dict[s[i]]
            else:
                value += roman_dict[s[i]]
        return value