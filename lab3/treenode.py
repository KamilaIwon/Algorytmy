from typing import Any, List


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value=Any):
        self.children = []
        self.value = value

    def is_leaf(self) -> bool:
        if self.children is None:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)


b = TreeNode(10)
c = TreeNode(5)
d = TreeNode(3)
print(b.value)
print(b.children)
print(b.is_leaf())
b.add(c)
b.add(d)
print(b.children)

