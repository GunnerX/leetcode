# 给你一个长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。
#
#  
#
# 示例:
#
# 输入: [1,2,3,4]
# 输出: [24,12,8,6]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/product-of-array-except-self
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution: # 核心思路为 自己以外的乘积 = 左边乘积 * 右边乘积
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left, right = 1, 1  # 用left,right保存原数组中每个元素左边元素的乘积和右边元素的乘积
                            # 初始都为1代表首尾元素的左右乘积为1
        for i in range(len(nums)):  # 现在res中保存每个元素的左边元素乘积
            res.append(left)
            left *= nums[i]
        for i in range(len(nums) - 1, -1, -1):  # 再给每个左边乘积乘上右边乘积即可
            res[i] *= right
            right *= nums[i]
        return res

