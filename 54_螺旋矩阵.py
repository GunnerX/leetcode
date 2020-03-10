# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
# 示例 2:
#
# 输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/spiral-matrix
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''每次从左到右，从上到下，在从右到左，从下到上，4个步骤打印一周，为一个大循环。
        用l, r, t, d代表每次的上下左右边界.注意边界条件'''
        if not matrix:
            return []
        res = []
        l, r, t, d = 0, len(matrix[0]) - 1, 0, len(matrix)-1
        while True:
            for i in range(l,r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > d:
                break;
            for i in range(t,d + 1):
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            for i in range(r,l - 1,-1):
                res.append(matrix[d][i])
            d -= 1
            if t > d:
                break
            for i in range(d,t - 1,-1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break
        return res



