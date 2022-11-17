from typing import Any, List, Callable, Union
from kolejka import Queue
import treelib


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value=Any):
        self.children = []
        self.value = value

    # sprawdzi czy węzeł jest liściem
    def is_leaf(self) -> bool:
        if self.children is []:
            return True
        return False

    # doda węzeł przyjęty w argumencie jako dziecko
    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self.value)  # odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit
        if self.children is []:
            return None
        else:
            for child in self.children:  # dla wszystkich dzieci bieżącego węzła
                child.for_each_deep_first(visit)  # wykonaj metodę for_each_deep_first()

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)  # odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit
        que = Queue()
        for child in self.children:  # wszystkie dzieci bieżącego węzła dodaj do pustej kolejki FIFO
            que.enqueue(child)

        while que.empty() is False:  # dopóki kolejka nie jest pusta
            element = que.dequeue()  # dla każdego pierwszego elementu w kolejce (element)
            visit(element)  # odwiedź element
            for child in element.children:
                que.enqueue(child)  # dodaj do kolejki wszystkie węzły, których rodzicem jest element

    # search(value: Any) -> Union['TreeNode', None], która sprawdzi
    # czy bieżący węzeł lub jego dzieci zawierają
    # wartość podaną w parametrze,
    # przy użyciu dowolnej metody przechodzenia po węzłach

    def search(self, value: Any) -> bool:
        if self.value == value:
            return True
        for child in self.children:
            if child.search(value):
                return True
        return False

    def __str__(self):
        return self.value


class Tree:
    root: TreeNode

    def __init__(self, root: 'TreeNode'):
        self.root = root

    def add(self, value: Any, parent_value: Any) -> None:
        def dzieci(node: 'TreeNode'):
            if node.children is not []:
                for child in node.children:
                    if child.value == parent_value:
                        tmp = TreeNode(value)
                        child.children.append(tmp)
                        break
                    else:
                        if child.children is not []:
                            dzieci(child)

        if(self.root.search(parent_value)):
            if self.root.value == parent_value:
                tmp = TreeNode(value)
                self.root.children.append(tmp)
            else:
                dzieci(self.root)
        else:
            print('nie ma parent_value o zawartosci: ', parent_value)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_level_order(visit)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        self.root.for_each_deep_first(visit)

    def show(self):
        tree = treelib.Tree()
        tree.create_node(str(self.root.value), str(self.root.value))

        def dzieci(node: 'TreeNode'):
            if node.children is not []:
                for child in node.children:
                    tree.create_node(str(child.value), str(child.value), parent=str(node.value))
                    if child.children is not []:
                        dzieci(child)

        dzieci(self.root)
        tree.show()


rootnode = TreeNode('F')
drzewo = Tree(rootnode)
drzewo.add('B', 'F')
drzewo.add('A', 'B')
drzewo.add('D', 'B')
drzewo.add('C', 'D')
drzewo.add('E', 'D')
drzewo.add('G', 'F')
drzewo.add('I', 'G')
drzewo.add('H', 'I')
drzewo.add('KK','KKK')

# drzewo.for_each_deep_first(print)
print("------------")
# drzewo.for_each_level_order(print)
print("------------")
drzewo.show()


