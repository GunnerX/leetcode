# 给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
#
#  
#
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
#
# 进阶:
#
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
#
# 示例:
#
# 输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出: 7 -> 8 -> 0 -> 7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/add-two-numbers-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []     # 双栈法，用两个栈s1,s2来保存链表中的数，栈尾(顶)的元素即为最低位,
        while l1:
            s1 += [l1.val]
            l1 = l1.next
        while l2:
            s2 += [l2.val]
            l2 = l2.next

        carry = 0   # 进位信息
        head = ListNode(-1)     # 结果链表的头
        p = None
        while s1 or s2:
            n1 = s1.pop() if s1 else 0
            n2 = s2.pop() if s2 else 0

            sum = n1 + n2 + carry

            new = ListNode(sum % 10)
            head.next = new     # 链表的头插法，每次讲结果插入链表头。用尾插法则是反的
            new.next = p
            p = head.next

            if sum >= 10:
                carry = 1
            else:
                carry = 0

        if carry == 1:
            new = ListNode(1)
            head.next = new
            new.next = p

        return head.next