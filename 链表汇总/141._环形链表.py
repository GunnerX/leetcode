# 给定一个链表，判断链表中是否有环。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
#
#  
#
# 示例 1：
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/linked-list-cycle
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:    # 空链表直接返回False
            return False
        quick, slow = head, head    # 快慢指针
        while quick:
            if not quick.next:  # 因为quick一次要走两格，所以要保证quick，quick.next都不为None
                return False
            quick = quick.next.next
            slow = slow.next
            if quick is slow:
                return True
        return False