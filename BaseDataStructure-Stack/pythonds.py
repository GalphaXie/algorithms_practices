from typing import Any


class Stack:
    def __init__(self):
        self._stack = []

    def push(self, item: Any) -> None:
        self._stack.append(item)

    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError("stack is empty")
        return self._stack.pop()

    @property
    def size(self) -> int:
        return len(self._stack)

    def is_empty(self) -> bool:
        return self._stack == []

    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError("stack is empty")
        return self._stack[-1]