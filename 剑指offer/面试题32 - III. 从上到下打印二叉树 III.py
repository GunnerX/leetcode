# 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
#
#  
#
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回其层次遍历结果：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue, res = collections.deque(), []
        queue.append(root)
        flag = True # 奇数层为True,偶数层为false
        while queue:
            tmp = collections.deque()   # 保存每一层结果的双端队列。用list也可以，右端插入append，左端插入insert
            for i in range(len(queue)):
                node = queue.popleft()
                if flag:    # 若为奇数层，从右往左保存
                    tmp.append(node.val)
                else:       # 若为偶数层，从左往右保存
                    tmp.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            flag = not flag
            res.append(list(tmp))   # 注意最后把deque转化为list
        return res
