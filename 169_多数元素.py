# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
# 示例 1:
#
# 输入: [3,2,3]
# 输出: 3
# 示例 2:
#
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
         # major为当前还无法删除的元素，count为其个数。
         # major初值必须为nums中没有的元素。或者也可major=nums[0],遍历nums[1:]
        major, count = 0, 0
        for num in nums:
            if not count: # 如果当前count为0，说明当前没有无法删除的元素，则更新major，count
                major = num
                count += 1
            else:   # 若当前count不为0,即存在无法删除的元素
                if num == major:    # 若num==major，说明两者相等，仍无法删除，count增加
                    count += 1
                else:       # 否则说明当前num可以抵消掉一个major，count减1
                    count -= 1
        return  major






