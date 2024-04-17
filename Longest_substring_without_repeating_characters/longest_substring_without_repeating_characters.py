class Solution:
    def lengthOfLongestSubstring_approach1(self, s: str) -> int:
        char_set = set()
        left, max_length = 0, 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    def lengthOfLongestSubstring_approach2(self, s: str) -> int:
        max_length = 0
        left = 0
        last_seen = {}

        for right, char in enumerate(s):
            if char in last_seen and last_seen[char] >= left:
                left = last_seen[char] + 1

            max_length = max(max_length, right - left + 1)
            last_seen[char] = right

        return max_length

