# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: # 画图，清晰明了
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:  # 若链表长度小于2，直接返回
            return head

        sen = ListNode(-1)  # 哨兵节点
        sen.next = head
        p = sen  # 用p保存每次交换的左节点left

        while head and head.next:
            left, right = head, head.next
            p.next = right  # p指向right
            left.next = right.next  # 交换
            right.next = left
            # 更新
            p = left  # p保存此时的left
            head = head.next

        return sen.next