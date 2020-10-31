from Package import Package


class ChainingHashTable:
    # complexity is O(1)
    def __init__(self, initial_capacity=10):
        self.hash_table = []
        for i in range(initial_capacity):
            self.hash_table.append([])

    # Inserts into hash table
    # complexity is O(1)
    def insert(self, package):
        # get hash index
        hash_index = package.get_package_ID() % 10
        # append the package to the end of the list
        self.hash_table[hash_index].append(package)

    # takes a package ID and return a package
    # complexity is O(n)
    def get_item(self, package_id):
        hash_index = package_id % 10
        hash_index_list = self.hash_table[hash_index]
        length_temp = len(hash_index_list)

        i = 0
        for i in range(length_temp):
            if hash_index_list[i].get_package_ID() == package_id:
                return self.hash_table[hash_index][i]
        return None
    # updates a package
    # O(n)
    def update(self, package):
        hash_index = package.get_package_ID() % 10
        hash_index_list = self.hash_table[hash_index]
        length_temp = len(hash_index_list)

        i = 0
        for i in range(length_temp):
            if hash_index_list[i].get_package_ID() == package.get_package_ID():
                self.hash_table[hash_index][i] = package
                print("item updated")
                return
        print("item not found")

