# 请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
#
# 若队列为空，pop_front 和 max_value 需要返回 -1
#
# 示例 1：
#
# 输入:
# ["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
# [[],[1],[2],[],[],[]]
# 输出: [null,null,null,2,1,2]
# 示例 2：
#
# 输入:
# ["MaxQueue","pop_front","max_value"]
# [[],[],[]]
# 输出: [null,-1,-1]

from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()  # 也可以用列表模拟，但是出队pop(0)是O(n)复杂度
        self.max_queue = deque()  # 用另一个双端队列，存储最大值，保证队头永远是当前的最大值，即单调递减队列

    def max_value(self) -> int:
        return self.max_queue[0] if self.max_queue else -1

    def push_back(self, value: int) -> None:  # 重点在这
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()  # 保证最大值队列永远单调递减。小于value的全部删除，然后value入队
        self.max_queue.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:  # 队列空了返回-1
            return -1
        else:
            if self.queue[0] == self.max_queue[0]:  # 若要出队的元素刚好是最大值，则将其在最大值队列中一并删除
                self.max_queue.popleft()
            return self.queue.popleft()

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()