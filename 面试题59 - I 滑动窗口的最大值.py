# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。
#
# 示例:
#
# 输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7]
# 解释:
#
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
#
# 提示：
#
# 你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。
#
#
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/hua-dong-chuang-kou-de-zui-da-zhi-lcof
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''pre_max, cur_max分别记录上一个, 当前窗口最大值'''
        if not nums:
            return []

        res = []
        pre_max = max(nums[:k])
        res.append(pre_max)

        i, j = 1, k
        while j < len(nums):
            if nums[i-1] == pre_max:    # 如果上个窗口的最大值出队了，则重新计算当前最大值
                pre_max = max(nums[i:j+1])
                cur_max = pre_max
            else:
                cur_max = max(pre_max, nums[j])
                pre_max = cur_max
            res.append(cur_max)
            i += 1
            j += 1
        return res