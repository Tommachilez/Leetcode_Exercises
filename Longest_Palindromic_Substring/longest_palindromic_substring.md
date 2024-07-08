### Input:
- A string ``s``
### Output:
  - The longest palindromic substring in ``s``
### Constraints:
- ``1 <= s.length <= 5 * 10^4``
- ``s`` consists of only English letters and digits.
# **Approach 1**
## Pseudo code
```
FUNCTION longest_palindrome_approach_1(s: STRING) -> STRING:
    IF LENGTH(s) <= 1:
        RETURN s
    
    SET result TO first character of s
    SET result_length TO 1
    
    FOR left FROM 0 TO LENGTH(s) - 2:
        FOR right FROM left + 1 TO LENGTH(s) - 1:
            IF (right - left + 1 > result_length) AND (SUBSTRING(s, left, right + 1) == REVERSE(SUBSTRING(s, left, right + 1))):
                SET result_length TO right - left + 1
                SET result TO SUBSTRING(s, left, right + 1)
    
    RETURN result

```
# **Approach 2**
## Pseudo code
```
FUNCTION longest_palindrome_approach_2(s: STRING) -> STRING:

    IF LENGTH(s) <= 1:
        RETURN s

    FUNCTION expand_string_center(left: INTEGER, right: INTEGER) -> STRING:
        WHILE left >= 0 AND right < LENGTH(s) AND s[left] == s[right]:
            left = left - 1
            right = right + 1
        RETURN SUBSTRING(s, left + 1, right)

    SET result TO first character of s

    FOR i FROM 0 TO LENGTH(s) - 2:
        SET odd TO expand_string_center(i, i)
        SET even TO expand_string_center(i, i + 1)

        IF LENGTH(odd) > LENGTH(result):
            SET result TO odd
        IF LENGTH(even) > LENGTH(result):
            SET result TO even

    RETURN result

```
# **Approach 3**
## Pseudo code
```
FUNCTION longest_palindrome_approach_3(s: STRING) -> STRING:

    IF LENGTH(s) <= 1:
        RETURN s

    SET result TO first character of s
    SET result_length TO 1

    INITIALIZE matrix AS a 2D LIST of size LENGTH(s) x LENGTH(s) FILLED WITH False

    FOR i FROM 0 TO LENGTH(s) - 1:
        SET matrix[i][i] TO True
        FOR j FROM 0 TO i - 1:
            IF s[j] == s[i] AND (i - j <= 2 OR matrix[j + 1][i - 1] == True):
                SET matrix[j][i] TO True
                IF i - j + 1 > result_length:
                    SET result_length TO i - j + 1
                    SET result TO SUBSTRING(s, j, i + 1)

    RETURN result

```