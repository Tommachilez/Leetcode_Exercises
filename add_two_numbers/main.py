# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nextnode=None):
        self.val = val
        self.next = nextnode


class Solution:
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