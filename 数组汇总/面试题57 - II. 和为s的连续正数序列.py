# # 输入一个正整数
# # target ，输出所有和为
# # target
# # 的连续正整数序列（至少含有两个数）。
# #
# # 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
# #
# #
# #
# # 示例
# # 1：
# #
# # 输入：target = 9
# # 输出：[[2, 3, 4], [4, 5]]
# # 示例
# # 2：
# #
# # 输入：target = 15
# # 输出：[[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]
# class Solution:
#     def findContinuousSequence(self, target: int) -> List[List[int]]:
#         i, j, sum, res = 1, 1, 0, []
#         while i < target / 2:
#             sum += j
#             while sum >= target:
#                 if sum == target:
#                     res.append([a for a in range(i, j+1)])
#                 sum -= i
#                 i += 1
#             j += 1
#         return res
#
# import time
#
# def get_time(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print('time: ', end-start)
#         return res
#     return inner
#
#
# @get_time
# def get(x):
#     sums = sum([i for i in range(x)])
#     print(sums)
#     return sums
#
# print(get(10000000))


nums = [2,3,1,0,2,5,3]
i = 0
m = nums[i]
nums[i], nums[m] = nums[m], nums[i]
print(nums)












