import Distance
from Address import Address
from Distance import Distance


class Graph:

    """    def __init__(self, n, e):

        edge = ""
        node1 = 0
        node2 = 0
        counter = 0
        self.nodes = n
        self.edges = e
        for row in e:
            print(row)
            for column in row:
                print("second l")
                print("row " + row + " column " + column)"""

    def __init__(self, csv_list):
        self.nodes = []
        self.edges = []
        location1 = 0
        location2 = 0
        for row in csv_list:
            name = row[0]
            street = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            address = Address(name, street, city, state, zip)
            self.nodes.append(address)
            location2 = 0
            for column in row[5:]:
                try:
                    edge = Distance(column, self.nodes[location1], self.nodes[location2])
                    self.edges.append(edge)
                    location2 = location2 + 1
                except IndexError:
                    pass
                continue
            location1 = location1 + 1
        for i in range(len(self.edges)):
            print(self.edges[i])


    # adds an node to the weighted graph
    def add_node(self,n):
        self.nodes.append(n)

    # adds a wighted bi-directional edge between to addresses
    def add_edge(self,n1, n2, e):
        distance = Distance(n1, n2, e)
        self.edges.append(distance)


    # test data
    def print_graph(self):
        global graph
        for vertex in graph:
            for edges in graph[vertex]:
                print(vertex, " -> ", edges[0], " edge weight: ", edges[1])


"""
  #
    graph = {}
    nodes = {}
    #
    a1 = Address("WGU", "ward ave", "Salt Lake", "UT", "38556")
    a2 = Address("post office", "william st", "honolulu", "co", "38556")
    a3 = Address("Ranch House", "12 3rd st", "dencr", "co", "38556")
    a4 = Address("Bla Building", "first st", "eugene", "OR", "76343")




    add_node(a1)
    add_node(a2)
    add_node(a3)
    add_node(a4)
    #
    # # Add the edges between the vertices by specifying
    # # the from and to vertex along with the edge weights.
    add_edge(a1, a2, 1)
    add_edge(a2, a3, 1)
    add_edge(a3, a1, 3)
    add_edge(a4, a2, 4)
    add_edge(a4, a1, 5)
    print_graph(self=graph)
    # # Reminder: the second element of each list inside the dictionary
    # # denotes the edge weight.
"""
