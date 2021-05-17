"""
场景描述:
1. 几个人添加到队列中, 指定一个周期数开始周期循环,
2. 从队列“头部”取出一个name后放入队列“尾部”, 直到一个周期结束, 将此时处于队列头部的人移出队列
2. 移出后的新队列的基础上重复 循环周期
"""
from pythonds import Queue


def hotpotato(names, num):

    queue = Queue()

    for name in names:
        queue.enqueue(name)

    while queue.size > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        else:
            queue.dequeue()

    return queue.dequeue()


if __name__ == '__main__':
    names = ["Bill", "David", "Susan", "Jane", "Kent", "Brad"]
    num = 7
    res = hotpotato(names, num)
    print(res)