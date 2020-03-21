# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, j, sum = 0, 0, 0 # 左右指针，部分和
        res = len(nums) + 1 # res存储长度最终结果。因为要求最小值，所以初值为一定比数组长度的值
        for j in range(len(nums)):
            sum += nums[j]
            while sum >= s and i <= j:
                length = j - i + 1
                res = min(res, length)
                sum -= nums[i]
                i += 1
        return 0 if res == len(nums) + 1 else res