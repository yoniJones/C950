import csv

from Graph import Graph
from Address import Address
from Distance import Distance

# setting up
# retrieve all data from distance table
# creates an address object and inserts each address into a node list
# collects the distances from each row as a list and inserts each list into an edge list

# extracts data from the csv file and creates a bidirectional weighted graph


def get_weighted_graph():
    with open('venv\Data\Distances1.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
        weighted_graph = Graph(readCSV)

def get_packages():
    with open('venv\Data\Packages.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')



graph = get_weighted_graph()




    #print(edges)
# sets up the weighted graph








def retrieve_data():
    x =5

def set_test_data():
    list = {}

    a1 = Address("WGU", "ward ave", "Salt Lake", "UT", "38556")
    a2 = Address("post office", "william st", "honolulu", "co", "38556")
    a3 = Address("Ranch House", "12 3rd st", "dencr", "co", "38556")
    a4 = Address("Bla Building", "first st", "eugene", "OR", "76343")

    graph.add_node(a1)
    graph.add_node(a2)
    graph.add_node(a3)
    graph.add_node(a4)
    #
    # # Add the edges between the vertices by specifying
    # # the from and to vertex along with the edge weights.
    graph.add_edge(a1, a2, 1)
    graph.add_edge(a2, a3, 1)
    graph.add_edge(a3, a1, 3)
    graph.add_edge(a4, a2, 4)
    graph.add_edge(a4, a1, 5)
    for i in graph:
        print(i)
    #graph.print_graph(graph)
    # # Reminder: the second element of each list inside the dictionary
    # # denotes the edge weight.






