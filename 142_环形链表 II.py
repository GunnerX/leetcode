# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# #
# # 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# #
# # 说明：不允许修改给定的链表。
# #
# # 来源：力扣（LeetCode）
# # 链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
# # # 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not fast or not fast.next:   # 因为要访问fast.next.next, 所以要保证fast,fast.next均不为None
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
