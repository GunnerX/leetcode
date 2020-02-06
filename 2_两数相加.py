# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)          # 创建一个新链表存储和
        i,j,p,c = l1,l2,head,0      # 用i，j，p遍历l1,l2，head , c为进位信息(0/1)
        while i or j:               # 当i,j都不为None，即没遍历完
            val1 = i.val if i else 0    # i还未链表l1遍历完，则加数val1 = i，否则为0
            val2 = j.val if j else 0    # j还未链表l2遍历完，则加数val1 = j，否则为0
            t = p                   # 用t存储当前p
            sum = val1 + val2 + c   #相加
            p = ListNode(sum % 10)      # p指向新结点
            t.next = p      # t指向p

            if i:   i = i.next  # i，j若还未遍历完则指向下一个节点
            if j:   j = j.next

            c = 0 if sum < 10 else 1    # 进位信息c

        if c:   # i,j都遍历完后，若仍有进位则再指向一个值为1的结点
            p.next = ListNode(1)
        return head.next











