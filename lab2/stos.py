
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
        nowy: Node = Node()
        nowy.value = value
        nowy.next = self.head
        if self.tail is None:
            self.tail = nowy
        self.head = nowy

    def append(self, value: Any) -> None:
        nowy: Node = Node()
        nowy.value = value
        nowy.next = None
        if self.head is None:
            self.head = nowy
        if self.tail:
            self.tail.next = nowy
        self.tail = nowy

    def node(self, at: int) -> Node:
        if self.head is None:
            return None
        tmp: Node = self.head
        i = 0
        while i < at:
            if tmp.next is None:
                return None
            tmp = tmp.next
            i += 1
        return tmp

    def insert(self, value: Any, after: Node) -> None:
        if after is None:
            return None
        nowy: Node = Node()
        nowy.value = value
        if after == self.tail:
            after.next = nowy
            self.tail = nowy
        nowy.next = after.next
        after.next = nowy

    def pop(self) -> Node:
        tmp: Node = self.head
        self.head = tmp.next
        tmp.next = None
        return tmp.value

    def remove_last(self) -> Node:
        length = len(self)
        ostatni: Node = self.tail
        if length <= 1:
            self.tail = None
            self.head = None
            return ostatni
        self.tail = self.node(len(self) - 2)
        self.tail.next = None
        return ostatni.value

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
        tmp = self.head
        length = 0
        if tmp is None:
            return 0
        while tmp is not None:
            length += 1
            tmp = tmp.next
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