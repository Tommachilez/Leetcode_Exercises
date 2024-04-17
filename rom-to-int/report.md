# Roman to Integer Problem

## Input
- A roman numeral `string`.

## Output
- The converted integer from the roman numeral.

## Constraints
>| Symbol   | Value   |
>| -------- | ------- |
>| I        | 1       |
>| V        | 5       |
>| X        | 10      |
>| L        | 50      |
>| C        | 100     |
>| D        | 500     |
>| M        | 1000    |

## Solution
Both solutions use the same roman dictionary as defined below

    SET roman_dict TO {

        "I": 1,

        "V": 5,

        "X": 10,

        "L": 50,

        "C": 100,

        "D": 500,

        "M": 1000

    }
### String properties and conditions
    SET result TO 0

    FOR index, char IN enumerate(string):

        IF (index < len(string) - 1) and (roman_dict[char] < roman_dict[string[index+1]]):

            result -= roman_dict[char]

        ELSE:

            result += roman_dict[char]

Pros:
- Easy to code and understand

### Roman numeral conversion
    SET result TO 0

    SET self.string TO self.string.replace("IV", "IIII").replace("IX", "VIIII")

    SET self.string TO self.string.replace("XL", "XXXX").replace("XC", "LXXXX")

    SET self.string TO self.string.replace("CD", "CCCC").replace("CM", "DCCCC")

    FOR char IN self.string:

        result += roman_dict[char]

Pros:
- Intuitively simple

Cons:
- Repeated code lines