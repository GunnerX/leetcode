# 给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。
#
# 请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。
#
# 示例 1:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 1->3->5->2->4->NULL
# 示例 2:
#
# 输入: 2->1->3->5->6->4->7->NULL
# 输出: 2->3->6->7->1->5->4->NULL
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/odd-even-linked-list
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution: # 画图画图画图！！！
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head :
            return head
        odd = head
        even = head.next
        even_head = even
        while even and even.next:   # 注意边界条件
            odd.next = even.next
            even.next = even.next.next

            odd = odd.next
            even = even.next
        odd.next = even_head
        return head