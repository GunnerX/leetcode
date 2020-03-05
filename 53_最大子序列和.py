# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, max_sum = 0, nums[0]
        for num in nums:
            if sum > 0:     # 若sum > 0 说明sum对增大和有用，所以应保留并加上当前元素
                sum += num
            else:           # 若sum <= 0 说明sum对增大和没有用，所以应舍弃并重置为当前元素
                sum = num
            max_sum = max(max_sum, sum)
        return max_sum
