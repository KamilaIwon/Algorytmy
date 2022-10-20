from lista_jednokierunkowa import Node
from lista_jednokierunkowa import LinkedList
from typing import Any

class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    #zwróci wartość pierwszego elementu w kolejce
    def peek(self) -> Any:
        return self._storage.head.value

    #umieści nowy element na końcu kolejki
    def enqueue(self, element) -> None:
        self._storage.append(element)

    #zwróci i usunie pierwszy element w kolejce
    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self) -> str:
        queue = ""
        temp = self._storage.head
        if self._storage is None:
            return str(None)
        queue += str(self._storage.head.value)
        while temp != self._storage.tail:
            temp = temp.next
            queue += (', ' + str(temp.value))
        return queue

    def __len__(self) -> int:
        return len(self._storage)

queue = Queue()

assert len(queue) == 0

queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
queue.enqueue('klient4')
queue.enqueue('klient5')

assert str(queue) == 'klient1, klient2, klient3, klient4, klient5'

client_first = queue.dequeue()

assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3, klient4, klient5'
assert len(queue) == 4

print(len(queue))

print(queue.peek())
queue.dequeue()
print(queue.peek())

print(len(queue))

print(queue)