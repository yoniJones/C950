from Package import Package

class Werehouse():
    def __init__(self, csv_package_list):
        self.truck1 = []
        self.truck2 = []
        self.truck3 = []
        self.truck4 = []
        for row in csv_package_list:

