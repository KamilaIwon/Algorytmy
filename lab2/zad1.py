
from typing import Any

class Node:
    value: Any
    next: 'Node'

class LinkedList:
    head: Node
    tail: Node


    def __init__(self) -> None:
        self.head = None
        self.tail = None


    def push(self, value: Any) -> None:
        new: Node = Node()
        new.value = value
        new.next = self.head
        if self.tail is None:
            self.tail = new
        self.head = new


    def append(self, value: Any) -> None:
        new: Node = Node()
        new.value = value
        new.next = None
        if self.head is None:
            self.head = new
        if self.tail:
            self.tail.next = new
        self.tail = new


    def node(self, at: int) -> Node:
        if self.head is None:
            return None
        current: Node = self.head
        current_temp = 0
        while current_temp < at:
            if current.next is None:
                return None
            current = current.next
            current_temp += 1
        return current


    def insert(self, value: Any, after: Node) -> None:
        if after is None:
            return None
        new: Node = Node()
        new.value = value
        if after == self.tail:
            after.next = new
            self.tail = new
        new.next = after.next
        after.next = new


    def pop(self) -> Node:
        popped: Node = self.head
        self.head = popped.next
        popped.next = None
        return popped.value


    def remove_last(self) -> Node:
        length = len(self)
        last: Node = self.tail
        if length <= 1:
            self.tail = None
            self.head = None
            return last
        self.tail = self.node(len(self) - 2)
        self.tail.next = None
        return last.value


    def remove(self, after: Node) -> None:
        if after is None:
            return None
        else:
            self.tail = after
            after.next = None


    def __str__(self) -> str:
        list = ""
        temp = self.head
        if temp is None:
            return str(None)
        while temp is not None:
            if temp.next is not None:
                list = list + str(temp.value) + ' -> '
            else:
                list = list + str(temp.value)
            temp = temp.next
        return list


    def __len__(self) -> int:
        current = self.head
        length = 0
        if current is None:
            return 0
        while current is not None:
            length = length + 1
            current = current.next
        return length

list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)


assert str(list_) == '0 -> 1 -> 9 -> 10'

middle_node = list_.node(at=1)
list_.insert(5, after=middle_node)

assert str(list_) == '0 -> 1 -> 5 -> 9 -> 10'
print(list_)
print(len(list_))

first_element = list_.node(at=0)
returned_first_element = list_.pop()

assert first_element.value == returned_first_element

last_element = list_.node(at=3)
returned_last_element = list_.remove_last()

assert last_element.value == returned_last_element
assert str(list_) == '1 -> 5 -> 9'

second_node = list_.node(at=1)
list_.remove(second_node)

assert str(list_) == '1 -> 5'

print(len(list_))
print(list_.remove_last())
print(list_)
print(len(list_))