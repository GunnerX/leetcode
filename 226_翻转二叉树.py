# 翻转一棵二叉树。
#
# 示例：
#
# 输入：
#
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# 输出：
#
#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/invert-binary-tree
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 递归
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 递归
        if not root:  # 根节点为空，结束条件
            return None

        root.left, root.right = root.right, root.left  # 交换当前的左右节点
        self.invertTree(root.left)  # 再递归的翻转左子树和右子树
        self.invertTree(root.right)

        return root

    # 非递归
    def invertTree2(self, root: TreeNode) -> TreeNode:
        if not root:    # 根节点为空直接返回None
            return None
        queue = [root]     # 用一个队列存储需要翻转的结点
        while queue:    # 若队列非空
            node = queue.pop(0)     # 第一个元素出队
            node.left, node.right = node.right, node.left   # 交换当前节点的左右子树
            if node.left:   # 若当前节点的左右子树非空，将其加入队列中
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root