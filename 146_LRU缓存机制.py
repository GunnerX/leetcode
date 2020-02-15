# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
#
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
#
# 进阶:
#
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
# 示例:
#
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/lru-cache
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Node:

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None



class LRUCache:
    '''双向链表 + 字典'''

    def __init__(self, capacity: int):
        self.capacity = capacity    # 容量
        self.dict = {}      # 字典
        self.head = Node()  # 头结点
        self.tail = Node()  # 尾节点
        self.head.next = self.tail     # 初始化尾头结点指向尾结点，尾结点指向头结点
        self.tail.prev = self.head



    def _add_node_to_tail(self, node):
        '''在在右边，即尾结点之前新添加一个结点'''
        self.dict[node.key] = node      # 疑问！！！ 为什么不是 = node.value??????????
        tail_prev = self.tail.prev      # 用tail_prev来保存添加之前尾结点之前的结点
        tail_prev.next = node           #
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node


    def _remove_node(self, node):
        '''删除一个节点'''
        self.dict.pop(node.key)     # 先删除字典中的键值对
        node.prev.next = node.next  # 再将结点抽出来
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        '''取元素'''
        if key in self.dict:       # 如果key存在，则将其结点放到最右边在取值
            node = self.dict[key]       # 疑问！！！ self.dict[key]应该是个value，为什么直接当做node?
            self._remove_node(node)
            self._add_node_to_tail(node)
            return node.value
        else:       # key不存在则返回-1
            return -1


    def put(self, key: int, value: int) -> None:
        '''添加元素'''
        node = Node(key, value)
        if key in self.dict:        # 如果key已存在,则直接将其删除
            self._remove_node(self.dict[key])
        if len(self.dict) == self.capacity:     # 如果缓存区已满
            self._remove_node(self.head.next)       # 删除最左边的元素
        self._add_node_to_tail(node)    # 将node添加进来


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)