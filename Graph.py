import Distance
from Address import Address
from Distance import Distance

# graph class
# processes the the distance.csv file into a weighted graph
class Graph:

    #O(n^2)
    def __init__(self, csv_list):
        # the node are addresses
        self.nodes = []
        # edge two addresses in the distance between them
        self.edges = []
        location1 = 0
        location2 = 0
        for row in csv_list:
            name = row[0]
            street = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            address = Address(street, city, state, zip)
            self.nodes.append(address)
            location2 = 0
            # distances in the csv file begin here
            for column in row[5:]:
                try:
                    edge = Distance(column, self.nodes[location1], self.nodes[location2])
                    self.edges.append(edge)
                    location2 = location2 + 1
                except IndexError:
                    pass
                continue
            location1 = location1 + 1


    # prints the entire grapg for testing perposes
    # O(n)
    def print_graph(self):
        for i in range(len(self.edges)):
          print(self.edges[i])

    # adds an node to the weighted graph
    # O(1)
    def add_node(self, n):
        self.nodes.append(n)

    # adds a wighted bi-directional edge between to addresses
    # O(1)
    def add_edge(self, n1, n2, e):
        distance = Distance(n1, n2, e)
        self.edges.append(distance)

    # Takes two addresses and return the distance between them
    # Space anf time complexity is O(n)
    def get_distance(self, n1, n2):
        # the city names in the given package.csv don't match the city names in the distances.csv. Therefore,
        # street address are used to compare

        st1 = n1.get_st()
        st2 = n2.get_st()
        for i in range(len(self.edges)):
            if str(st1) in str(self.edges[i].get_address1()) and str(st2) in str(self.edges[i].get_address2()):
                return self.edges[i].get_distance()
            elif str(st2) in str(self.edges[i].get_address1()) and str(st1) in str(self.edges[i].get_address2()):
                return self.edges[i].get_distance()
        print("not found")

    # takes an address and return a list of all connecting address
    # Space and time complexity is O(n)
    def get_connected_edges(self, node):
        st = node.get_st()
        close_by_list = []
        #print(node)
        for i in range(len(self.edges)):

            if str(st) in str(self.edges[i].get_address1()) and str(st) not in str(self.edges[i].get_address2()):
                close_by_list.append(self.edges[i])
            elif str(st) in str(self.edges[i].get_address2()) and str(st) not in str(self.edges[i].get_address1()):
                close_by_list.append(self.edges[i])
        return close_by_list


