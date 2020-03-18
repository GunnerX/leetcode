# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 遍历，有重复就删除的做法
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy = ListNode(None)
        dummy.next = head
        node = dummy
        while node.next:
            if node.val == node.next.val:
                t = node.next
                node.next = node.next.next
                t.next = None
            else:
                node = node.next
        return dummy.next


    # 类似数组的做法，双指针改变值val
    def deleteDuplicates1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        left, right = head, head
        while right:
            if left.val != right.val:
                left = left.next
                left.val = right.val
            right = right.next
        left.next = None
        return head