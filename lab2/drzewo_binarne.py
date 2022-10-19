import treelib
from typing import Any, Callable

# binarny węzeł drzewa przechowujący wartość oraz lewe i prawe dziecko.
class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    # inicjalizator ustawia wartość bieżącego węzła
    def __init__(self, value=Any):
        self.left_child = None
        self.right_child = None
        self.value = value

    # przesłonięcie metody w celu uzyskania wartości
    def __str__(self):
        return str(self.value)

    # is_leaf() sprawdza czy węzeł jest liściem
    def is_leaf(self):
        if (self.right_child == None) and (self.left_child == None):
            return True
        elif (self.right_child != None) and (self.left_child != None):
            return False
        else:
            return False

    # add_left_child dodaje lewe dziecko bieżącego węzła jako nowy węzeł
    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    # add_right_child dodaje prawe dziecko bieżącego węzła jako nowy węzeł
    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    # traverse_post_order wykonuje operację wstecznego przejscia po podrzędnych węzłach
    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child != None:
            self.right_child.traverse_in_order(visit)

    # traverse_pre_order wykonuje operację wzdłużnego przejścia po podrzędnych węzłach
    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child != None:
            self.left_child.traverse_post_order(visit)
        if self.right_child != None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    # traverse_pre_order wykonuje operację wzdłużnego przejścia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child != None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child != None:
            self.right_child.traverse_pre_order(visit)

# przechowuje strukturę drzewa binarnego
class BinaryTree:
    root: BinaryNode

    # inicjalizator, root reprezentuje węzeł będący korzeniem
    def __init__(self, value= Any):
        self.root = BinaryNode(value)

    # traverse_in_order wykonuje operację poprzecznego przejścia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    # traverse_post_order wykonuje operację wstecznego przejscia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    # traverse_pre_order wykonuje operację wzdłużnego przejścia po podrzędnych węzłach rozpoczynając od korzenia
    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    # wyświetla drzewo w formie graficznej
    def show(self):
        # utworzenie reprezentacji drzewa za pomocą biblioteki TreeLib
        binary_tree = treelib.Tree()
        binary_tree.create_node(str(self.root.value), str(self.root.value))

        # odwołanie się do podrzędnych węzłów left_child i right_child
        # jeżeli istnieją to tworzymy z nich Node z wartościami
        def binary_children(node: 'BinaryNode'):
            if node.left_child != None:
                binary_tree.create_node(str(node.left_child.value), str(node.left_child.value), parent=str(node.value))
            if node.right_child != None:
                binary_tree.create_node(str(node.right_child.value), str(node.right_child.value), parent=str(node.value))

        # wzdłużne przejście po podrzędnych węzłach - dzieciach
        self.traverse_pre_order(binary_children)

        # wyświetlenie drzewa
        binary_tree.show(line_type="ascii-emv")

# zwraca najbliższy wspólny węzeł nadrzędny przekazanych węzłów first_node->node1 , second_node ->node2
def closest_parent(binary_tree: BinaryTree, node1: BinaryNode, node2: BinaryNode):

    # jeżeli node1 lub node2 istnieją to zwracamy drzewo postaci instancji binary_tree
    if binary_tree == node1 or binary_tree == node2:
        return binary_tree

    # jeżeli binary_tree jest puste, nieokreślone to zwracamy None
    elif binary_tree == None:
        return None

    # przeszukanie z lewej strony
    left = closest_parent(binary_tree.left_child, node1, node2)

    # przeszkanie z prawej strony
    right = closest_parent(binary_tree.right_child, node1, node2)

    # jeżeli lewa i prawa strona nie jest pusta to zwracamy drzewo binarne
    if left != None and right != None:
        return binary_tree
    elif left != None:
        return left
    elif right != None:
        return right
    else:
        return None


# dodajemy korzeń, root, jego wartość wynosi 10
binary_tree = BinaryTree(10)

# dodajemy lewe dziecko
binary_tree.root.add_left_child(8)

# dodajemy prawe dziecko
binary_tree.root.add_right_child(2)

# dodajemy lewego potomka lewemu dziecku
binary_tree.root.left_child.add_left_child(1)

# dodajemy prawego potomka lewemu dziecku
binary_tree.root.left_child.add_right_child(5)

# dodajemy lewego potomka prawemu dziecku
binary_tree.root.right_child.add_left_child(4)

# dodajemy prawego potomka lewemu dziecku
binary_tree.root.right_child.add_right_child(7)

# drukujemy drzewo na ekran
binary_tree.show()

# wyszukiwanie nadrzędnego węzła dla pary (2,8)
print("Closest parent of (2,8): ",closest_parent(binary_tree.root, binary_tree.root.right_child, binary_tree.root.left_child))

# wyszukiwanie nadrzędnego węzła dla pary (1,5)
print("Closest parent of (1,5): ",closest_parent(binary_tree.root, binary_tree.root.left_child.left_child, binary_tree.root.left_child.right_child))

# wyszukiwanie nadrzędnego węzła dla pary (4,7)
print("Closest parent of (4,7): ",closest_parent(binary_tree.root, binary_tree.root.right_child.left_child, binary_tree.root.right_child.right_child))

# wyszukiwanie nadrzędnego węzła dla pary (2,4)
print("Closest parent of (2,4): ",closest_parent(binary_tree.root, binary_tree.root.right_child, binary_tree.root.right_child.left_child))

# wyszukiwanie nadrzędnego węzła dla pary (1,8)
print("Closest parent of (1,8): ",closest_parent(binary_tree.root, binary_tree.root.left_child.left_child, binary_tree.root.left_child))

# wyszukiwanie nadrzędnego węzła dla pary (5,7)
print("Closest parent of (5,7): ",closest_parent(binary_tree.root, binary_tree.root.left_child.right_child, binary_tree.root.right_child.right_child))

# wyszykiwanie nadrzędnego węzła jeżeli argumenty first_node i second_node nie są określone -> None
print("Closest parent of (None, None): ",closest_parent(binary_tree.root, None, None))



# testy poprawności implementacji

# wartość w korzeniu drzewa wynosi 10
assert binary_tree.root.value == 10

# wartość prawego dziecka korzenia wynosi 2
assert binary_tree.root.right_child.value == 2

# prawe dziecko nie jest liściem
assert binary_tree.root.right_child.is_leaf() is False

# wartość skrajnie lewego liścia drzewa wynosi 1
assert binary_tree.root.left_child.left_child.value == 1

# skrajnie prawe dziecko jest liściem
assert binary_tree.root.left_child.left_child.is_leaf() is True