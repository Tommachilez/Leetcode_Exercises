### Input
- Given two non-empty linked lists representing two non-negative integers
- The digits are stored in reverse order, and each of their nodes contains a single digit
### Output
- Add the two numbers and return the sum as a linked list
- Assume the two numbers do not contain any leading zero, except the number 0 itself
# Approach 1
## Pseudo code
```
FUNCTION addtwonumbers_approach_1(l1: ListNode, l2: ListNode) -> ListNode:
    DECLARE num1 = 0
    DECLARE num2 = 0
    DECLARE i1 = 0
    DECLARE i2 = 0

    WHILE l1 is not None:
        num1 += 10^i1 * l1.val
        l1 = l1.next
        i1 += 1

    WHILE l2 is not None:
        num2 += 10^i2 * l2.val
        l2 = l2.next
        i2 += 1

    DECLARE total = num1 + num2
    DECLARE s = CONVERT total TO STRING
    DECLARE n = LENGTH OF s
    DECLARE result = NEW ListNode()
    DECLARE current_node = result

    FOR i FROM 0 TO n-1:
        SET current_node.val = CONVERT s[n - 1 - i] TO INTEGER

        IF i EQUALS n - 1:
            SET current_node.next = None
            BREAK

        DECLARE node = NEW ListNode()
        SET current_node.next = node
        SET current_node = current_node.next

    RETURN result
```
## Source code
```
def addtwonumbers_approach_1(self, l1: ListNode, l2: ListNode) -> ListNode:
    num1 = 0
    num2 = 0
    i1 = 0
    i2 = 0

    while l1 is not None:
        num1 += 10 ** i1 * l1.val
        l1 = l1.next
        i1 += 1

    while l2 is not None:
        num2 += 10 ** i2 * l2.val
        l2 = l2.next
        i2 += 1

    total = num1 + num2
    s = str(total)
    n = len(s)
    result = ListNode()
    current_node = result

    for i in range(n):
        current_node.val = int(s[n - 1 - i])

        if i == n - 1:
            current_node.next = None
            break

        node = ListNode()
        current_node.next = node
        current_node = current_node.next

    return result
```
# Approach 2
## Pseudo code
```
FUNCTION addtwonumbers_approach_2(l1: ListNode, l2: ListNode) -> ListNode:
    DECLARE result = NEW ListNode()
    DECLARE current_node = result
    DECLARE carry = 0

    WHILE l1 is not None OR l2 is not None:
        IF l1:
            SET num1 = l1.val
        ELSE:
            SET num1 = 0

        IF l2:
            SET num2 = l2.val
        ELSE:
            SET num2 = 0

        SET current_total = num1 + num2 + carry
        SET current_node.val = current_total MOD 10
        SET carry = current_total DIV 10

        DECLARE node = NEW ListNode()
        SET current_node.next = node

        IF l1:
            SET l1 = l1.next
        IF l2:
            SET l2 = l2.next
        IF l1 is None AND l2 is None:
            SET current_node.next = None
            BREAK

        SET current_node = current_node.next

    IF carry != 0:
        DECLARE node = NEW ListNode()
        SET current_node.next = node
        SET current_node = current_node.next
        SET current_node.val = carry
        SET current_node.next = None

    RETURN result
```
## Source code
```
def addtwonumbers_approach_2(self, l1: ListNode, l2: ListNode) -> ListNode:
    result = ListNode()
    current_node = result
    carry = 0

    while l1 is not None or l2 is not None:
        if l1:
            num1 = l1.val
        else:
            num1 = 0

        if l2:
            num2 = l2.val
        else:
            num2 = 0

        current_total = num1 + num2 + carry
        current_node.val = current_total % 10
        carry = current_total // 10

        node = ListNode()
        current_node.next = node

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
        if l1 is None and l2 is None:
            current_node.next = None
            break
        current_node = current_node.next

    if carry != 0:
        node = ListNode()
        current_node.next = node
        current_node = current_node.next
        current_node.val = carry
        current_node.next = None

    return result
```