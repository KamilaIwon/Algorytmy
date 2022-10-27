from typing import Any, List, Callable


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value=Any):
        self.children = []
        self.value = value

    # sprawdzi czy węzeł jest liściem
    def is_leaf(self) -> bool:
        if self.children == []:
            return True
        return False

    # doda węzeł przyjęty w argumencie jako dziecko
    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    # wyprintuje drzewo
    def PrintTree(self):
        if self.children:
            print(self.value)
        if self.children != []:
            for x in b.children:
                print(x.value)
            self = self.children[0]



    # wykona operację przechodzenia po węzłach metodą deep first według następujących instrukcji:
    #
    # odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit (przyjętą w parametrze)
    # dla wszystkich dzieci bieżącego węzła wykonaj metodę for_each_deep_first()
    # na razie troche inne argumenty
    def for_each_deep_first(self) -> None:
        nodes_to_visit = [self]
        while len(nodes_to_visit) > 0:
            current_node = nodes_to_visit.pop()
            print(current_node.value)
            nodes_to_visit += current_node.children

        #visit()
        #if self.children is not None:
            #self.children.for_each_deep_first(visit)

    def for_each_level_order(visit: Callable[['TreeNode'], None]) -> None:
        return None
    '''
    która wykona operację przechodzenia po węzłach metodą level order według następujących instrukcji:

    odwiedź bieżący wierzchołek i wykonaj na nim funkcję visit (przyjętą w parametrze)
    wszystkie dzieci bieżącego węzła dodaj do pustej kolejki FIFO
    dopóki kolejka nie jest pusta, dla każdego pierwszego elementu w kolejce (element)
        odwiedź element
        dodaj do kolejki wszystkie węzły, których rodzicem jest element
    '''
b = TreeNode(10)
c = TreeNode(5)
d = TreeNode(3)
print(b.value)
print(b.children)
print(b.is_leaf())
b.add(c)
b.add(d)
print(b.children)

for x in b.children:
    print(x.value)
print("------------")
b.for_each_deep_first()
print("------------")
b.PrintTree()
