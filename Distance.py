# this class will act as an edge for the weighted graph together with the Address class
# take  in two nodes


class Distance:
    def __init__(self, weight, node1, node2):
        self.distance = weight
        self.address1 = node1
        self.address2 = node2

    def __str__(self):
        return "from  %s to %s is: %s" %(self.address1,self.address2, self.distance)

    def id(self):
        return self.__str__()