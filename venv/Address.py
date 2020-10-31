# this class will act as a node in the weighted graph for the distance table.
# address class with getters and setters
# all O(1)
class Address:
    def __init__(self,  address, city, state, zip):
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        return "%s %s %s %s" % (self.address, self.city, self.state, self.zip)

    def id(self):
        return self.__str__()


    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

    def get_st(self):
        return self.address

    def get_zip(self):
        return self.zip

    def edit_address(self, new):
        self.address = new

    def edit_city(self, new):
        self.city = new

    def edit_zip(self, new):
        self.zip = new

    def edit_state(self, new):
        self.state = new
