from Address import Address
from Graph import Graph
import csv

# weighted graph deceleration for the distances


# retrieve data from the disances1.csv table and insert it into a list
# return a list of the rows in the distance table
address_node = []
distance_edge = []
weighted_graph_distance = []

# graph object
graph = Graph

# returns a list of the distances after extracting it from the distance.cvc file
def distance_data_retrieve():
    csv_distance_list = []
    with open('venv\Data\Distances1.csv', 'r') as csvfile:
        readCSV = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
        for row in readCSV:
            csv_distance_list.append(row)
        return csv_distance_list




#return a weighted graph
# O(n)
def create_weighted_graph(list):

    for row in list:
        name = row[0]
        street = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        graph.add_node(Address(name, street, city, state, zip))








list_distance = distance_data_retrieve()
create_weighted_graph(list_distance)
