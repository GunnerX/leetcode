# 给定两个二叉树，编写一个函数来检验它们是否相同。
#
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
#
# 示例 1:
#
# 输入:       1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# 输出: true
# 示例 2:
#
# 输入:      1          1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# 输出: false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/same-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        '''两个根节点比较有4种情况，
        1 都为空，
        2 只有一个为空，
        3 都不为空且值相等，
        4 都不为空且值不等，
        只有当都不为空且值相等时再递归的比较左右子树'''

        if not p and not q: # 若根节点都为空，则返回True
            return True

        if not p and q:  # 若根节点只有一个为空
            return False
        if not q and p:
            return False

        if p.val == q.val:
            res_left = self.isSameTree(p.left, q.left)
            res_right = self.isSameTree(p.right, q.right)
            if res_left and res_right:
                return True
            else:
                return False
        else:
            return False


