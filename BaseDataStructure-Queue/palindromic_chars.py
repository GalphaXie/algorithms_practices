"""
算法:
    1. 从字符串的两端分别取出字符进行比较, 如果相等则重复上述动作;
    2. 如果队列中字符最后只有一个字符, 则字符长度是奇数, 也视为回文数;
"""

from pythonds import Deque


def is_palindromic(s: str) -> bool:

    chars_deque = Deque()

    for char in s:
        chars_deque.add_rear(char)

    still_equal = True

    while chars_deque.size > 1 and still_equal:
        first = chars_deque.remove_front()
        last = chars_deque.remove_rear()

        if first != last:
            still_equal = False

    return still_equal


if __name__ == '__main__':
    s = "abc"
    is_palindromic(s)