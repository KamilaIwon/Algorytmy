from enum import Enum
from typing import Any, Optional, Dict, List, Callable
from koll import Queue

class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    data: Any
    index: int

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index


class Edge:
    source: Vertex
    destination: Vertex
    weight: Optional[float]

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = dict()

    def create_vertex(self, data: Any) -> Vertex:
        new = Vertex(data, len(self.adjacencies))
        self.adjacencies[new] = list()
        return new

    def __repr__(self):
        lista = ''
        for x in self.adjacencies:
            lista += f'--{x.data}-->{self.adjacencies[x]}\n'
        return lista

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        nowy = Edge(source, destination, weight)
        self.adjacencies[source].append(nowy)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == edge.directed:
            self.add_directed_edge(source, destination, weight)
        else:
            self.add_undirected_edge(source, destination, weight)

    @staticmethod
    def wypisz(lista):
        for i in graf1.adjacencies:
            print(f'{i.index}: {i.data}')


graf1 = Graph()
A = graf1.create_vertex('A')
B = graf1.create_vertex('B')
C = graf1.create_vertex('C')
graf1.add(EdgeType.undirected, A, B)
print('-------------')
for i in graf1.adjacencies:
    print(f'{i.index}: {i.data}')

print(graf1)

