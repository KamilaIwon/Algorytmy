from typing import Any

# klasa Node będzie reprezentacją węzła
class Node:
    value: Any
    next: 'Node'

# klasa LinkedList będzie reprezentacją listy jednokierunkowej
class LinkedList:
    head: Node
    tail: Node

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # umieszcza nowy węzeł na początku listy
    def push(self, value: Any) -> None:
        # tworzy nowy wiezel
        nowy: Node = Node()
        # nadaje mu wartosc
        nowy.value = value
        # ustawia obecna glowe jako wskanik na kolejny element
        nowy.next = self.head
        # przypadek gdy lista jest pusta
        if self.tail is None:
            self.tail = nowy
        # ustawiamy head jako nasz nowy element
        self.head = nowy


     # printuje liste
    def __str__(self) -> str:
        list = ""
        temp = self.head
        if temp is None:
            return str(None)
        while temp:
            if temp.next:
                list = list + str(temp.value) + ' -> '
            else:
                list = list + str(temp.value)
            temp = temp.next
        return list

    # umieszcza nowy węzeł na końcu listy
    def append(self, value: Any) -> None:
        # tworzy nowy wiezel
        nowy: Node = Node()
        # nadaje mu wartosc
        nowy.value = value
        # ustawia wskaznik na kolejny element (ostatni wiec None)
        nowy.next = None
        # przypadek gdy lista jest pusta
        if self.head is None:
            self.head = nowy
        # przypadek gdy lista nie jest pusta
        if self.tail:
            self.tail.next = nowy
        self.tail = nowy

    # zwraca węzeł znajdujący się na wskazanej pozycji
    def node(self, at: int) -> Node:
        # pusta lista
        if self.head is None:
            return None
        #nowy
        current: Node = self.head
        current_temp = 0
        while current_temp < at:
            if current.next is None:
                return None
            current = current.next
            current_temp += 1
        return current

    # wstawia nowy węzeł tuż za węzłem wskazanym w parametrze
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

    # usuwa i zwraca pierwszy element listy
    def pop(self) -> Node:
        popped: Node = self.head
        self.head = popped.next
        popped.next = None
        return popped.value

    # usuwa i zwraca ostatni element listy
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

    # przyjmuje węzeł jako argument, a następnie usuwa jego następnik
    def remove(self, after: Node) -> None:
        if after is None:
            return None
        else:
            self.tail = after
            after.next = None

    # podaje długość
    def __len__(self) -> int:
        current = self.head
        length = 0
        if current is None:
            return 0
        while current:
            length += 1
            current = current.next
        return length


list_ = LinkedList()

assert list_.head == None

list_.push(1)
list_.push(0)

print(list_)

assert str(list_) == '0 -> 1'

list_.append(9)
list_.append(10)


assert str(list_) == '0 -> 1 -> 9 -> 10'
print(list_)
print(len(list_))


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


print(list_.remove_last())
print(list_)
print(len(list_))
