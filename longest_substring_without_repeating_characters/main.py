class Solution:
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
