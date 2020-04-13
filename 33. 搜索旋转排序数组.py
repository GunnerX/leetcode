# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
#
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
#
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
#
# 你可以假设数组中不存在重复的元素。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 示例 1:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 示例 2:
#
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        begin, end = 0, len(nums) - 1
        while begin <= end:
            mid = (begin + end) // 2

            # 找到target直接返回即可
            if nums[mid] == target:
                return mid

            # 如果左边有序
            if nums[begin] <= nums[mid]:
                # 如果target在mid左边
                if nums[begin] <= target <= nums[mid]:
                    end = mid - 1
                # 如果target在mid右边
                else:
                    begin = mid + 1
            # 如果右边有序
            else:
                # 如果target在mid右边
                if nums[mid] < target <= nums[end]:
                    begin = mid + 1
                # 如果target在mid左边
                else:
                    end = mid - 1
        return -1


