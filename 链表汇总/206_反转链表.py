# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 双指针
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p, q = None, head
        while q is not None:
            t = q.next
            q.next = p
            p = q
            q = t
        head = p
        return p

# 递归
    def reverseList1(self, head: ListNode) -> ListNode:
        if not head or not head.next:   # 前者空链表直接返回，后者则为递归到达尾部了，将尾结点返回
            return head
        node = self.reverseList(head.next)  # 保存翻转后的头结点，递归返回上层调用
        head.next.next = head   # 将翻转后的尾结点指向当前节点
        head.next = None    # 防止成环
        return node