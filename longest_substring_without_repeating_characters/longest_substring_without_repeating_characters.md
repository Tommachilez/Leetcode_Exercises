### Input
- Given a string s
### Output
- Length of the longest 
substring
 without repeating characters
# Approach 1
## Pseudo code
```
FUNCTION lengthOfLongestSubstring_approach_1(s: str) -> int:
    DECLARE result as 0
    DECLARE start as 0
    DECLARE end as length of s - 1
    DECLARE i as 0
    DECLARE character_list as an empty list

    WHILE i is less than length of s:
        IF s[i] is not in character_list:
            ADD s[i] to character_list
            SET end to i
            INCREMENT i by 1
        ELSE:
            DECLARE temp_result as length of substring from s[start] to s[end]
            UPDATE result with the maximum of result and temp_result

            INCREMENT start by 1
            SET i to start
            CLEAR character_list

        IF end is equal to length of s - 1:
            DECLARE temp_result as length of substring from s[start] to s[end]
            UPDATE result with the maximum of result and temp_result

    RETURN result
```
## Source code
```
def lengthoflongestsubstring_approach_1(self, s: str) -> int:
    result = 0
    start = 0
    end = len(s) - 1
    i = 0
    character_list = []

    while i < len(s):
        if s[i] not in character_list:
            character_list.append(s[i])
            end = i
            i += 1
        else:
            temp_result = len(s[start:end + 1])
            result = max(result, temp_result)

            start += 1
            i = start
            character_list = []

        if end == len(s) - 1:
            temp_result = len(s[start:end + 1])
            result = max(result, temp_result)

    return result
```
# Approach 2
## Pseudo code
```
FUNCTION lengthOfLongestSubstring_approach_2(s: str) -> int:
    DECLARE left as 0
    DECLARE right as 0
    DECLARE result as 0
    DECLARE characters as an empty list

    WHILE right is less than length of s:
        IF s[right] is in characters:
            DECLARE i as index of s[right] in characters
            DECLARE steps as length of characters[:i + 1]
            SET characters to characters[i + 1:]
            INCREMENT left by steps

        ADD s[right] to characters
        UPDATE result with the maximum of result and (right - left + 1)
        INCREMENT right by 1

    RETURN result
```
## Source code
```
def lengthoflongestsubstring_appoach_2(self, s: str) -> int:
    left = 0
    right = 0
    result = 0
    characters = []

    while right < len(s):
        if s[right] in characters:
            i = characters.index(s[right])
            steps = len(characters[:i + 1])
            characters = characters[i + 1:]
            left += steps

        characters.append(s[right])
        result = max(result, right - left + 1)
        right += 1

    return result
```