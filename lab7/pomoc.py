from typing import Callable, Dict, List, Optional, Any
from enum import Enum
from koll import Queue
#from graphviz import Graph as Gr


# TO DO: make show() better
#       add dijkstra algorithm
#       add shortest path in weighted graph algorithm

class EdgeType(Enum):
    directed = 1
    undirected = 2


class Vertex:
    '''
    data: Any
    index: int
    '''

    def __init__(self, data: Any, index: int) -> None:
        self.data = data
        self.index = index

    def __repr__(self) -> str:
        return f"{self.index}: {self.data}"


class Edge:
    '''
    source: Vertex
    destination: Vertex
    weight: Optional[float]
    '''

    def __init__(self, source: Vertex, destination: Vertex, weight: Optional[float]) -> None:
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self) -> str:
        return f'{self.destination}'


class Graph:
    adjacencies: Dict[Vertex, List[Edge]]

    def __init__(self) -> None:
        self.adjacencies = dict()

    def __repr__(self):
        output = ''
        for vertex in self.adjacencies:
            output += f"- {vertex} ----> {self.adjacencies[vertex]}\n"
        return output

    def create_vertex(self, data: Any) -> Vertex:
        new_vertex = Vertex(data, len(self.adjacencies))
        self.adjacencies[new_vertex] = list()
        return new_vertex

    def add_directed_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        new_edge = Edge(source, destination, weight)
        self.adjacencies[source].append(new_edge)

    def add_undirected_edge(self, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        self.add_directed_edge(source, destination, weight)
        self.add_directed_edge(destination, source, weight)

    def add(self, edge: EdgeType, source: Vertex, destination: Vertex, weight: Optional[float] = None) -> None:
        if edge == edge.directed:
            self.add_directed_edge(source, destination, weight)
        if edge == edge.undirected:
            self.add_undirected_edge(source, destination, weight)

    def traverse_breadth_first(self, visit: Callable[[Any], None]) -> None:
        keys = []
        for key in self.adjacencies.keys():
            keys.append(key)
        visited = []
        queue = Queue()
        queue.enqueue(keys[0])

        while queue.empty != False:
            v = queue.peek()
            if v not in visited:
                visit(v)
                visited.append(v)
            if len(visited) == len(keys):
                return
            for vertex in self.adjacencies[v]:
                if vertex.destination not in visited:
                    queue.enqueue(vertex.destination)

    def traverse_depth_first(self, visit: Callable[[Any], None]) -> None:
        keys = []
        for key in self.adjacencies.keys():
            keys.append(key)
        visited = [keys[0]]
        self.dfs(keys[0], visited, visit)

    def dfs(self, v: Vertex, visited: List[Vertex], visit: Callable[[Any], None]):
        visit(v)
        if v not in visited:
            visited.append(v)
        for vertex in self.adjacencies[v]:
            if vertex.destination not in visited:
                self.dfs(vertex.destination, visited, visit)

    def show(self):
        _show = Gr()
        _show.attr(shape='circle')
        _set = set()
        list_of_elements = []
        for key in self.adjacencies.keys():
            for edge in self.adjacencies[key]:
                new_element = (str(edge.source.data), str(edge.destination.data))
                if new_element not in list_of_elements and new_element[::-1] not in list_of_elements:
                    list_of_elements.append(new_element)

        print(list_of_elements)
        for element in list_of_elements:
            _set.add(element)
            _show.edge(element[0], element[1])
        # print(*_set)
        print(_show)
        _show.render(f'output/graf{random.random()}', view=True, format="png", quiet_view=False)


class GraphPath:

    def friend_path(g: Graph, f0: Any, f1: Any) -> List[Any]:
        visited = [f0]
        queue = Queue()
        queue.put(f0)
        parents = dict()
        while queue.not_empty:
            v = queue.get()
            if v not in visited:
                visited.append(v)
            if v == f1:
                break
            for vertex in g.adjacencies[v]:
                if parents.get(vertex.destination) is None:
                    parents[vertex.destination] = v
                else:
                    if parents.get(v) != parents.get(vertex.destination) and vertex.destination not in visited:
                        parents[vertex.destination] = v
                if vertex.destination not in visited:
                    if vertex.destination == f1:
                        visited.append(vertex.destination)
                        return visited, parents
                    queue.put(vertex.destination)
        return []
'''
    def display(start: Vertex, end: Vertex, graph) -> None:
        print()
        print(f"looking for path from {start.data} to {end.data}")
        path_ = []
        path, parents = GraphPath.friend_path(graph, start, end)
        while end != start:
            path_.append(end.data)
            # print(end.data, end=" ---> ")
            end = parents[end]
        path_.append(end.data)
        print(' ---> '.join(path_[::-1]))
'''

vertexs = ["VI", "RU", "PA", "CO", "CH", "SU", "KE", "RA"]
graph = Graph()
for vertex in vertexs:
    graph.create_vertex(vertex)
keys = [key for key in graph.adjacencies.keys()]
graph.add(EdgeType.undirected, keys[0], keys[4])
graph.add(EdgeType.undirected, keys[0], keys[1])
graph.add(EdgeType.undirected, keys[0], keys[2])

graph.add(EdgeType.undirected, keys[1], keys[7])
graph.add(EdgeType.undirected, keys[1], keys[5])
graph.add(EdgeType.undirected, keys[1], keys[0])

graph.add(EdgeType.undirected, keys[2], keys[3])
graph.add(EdgeType.undirected, keys[2], keys[6])

graph.add(EdgeType.undirected, keys[3], keys[1])
graph.add(EdgeType.undirected, keys[3], keys[0])


print(graph)
# CH - SU, CH - VI - RU - SU

print("Breadth First Traversal")
graph.traverse_breadth_first(print)
