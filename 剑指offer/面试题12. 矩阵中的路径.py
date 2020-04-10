# 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。
#
# [["a","b","c","e"],
# ["s","f","c","s"],
# ["a","d","e","e"]]
#
# 但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
#
#  
#
# 示例 1：
#
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# 输出：true
# 示例 2：
#
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):  # 如果下标越界
                return False
            if board[i][j] != word[k] or board[i][j] == '':
                return False
            # 否则就是匹配到了一个字符
            if k == len(word) - 1:  # 如果k==len(word)-1,说明word的最后一个字符也找到了，所以返回True
                return True
            tmp = board[i][j]  # 暂存当前board[i][j]，并将其置为空以防干扰下层递归，下次递归结束返回后在变回去
            board[i][j] = ''  # 并将其置为空以防干扰下层递归
            # 用or相连，表示有一个方向找到结果即可
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j] = tmp  # 下次递归结束返回后再变回去
            return res

            # 先遍历二维数组找到word的第一个字符，找到后对其开启dfs递归查找word中的每一个字符；若遍历完也为找到字符串第一个字符，直接返回False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False