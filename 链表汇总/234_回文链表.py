# 234. 回文链表
# 请判断一个链表是否为回文链表。
#
# 示例 1:
#
# 输入: 1->2
# 输出: false
# 示例 2:
#
# 输入: 1->2->2->1
# 输出: true


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        node = self.get_middle(head)  # 中间节点

        pre, cur = None, node  # 用来翻转后半部分链表
        while cur:
            t = cur.next
            cur.next = pre
            pre = cur
            cur = t
        left, right = head, pre  # 翻转完毕，left, right分别指向前，后半部分头部

        while right:  # 注意这里，因为前后链表可能等长也可能后半部分少一个，所以只要后面遍历完就可以了。画图理解
            if left.val != right.val:
                return False
            left, right = left.next, right.next

        return True

    # 找到中间节点
    def get_middle(self, head):
        quick, slow = head, head
        while quick and quick.next:
            quick, slow = quick.next.next, slow.next
        return slow