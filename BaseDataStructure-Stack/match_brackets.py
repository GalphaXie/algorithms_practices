"""
题目描述:
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：
1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses

题解:
1. 类似的题目接触很多, 很容易想到用 Stack 这种基础数据结构;
2. if (、[、{ then 入栈;
3. if )、]、} 则从栈顶取一个元素进行比较;
    if 配对成功, 那么pop后 重复, 直到所有的字符比较结束, 栈是一个空栈: 返回 True
    else: 返回False
4. 漏掉了一个情况, 栈中元素全部被取出为空, 但是字符串中仍然有)、}、]的字符;

"""
from pythonds import Stack


def valid_parentheses(s: str) -> bool:
    stack = Stack()

    for char in s:
        if char in ["(", "[", "{"]:
            stack.push(char)
        else:
            if stack.is_empty():
                return False
            else:
                v = stack.peek()
                if v == "(" and char == ")":
                    stack.pop()
                elif v == "[" and char == "]":
                    stack.pop()
                elif v == "{" and char == "}":
                    stack.pop()
                else:
                    return False
    else:
        if stack.is_empty():
            return True
        else:
            return False


s = "()"  # True
s = "()[]{}"  # True
s = "(]"  # False
s = "([)]"  # False
s = "{[]}"  # True
print(valid_parentheses(s))
