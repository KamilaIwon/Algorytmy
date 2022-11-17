from lista_jednokierunkowa import Node
from lista_jednokierunkowa import LinkedList
from typing import Any

class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    #umieści nową wartość "na szczycie" stosu, czyli zostanie dodana na końcu wewnętrznej listy
    def push(self, element: Any) -> None:
        self._storage.append(element)

    #zwróci i usunie wartość ze szczytu stosu
    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self) -> str:
        stack = ""
        temp = self._storage.head
        if self._storage.head is None:
            return str(None)
        reverse_list: LinkedList = LinkedList()
        reverse_list.push(self._storage.head.value)
        while temp != self._storage.tail:
            temp = temp.next
            reverse_list.push(temp.value)
        temp = reverse_list.head
        stack += str(reverse_list.head.value)
        while temp != reverse_list.tail:
            temp = temp.next
            stack += ('\n' + str(temp.value))
        return stack

    def __len__(self) -> int:
        return len(self._storage)

stack = Stack()
print(stack)

assert len(stack) == 0

stack.push(3)

assert str(stack) == '3'

stack.push(10)
stack.push(1)

assert str(stack) == '1\n10\n3'

assert len(stack) == 3

top_value = stack.pop()

assert top_value == 1

assert len(stack) == 2


print(stack)
print("\n")
print(stack.pop())
print("\n")
print(stack)
print("\n")
print(len(stack))

stack.push(11)
top_value = stack.pop()
assert top_value == 11

stack.push(12)
top_value = stack.pop()
assert top_value == 12

stack.push(13)
stack.push(14)
top_value = stack.pop()
assert top_value == 14
top_value = stack.pop()
assert top_value == 13