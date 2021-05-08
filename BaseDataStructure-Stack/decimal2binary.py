"""
topic:
    十进制转二进制
题解:
mod 2 取 余, 倒序
"""

from pythonds import Stack

def decimal_to_binary(value: int) -> int:
    stack = Stack()
    while value > 0:
        remainder = value % 2
        stack.push(remainder)
        value //= 2

    s = ""
    while not stack.is_empty():
        s += str(stack.pop())

    return int(s)
