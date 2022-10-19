from typing import Any, List


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __int__(self, value=Any):
        self.value = value
        self.children = None

    def __str__(self):
        return str(self.value)

    def is_leaf(self) -> bool:
        if self.children is None:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)


