from typing import Any


class Queue:
    def __init__(self) -> None:
        self._queue = []

    def enqueue(self, item: Any) -> None:
        self._queue.insert(0, item)

    def dequeue(self) -> Any:
        return self._queue.pop()

    @property
    def size(self) -> int:
        return len(self._queue)

    def is_empty(self) -> bool:
        return self._queue == []


class Deque:
    def __init__(self) -> None:
        self._deque = []

    def add_front(self, item: Any) -> None:
        self._deque.insert(0, item)

    def remove_front(self) -> Any:
        return self._deque.pop(0)

    def add_rear(self, item: Any) -> None:
        self._deque.append(item)

    def remove_rear(self) -> Any:
        return self._deque.pop()

    def is_empty(self) -> bool:
        return self._deque == []

    @property
    def size(self) -> int:
        return len(self._deque)
