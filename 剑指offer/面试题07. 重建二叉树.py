# 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
#
#  
#
# 例如，给出
#
# 前序遍历 preorder = [3,9,20,15,7]
# 中序遍历 inorder = [9,3,15,20,7]
# 返回如下的二叉树：
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        dic = {val:i for i,val in enumerate(inorder)}   # 中序遍历的值与索引映射

        def recur(pre_root, l, r):  # pre_root前序遍历中根节点的索引，l，r中序遍历的左右边界
            if l > r:
                return None
            val = preorder[pre_root]
            index = dic[val]
            node = TreeNode(val)
            node.left = recur(pre_root + 1, l, index - 1)
            node.right = recur(pre_root + index - l + 1, index + 1, r)
            return node
        return recur(0, 0, len(preorder) - 1)