from typing import Any, List, Callable
import treelib

class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def min(self) -> 'BinaryNode':
        if self.left_child is not None:
            self.left_child.min()
        return self

    def __repr__(self):
        print(f'{self.value}')

    def is_leaf(self):
        if self.left_child is None and self.right_child is None:
            return True

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)

class BinarySearchTree:
    root: 'BinaryNode'

    def __init__(self, root: 'BinaryNode'):
        self.root = root

    def insert(self, value: 'Any') -> None:
        self._insert(self.root,value)

    def _insert(self, node: BinaryNode, value: Any) -> 'BinaryNode':
        if value < node.value:
            if node.left_child == None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(node.left_child, value)
        else:
            if node.right_child == None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(node.right_child, value)
        return node

    def insert_list(self, list_: List[Any]) -> None:
        for x in list_:
            self.insert(x)

    def contains(self, value: Any) -> bool:
        tmp = self.root
        while tmp is not None:
            if tmp.value == value:
                return True
            elif value <  tmp.value:
                tmp = tmp.left_child
            else:
                tmp = tmp.right_child
        return False

    def remove(self, value: Any) -> None:
        self.root = self._remove(self.root,value)

    def _remove(self, node: BinaryNode, value: Any) -> BinaryNode:
        if value == node.value:
            if node.is_leaf():
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
        if value < node.value:
            node.left_child = self._remove(node.left_child,value)
        if value > node.value:
            node.right_child = self._remove(node.right_child,value)
        return node

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        drzewo = treelib.Tree()
        drzewo.create_node(str(self.root.value), str(self.root.value))

        def dzieci(node: 'BinaryNode'):
            if node.left_child is not None:
                drzewo.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))

            if node.right_child is not None:
                drzewo.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        self.traverse_pre_order(dzieci)
        drzewo.show()






# testy

el_1 = BinaryNode(6)
drzewo = BinarySearchTree(el_1)
drzewo.insert_list([4,7,3,5,2])

print(drzewo.root.left_child.left_child.left_child.value)
print(drzewo.contains(2))
drzewo.remove(2)
print(drzewo.contains(2))
drzewo.show()