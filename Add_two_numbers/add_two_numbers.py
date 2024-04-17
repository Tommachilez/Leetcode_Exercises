# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers_approach1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = 0
        num_2 = 0
        i1 = 0
        i2 = 0
        while l1 is not None:
            num_1 += 10 ** i1 * l1.val
            i1 += 1
            l1 = l1.next

        while l2 is not None:
            num_1 += 10 ** i2 * l2.val
            i2 += 1
            l2 = l2.next

        int_result = num_1 + num_2
        str_result = str(int_result)
        str_result = str_result[::-1]

        result = ListNode()
        current_node = result
        for j in range(len(str_result)):
            current_node.val = int(str_result[j])

            if j == len(str_result) - 1:
                current_node = current_node.next
                break

            node = ListNode()
            current_node.next = node
            current_node = current_node.next
        return result

    def addTwoNumbers_approach2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode()
        current_node = head_node
        carry = 0
        while (l1 != None or l2 != None or carry != 0):
            if l1:
                l1_val = l1.val
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
            else:
                l2_val = 0

            result = l1_val + l2_val + carry
            current_node.next = ListNode(result % 10)
            carry = result // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            current_node = current_node.next
        return head_node.next