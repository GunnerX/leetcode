# 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        '''递归'''
        if not root:
            return True
        def helper(left, right):
            if not (left or right): # 左右均为None
                return True
            if not (left and right):    # 左右只有一个为None
                return False
            if left.val != right.val:   # 不等
                return False
            return helper(left.left, right.right) and helper(left.right, right.left)    # 递归
        return helper(root.left, root.right)

    def isSymmetric1(self, root: TreeNode) -> bool:
        from collections import deque

        if not root or not (root.left or root.right):
            return True
        queue = deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if not (left or right):
                continue
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)  # 注意这里的添加顺序！
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True