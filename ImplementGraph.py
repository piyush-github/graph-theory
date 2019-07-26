class AdjacecnyList:
    def __init__(self, data):
        self.vertex = data
        self.next = None

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def add_edge(self, source, destination):
        node = AdjacecnyList(destination)
        node.next = self.graph[source]
        self.graph[source] = node

        node = AdjacecnyList(source)
        node.next = self.graph[destination]
        self.graph[destination] = node

    def print_graph(self):
        for node in range(self.V):
            print("Adjacency list of vertex {}\n head".format(node), end="")
            tempAdjacencyList = self.graph[node]
            while tempAdjacencyList:
                print(" -> {}".format(tempAdjacencyList.vertex), end="")
                tempAdjacencyList = tempAdjacencyList.next
            print(" \n")

if __name__ == "__main__":
    V = 5
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)

    graph.print_graph()

