### Input:
- Two non-empty linked lists
- The digits are stored in reverse order, and each of their nodes contains a single digit.
### Output:
- Add the two numbers and return the sum as a linked list.
- The two numbers do not contain any leading zero, except the number 0 itself.
### Constraints:
- The number of nodes in each linked list is in the range [1, 100].
- ``0 <= Node.val <= 9``
- It is guaranteed that the list represents a number that does not have leading zeros.
# **Approach 1**
## Pseudo code
```
Function addTwoNumbers_approach1 takes l1, l2:
        Initialize num_1, num_2 to 0
        Initialize i1, i2 to 0
        While l1 is not None:
            Add (10 raised to i1) times l1.val to num_1
            Increment i1
            Move to the next node in l1

        While l2 is not None:
            Add (10 raised to i2) times l2.val to num_1
            Increment i2
            Move to the next node in l2

        Calculate int_result as the sum of num_1 and num_2
        Convert int_result to a string and reverse it

        Create a new ListNode as result
        Set current_node to result
        For each character in str_result:
            Set the value of current_node to the integer value of the character
            If at the last character:
                Move to the next node and break

            Create a new ListNode
            Set the next of current_node to the new node
            Move to the new node
        Return result
```
# **Approach 2**
## Pseudo code
```
Function addTwoNumbers_approach2 takes l1, l2:
        Create a new ListNode as head_node
        Set current_node to head_node
        Initialize carry to 0
        While l1, l2, or carry is not 0:
            Set l1_val to l1.val if l1 exists, else 0
            Set l2_val to l2.val if l2 exists, else 0

            Calculate result as l1_val plus l2_val plus carry
            Set the next of current_node to a new ListNode with value of result mod 10
            Calculate carry as result divided by 10

            If l1 exists, move to the next node in l1
            If l2 exists, move to the next node in l2
            Move to the next node in current_node
        Return the node next to head_node
```