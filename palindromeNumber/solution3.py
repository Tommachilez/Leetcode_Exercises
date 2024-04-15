class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0): return False
        len_x = 0
        temp = x
        while temp > 0:
            temp = int(temp / 10)
            len_x += 1
        temp = x
        while len_x > 1:
            left = int(temp / (10**(len_x-1)))
            right = temp % 10
            if right != left:
                return False
            temp = temp % (10**(len_x-1))
            temp = int(temp / 10)
            len_x -= 2
        return True