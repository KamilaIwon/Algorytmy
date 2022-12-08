from listy_jednokierunkowe import Node
from listy_jednokierunkowe import LinkedList
from typing import Any

#bufor
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

    # zwróci i usunie ostatni element w kolejce
    def usun(self) -> Any:
        return self._storage.remove_last()

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

    def empty(self):
        if self._storage is None:
            return True
        return False
'''
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

queue.enqueue(11)
top_value = queue.usun()
assert top_value == 11

queue.enqueue(12)
top_value = queue.usun()
assert top_value == 12

queue.enqueue(13)
queue.enqueue(14)
top_value = queue.usun()
top_value = queue.usun()
assert top_value == 13
'''
