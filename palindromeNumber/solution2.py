class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse = str_x[::-1]
        return reverse == str_x