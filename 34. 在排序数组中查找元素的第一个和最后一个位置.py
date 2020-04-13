# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        # 用find_first来表示是寻找第一个还是最后一个位置
        def helper(find_first):
            # else之前的逻辑与二分查找一样
            n = len(nums)
            begin, end = 0, n - 1
            while begin <= end:
                mid = (begin + end) // 2
                if nums[mid] < target:
                    begin = mid + 1
                elif nums[mid] > target:
                    end = mid - 1

                else:
                    # 查找的是第一个位置
                    if find_first:
                        if mid > 0 and nums[mid] == nums[mid - 1]:
                            end = mid - 1
                        # mid = 0取到数组的第一个元素，或者nums[mid]不再等于nums[mid-1]说明找到了第一个位置
                        else:
                            return mid
                    # 查找的是最后一个位置
                    else:
                        if mid < n - 1 and nums[mid] == nums[mid + 1]:
                            begin = mid + 1
                        # mid = n - 1取到数组的最后一个元素，或者nums[mid]不再等于nums[mid+1]说明找到了最后一个位置
                        else:
                            return mid
            return -1

        return [helper(1), helper(0)]