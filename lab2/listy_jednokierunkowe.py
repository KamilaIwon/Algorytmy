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
        # tworzymy nowy wezel
        nowy: Node = Node()
        # ustawiamy jego wartosc
        nowy.value = value
        # ustawiamy wskaznk (obecny pierwszy element ustawiamy na drugi)
        nowy.next = self.head
        # jezeli lista jest pusta (brak ostatniego elementu)
        if self.tail is None:
            self.tail = nowy
        # ustawienie nowego wezla na pierwszy w liscie
        self.head = nowy

    # printuje liste
    def __str__(self) -> str:
        list = ""
        # wskaznik na poczatek listy
        temp = self.head
        # jezeli lista jest pusta
        if temp is None:
            return str(None)
        # przechodzimy przez liste
        while temp:
            if temp.next is not None:
                list += str(temp.value) + ' -> '
            else:
                list += str(temp.value)
                # wskaznik na kolejny element
            temp = temp.next
        return list

    # umieszcza nowy węzeł na końcu listy
    def append(self, value: Any) -> None:
        # tworzymy nowy wezel
        nowy: Node = Node()
        # ustawiamy wartosc
        nowy.value = value
        # ustawiamy brak kolejnego elementu
        nowy.next = None
        # jezeli lista jest pusta
        if self.head is None:
            self.head = nowy
        # wskaznik nastepnika ostatniego elementu ustawiamy na nasz nowy wezel
        if self.tail:
            self.tail.next = nowy
        # ustawiamy wezel jako ostatni
        self.tail = nowy

    # zwróci węzeł znajdujący się na wskazanej pozycji
    def node(self, at: int) -> Node:
        # pusta lista
        if self.head is None:
            return None
        # ustawiamy wskanik
        tmp: Node = self.head
        ile = 0
        # szukamy podanej wartosci
        while ile < at:
            # jezeli nie ma takiej pozycji (lista za krótka)
            if tmp.next is None:
                return None
            tmp = tmp.next
            ile += 1
        return tmp

    # wstawia nowy węzeł tuż za węzłem wskazanym w parametrze
    def insert(self, value: Any, after: Node) -> None:
        # jezeli brak podanego wezla
        if after is None:
            return None
        # tworzymy nowy wezel
        nowy: Node = Node()
        # ustawiamy jego wartosc
        nowy.value = value
        # jezeli podany wezel jest ostatnim
        if after == self.tail:
            after.next = nowy
            self.tail = nowy
        # wstawiamy wezel do listy
        nowy.next = after.next
        after.next = nowy

    # usunie pierwszy element z listy i go zwróci
    def pop(self) -> Node:
        # wskanik na pierwszy element
        nowy: Node = self.head
        # ustawiamy drugi element na pierwszy
        self.head = nowy.next
        # usuwamy element
        nowy.next = None
        return nowy.value

    # usunie ostatni element z listy i go zwróci
    def remove_last(self) -> Node:
        length = len(self)
        # wskaznik na ostatni element
        tmp: Node = self.tail
        # jezeli jest tylko 1 element lub lista jest pusta
        if length <= 1:
            self.tail = None
            self.head = None
            return tmp
        # ustawiamy nowy ostatni element
        self.tail = self.node(len(self) - 2)
        # ustawiamy pust nastepnik
        self.tail.next = None
        return tmp.value

    # usunie z listy następnik węzła przekazanego w parametrze
    def remove(self, after: Node) -> None:
        # jezeli brak takiego elementu
        if after is None:
            return None
        else:
            # usuwamy nastepnik
            self.tail = after
            after.next = None

    # wywołana na obiekcie listy zwróci jej długość
    def __len__(self) -> int:
        # wskaznik na poczatek
        tmp = self.head
        length = 0
        # gdy lista jest pusta
        if tmp is None:
            return 0
        # liczymy elementy
        while tmp:
            length = length + 1
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
