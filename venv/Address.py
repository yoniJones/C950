# this class will act as a node in the weighted graph for the distance table.
class Address:
    def __init__(self, name,  address, city, state, zip):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return "%s %s %s %s %s" % (self.name, self.address, self.city, self.state, self.zip)

    def id(self):
        return self.__str__()
# path class
# linear representation of addresses
# wairhoese
# start list, next address. next address.