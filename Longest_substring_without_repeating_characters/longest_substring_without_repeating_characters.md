### Input:
- A string ``s``
### Output:
- The length of the longest substring without repeating characters.
### Constraints:
- ``0 <= s.length <= 5 * 10^4``
- ``s`` consists of English letters, digits, symbols and spaces.
# **Approach 1**
## Pseudo code
```
Algorithm lengthOfLongestSubstring_approach1(s):
  Initialize an empty set char_set
  Initialize variables left and max_length to 0
  For each index right from 0 to the length of s:
    While the character at index right is in char_set:
      Remove the character at index left from char_set
      Increment left by 1
    Add the character at index right to char_set
    Update max_length to be the maximum of max_length and (right - left + 1)
  Return max_length
```
# **Approach 2**
## Pseudo code
```
Algorithm lengthOfLongestSubstring_approach2(s):
  Initialize max_length to 0
  Initialize left to 0
  Initialize an empty dictionary last_seen
  For each index right and character char in s:
    If char is in last_seen and last_seen[char] is greater than or equal to left:
      Update left to be last_seen[char] + 1
    Update max_length to be the maximum of max_length and (right - left + 1)
    Update last_seen[char] to right
  Return max_length
```