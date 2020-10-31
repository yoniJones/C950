from Package import Package
from Hash_table import ChainingHashTable
import datetime



# takes a time in as a string and converts it into a time()
# O(1)
def convert_to_time(string_time):
    format = '%I:%M %p'

    if string_time == 'EOD':
        string_time = '05:00 PM'

    converted_time = datetime.datetime.strptime(string_time, format).time()
    return converted_time

# takes a csv file in the constructor and populates the hash table
class Warehouse():
    def __init__(self, csv_package_list1):

        self.hash_table = ChainingHashTable()

        self.delivery_deadline = datetime

        # loops through the csv list, creates package objects and inserts the object into the hash table
        # O(n)
        for row in csv_package_list1:
            id = row[0]
            address = row[1]
            city = row[2]
            state = row[3]
            zip = row[4]
            self.delivery_deadline = convert_to_time(row[5])
            weight = row[6]
            note = row[7]
            self.package = Package(id, address, city, state, zip, self.delivery_deadline, weight, note)
            self.hash_table.insert(self.package)

            # if the package has a special instruction then it is handled by the special instruction method
            # packages that need to be delivered together are already handled


