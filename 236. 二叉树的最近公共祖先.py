# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
#
# 例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]
#
#
#
#  
#
# 示例 1:
#
# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def __init__(self):
        self.res = None

    def lowestCommonAncestor(self, root, p, q):

        def helper(node):
            if not node:
                return False

            left = helper(node.left)
            right = helper(node.right)

            if node == p or node == q:  # mid表示当前节点node是否为p或q
                mid = True
            else:
                mid = False

            if mid + left + right >= 2:
                self.res = node
            return mid or left or right  # mid,left,right有一个为True，即返回True

        helper(root)
        return self.res