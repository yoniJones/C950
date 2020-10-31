import csv
import datetime
import re
from Graph import Graph
from Warehouse import Warehouse
from Address import Address

# Jonathan Jones
# C950
# 10/29/2020

# takes a datetime value and a float value, converts the float value into
# minutes, adds the minutes to the dare
# space/time complexity O(1)
def add_time(current_time, added_time):
    d = datetime.timedelta(minutes=added_time)
    temp_time = datetime.datetime.combine(datetime.date(1, 1, 1), current_time)
    current_time = (temp_time + d).time()

    return current_time


# takes a datetime value and a float value, converts the float value into
# minutes, subtracts the minutes to the dare
# space/time complexity O(1)
def subtract_time(current_time, sub_time):
    if sub_time == 0 or sub_time == 0.0:
        return current_time
    d = datetime.timedelta(minutes=sub_time)
    temp_time = datetime.datetime.combine(datetime.date(1, 1, 1), current_time)
    current_time = (temp_time - d).time()

    return current_time


# takes a time in a string format and converts into a time()
# complexity O(1)
def convert_to_time(string_time):
    format = '%I:%M %p'
    try:
        converted_time = datetime.datetime.strptime(string_time, format).time()
        return converted_time
    except:
        return None



#  runs simulation for truck 1
# O(n^2 + 2n)
def run_simulation_truck1_part3():
    global truck3_departure_time
    global total_miles
    global truck3
    total_distance = 0.0
    test_time = datetime.datetime.strptime('11:00 AM', '%I:%M %p').time()
    test_time2 = datetime.datetime.strptime('10:30 AM', '%I:%M %p').time()
    time_tracker = datetime.datetime.strptime('8:00 AM', '%I:%M %p').time()

    # time/space complexity O(n)
    unvisited = truck1.copy()
    hub = Address("4001 South 700 East", "Salt Lake City", "UT", "84107")
    current_location = hub

    # greedy algorithm to find the nearest address
    # time/space complexity O(n^2)
    for i in truck1:
        min_distance = 65.0
        if len(unvisited) <= 1:
            distance = float(graph.get_distance(current_location, unvisited[0]))
            total_distance = total_distance + distance
            time_past = distance * 60 / 18
            time_tracker = add_time(time_tracker, time_past)
            current_location = unvisited[0]

            # going back to the hub
            distance = float(graph.get_distance(current_location, hub))
            total_distance = total_distance + distance
            time_past = distance * 60 / 18
            time_tracker = add_time(time_tracker, time_past)
            truck3_departure_time = time_tracker
        for j in unvisited:
            if j == current_location:
                continue
            distance = float(graph.get_distance(current_location, j))

            if distance <= min_distance:
                min_distance = distance
                temp_location = j

        # track the distance and update package delivery time
        if current_location in unvisited:
            unvisited.remove(current_location)
        current_location = temp_location

        # keeping track of distance traveled
        total_distance = total_distance + min_distance

        # calculate the time and add it to the time tracker
        time_past = (min_distance * 60) / 18
        time_tracker = add_time(time_tracker, time_past)
        current_location.set_delivery_time(time_tracker)

    # display truck 1
    # time/space complexity O(n)
    for i in truck1:
        print(i)
    # set up truck three departure time
    truck3_departure_time = time_tracker
    print("returned to hub " + str(truck3_departure_time))
    print("----------------END OF TRUCK1 SIMULATION -------------\n\n\n\n")
    total_miles += total_distance


# run simulation for truck 2
# time/space complexity O(n^2 + 2n)
# truck2 leaves at 9:05
def run_simulation_truck2_part3():
    global truck2
    global total_miles

    time_tracker = datetime.datetime.strptime('9:05 AM', '%I:%M %p').time()
    # used in if statement for updating package ID 9
    time2 = datetime.datetime.strptime('10:20 AM', '%I:%M %p').time()
    # keeps track of unvisited packages O(n)
    unvisited = truck2.copy()
    hub = Address("4001 South 700 East", "Salt Lake City", "UT", "84107")
    current_location = hub
    total_distance = 0.0

    # used in if statement when updating package ID 9
    changed = True

    # greedy algorithm to find the nearest address
    # time/space complexity O(n^2)
    for i in truck2:
        min_distance = 65.0
        if len(unvisited) <= 1:
            # returns the distance between two addresses
            # time/space complexity
            distance = float(graph.get_distance(current_location, unvisited[0]))

            # calculate the total distance, convert to time(in minutes), add minutes to time tracker
            total_distance = total_distance + distance
            time_past = distance * 60 / 18
            time_tracker = add_time(time_tracker, time_past)
            current_location = unvisited[0]
            break
        for j in unvisited:
            # skip if the location is the same
            if j == current_location:
                continue
            # returns the distance between two addresses
            distance = float(graph.get_distance(current_location, j))

            # keep track of minimum distance
            if distance <= min_distance:
                min_distance = distance
                temp_location = j

        # track the distance and update package delivery time
        if current_location in unvisited:
            unvisited.remove(current_location)

        # update current location
        current_location = temp_location

        # keep track of miles travled
        total_distance = total_distance + min_distance

        # calculate the time(in minutes), add the time to the time_tracker, update the
        time_past = (min_distance * 60) / 18

        time_tracker = add_time(time_tracker, time_past)
        current_location.set_delivery_time(time_tracker)

        # here packageID 9 gets address updated to 410 S State St., Salt Lake City, UT 84111 after 10:20
        # changed is a boolean value used to verify that the package does not get updated with every loop after 10:20
        if time_tracker >= time2 and changed:
            # new address object with updated address
            a = Address("410 S State St", "Salt Lake City", "UT", "8411")

            # retrieves address from the hash table
            # time/space complexity O(n)
            p = hash_map.get_item(9)
            # address updated here
            p.edit_address(a)
            changed = False

    # time/space complexity O(n)
    for i in truck2:
        print(i)
    print("Last package delivered at " + str(time_tracker))
    print("----------------END OF TRUCK2 SIMULATION -------------\n\n\n\n")

    # add to the total distance
    total_miles += total_distance


# run simulation for truck 3
# O(n^2 + 2n)
# leaves the hub at 9:28 AM(when truck1 returns). takes truck1 return time as a parameter
def run_simulation_truck3_part3(start_time):
    print("in truck 3 start time " + str(start_time))

    # shared variable that keeps track of the total miles traveled
    global total_miles
    global truck3
    total_distance = 0.0

    # initialize the time tracker
    time_tracker = start_time
    # unvisted list for looping O(n)
    unvisited = truck3.copy()

    hub = Address("4001 South 700 East", "Salt Lake City", "UT", "84107")
    current_location = hub

    # greedy algorithm to find the nearest address
    # time/space complexity O(n^2)
    for i in truck3:
        min_distance = 65.0
        if len(unvisited) <= 1:
            # retrieves the distance between 2 addresses
            distance = float(graph.get_distance(current_location, unvisited[0]))

            # calculate the total distance, convert to time(in minutes), add minutes to time tracker
            total_distance = total_distance + distance
            time_past = distance * 60 / 18
            time_tracker = add_time(time_tracker, time_past)
            current_location = unvisited[0]

        for j in unvisited:
            # skip testing against same location
            if j == current_location:
                continue
            # returns the distance between 2 addresses
            distance = float(graph.get_distance(current_location, j))

            # greedy algorithm here
            # find the shortest distance
            if distance <= min_distance:
                min_distance = distance
                temp_location = j

        # delete the delivered packages from the visited list
        if current_location in unvisited:
            unvisited.remove(current_location)
        # update the current location
        current_location = temp_location

        # update the miles traveled
        total_distance = total_distance + min_distance

        # calculate the total distance, convert to time(in minutes), add minutes to time tracker
        time_past = (min_distance * 60) / 18
        time_tracker = add_time(time_tracker, time_past)
        current_location.set_delivery_time(time_tracker)


# print report for truck 3 O(n)
    for i in truck3:
        print(i)

    print("Last Package delivered at " + str(time_tracker))
    print("----------------END OF TRUCK3 SIMULATION -------------\n\n\n\n")


    total_miles += total_distance
    # print report
    print("Total miles driven: " + str(total_miles))
    print("Last Package delivered at " + str(time_tracker))
    print("\n\n")


# reads in all addresses from Distances1.csv and returns a weighted graph object
# O(n)
def get_weighted_graph():
    with open('venv\Data\Distances1.csv', 'r') as csvfile:
        read_csv = csv.reader(csvfile, skipinitialspace=True, delimiter=',')
        weighted_graph = Graph(read_csv)
        return weighted_graph


# reads in all packages from Packages1.csv and returns a warehouse object containing
# the hash table that is holds all the packages
# time\space complexity O(n)
def get_packages():
    with open('venv\Data\Packages1.csv', 'r', encoding='utf-8-sig') as csvfile:
        read_csv1 = csv.reader(csvfile, skipinitialspace=True, delimiter=',')

        warehouse_obj = Warehouse(read_csv1)
        return warehouse_obj


# method used to sort the packages on to the trucks
#O(5n + n^2)
def sort_into_trucks(h_map):
    global truck1
    global truck2
    global truck3

    # a list of all the packages ID's that need to be on truck1
    global dependent_packages_id_truck1
    # a list of all the packages ID's that need to be on truck2
    global dependent_packages_id_truck2

    # lists that hold the street names for for each truck during the sort loop
    # this is used to keep packages with the same addresses on the same truck(for quicker delivery)
    global truck1_st_list
    global truck2_st_list
    global truck3_st_list
    # temperary list used to hold the packages when extracted from hash table
    temp_list = []
    # used for sorting into trucks
    test_time = datetime.datetime.strptime('10:00 AM', '%I:%M %p').time()
    test_time2 = datetime.datetime.strptime('12:00 AM', '%I:%M %p').time()

    # loop through hash table insert all packages into temp_list
    # complexity O(n^2)
    for row in range(len(h_map)):
        for package in range(len(h_map[row])):
            temp_list.append(h_map[row][package])

    # creating two lists, 1 sorted by delivery deadline and 1 sorted by street address O[2(n log(n))]
    sorted_by_delivery_deadline = sorted(temp_list, key=lambda package: package.deliveryDeadline)
    sorted_by_street = sorted(temp_list, key=lambda package: package.get_st())

    # populates dependent_packages_id_truck1 and dependent_packages_id_truck2
    # O(n)
    find_all_dependent_packages_attempt_2(sorted_by_delivery_deadline)

    # sort into trucks
    # complexity O(n)
    for i in sorted_by_street:
        id = int(i.get_package_ID())
        st = i.get_st()
        # truck 1 gets all the early deliveries
        if i.get_delivery_deadline() < test_time:
            truck1.append(i)
            truck1_st_list.append(st)
            sorted_by_delivery_deadline.remove(i)
        # truck 1 gets all the packages that need to be sent with other packages
        # and packages that have the same address as packages already in the truck
        elif id in dependent_packages_id_truck1 or st in truck1_st_list:
            truck1.append(i)
            sorted_by_delivery_deadline.remove(i)
        # truck 2 gets all the packages that are required to be on truck2,
        # packages that have the same address as packages already in the truck,
        # packages that  will not arrive to depot until 9:05
        elif id in dependent_packages_id_truck2 or st in truck2_st_list:
            truck2_st_list.append(st)
            truck2.append(i)
            sorted_by_delivery_deadline.remove(i)
        # truck 3 gets packages that have the same address as packages already in the truck,
        # and the rest of the packages that have a delivery deadline(temporarily)
        elif i.get_delivery_deadline() < test_time2 or st in truck3_st_list:
            truck3.append(i)
            truck3_st_list.append(st)
            sorted_by_delivery_deadline.remove(i)

    # whatever was not sorted into trucks get duped into truck 3
    # complexity O(n)
    for j in sorted_by_delivery_deadline:
        truck3.append(j)

    # removing early deliveries from truck 3 and inserting into truck 1
    # O(n)
    for i in truck3:
        if i.get_delivery_deadline() < datetime.datetime.strptime('12:00 PM', '%I:%M %p').time():
            truck3.remove(i)
            truck1.append(i)
    # fine tuning truck 3 to optimize the delivery time(not ideal but it works)
    truck1.append(truck3[0])
    truck3.pop(0)
    # removing packages with the ID's 37 and 30 from truck 2 into truck 1 for optimization
    # (not ideal but it works. i dont have time ill fix later )
    # complexity O(n)
    for i in truck2:
        if i.get_package_ID() in [37, 30]:
            truck1.append(i)
            truck2.remove(i)

# takes a time and prints out the statuse of the package delivery for that given time
# O(
def get_all_packages_before_given_time(time):
    # used for updating package ID 9 based on the time given
    address9 = Address("300 State St", "Salt Lake City", "UT", "84103")
    # used in the loop
    time_tester = datetime.datetime.strptime('9:05 AM', '%I:%M %p').time()
    time_tester2 = datetime.datetime.strptime('8:00 AM', '%I:%M %p').time()
    time_tester3 = datetime.datetime.strptime('10:20 AM', '%I:%M %p').time()
    time_tester4 = datetime.datetime.strptime('9:28 AM', '%I:%M %p').time()

    # loop through the entire hash table and print out the package in its delivery status
    # O(n^2)
    for row in range(len(hash_map.hash_table)):
        for package in range(len(hash_map.hash_table[row])):
            # gets ID from each package
            id = hash_map.hash_table[row][package].get_package_ID()
            # package 9 address gets updated at 10:20 so if the time < 10:20 then the address has not been updated yet
            if id == 9 and time < time_tester3:
                # save the current address before updating
                temp_address = hash_map.hash_table[row][package].get_address()
                # update address to old address
                hash_map.hash_table[row][package].edit_address(address9)
                if time <= time_tester:
                    print(str(hash_map.hash_table[row][package]) + " Status: At Hub")
                    # change back to updated address
                    hash_map.hash_table[row][package].edit_address(temp_address)
                else:
                    print(str(hash_map.hash_table[row][package]) + " Status: In Transit")
                    hash_map.hash_table[row][package].edit_address(temp_address)
            #  will not arrive to depot until 9:05 am
            elif time <= time_tester and "will not" in hash_map.hash_table[row][package].get_special_note():
                print(str(hash_map.hash_table[row][package]) + " Status: On the way to Hub for processing")
            # truck 2 leaves the hub at 9:05
            elif time <= time_tester and hash_map.hash_table[row][package] in truck2:
                print(str(hash_map.hash_table[row][package])+ " Status: At Hub")
            # if time entered is < 8:00
            elif time <= time_tester2:
                print(str(hash_map.hash_table[row][package]) + " Status: At Hub")
            # truck 3 leaves the hub at 9:28 AM
            elif time <= time_tester4 and hash_map.hash_table[row][package]  in truck3:
                print(str(hash_map.hash_table[row][package]) + " Status: At Hub")
            elif time < hash_map.hash_table[row][package].get_delivery_time():
                print(str(hash_map.hash_table[row][package]) + " Status: In Transit")
            else:
                a = " Status: Delivered at " + str(hash_map.hash_table[row][package].get_delivery_time())
                print(str(hash_map.hash_table[row][package]) + a)


# method used to view all the packages on the trucks(for testing purposes)
def print_trucks():
    global truck1
    global truck2
    global truck3
    print(len(truck1))
    print(len(truck2))
    print(len(truck3))
    print("truck 1")
    for i in range(len(truck1)):
        print(truck1[i])
    print("end")
    print("truck 2")
    for i in range(len(truck2)):
        print(truck2[i])
    print("end")
    print("truck 3")
    for i in range(len(truck3)):
        print(truck3[i])
    print("end")

def find_all_dependent_packages_attempt_2(sorted_temp_list):
    global truck1_st_list
    global truck2_st_list
    global truck3_st_list
    global dependent_packages_id_truck1
    global dependent_packages_id_truck2

    for i in range(len(sorted_temp_list)):
        id = int(sorted_temp_list[i].get_package_ID())
        st = sorted_temp_list[i].get_st()
        instruction = sorted_temp_list[i].get_special_note().lower()

        address_list = []
        package_group_list = []
        if "deliver with" in instruction:

            # Extracting the package ID(numbers) that this package must be delivered with.
            # These numbers are added to a list (packages_to_deliver_with)
            # all packages with accompanying package dependencies are loaded on to truck1
            if id not in dependent_packages_id_truck1:
                dependent_packages_id_truck1.append(id)
                truck1_st_list.append(st)
            elif id in dependent_packages_id_truck1 and st not in truck1_st_list:
                truck1_st_list.append(st)

            temp = re.findall(r'\d+', instruction)
            packages_to_deliver_with = list(map(int, temp))

            for j in packages_to_deliver_with:
                if j not in dependent_packages_id_truck1:
                    dependent_packages_id_truck1.append(j)


        elif "delayed" in instruction or "truck 2" in instruction or "wrong" in instruction or st in dependent_packages_id_truck2:
            dependent_packages_id_truck2.append(id)
            truck2_st_list.append(st)


# used to hold id's of packages that need to be sent with other packages
dependent_packages_id_truck1 = []
# used to hold the id of packages that need to be delivered on truck2
dependent_packages_id_truck2 = []

# used to track the addresses of the package so packages with same addresses get sent together
truck1_st_list = []
truck2_st_list = []
truck3_st_list = []

truck1 = []
truck2 = []
truck3 = []

total_miles = 0.0

# temp time for truck three departure. new time will be given once truck1 returns
truck3_departure_time = datetime.datetime.strptime('11:00 AM', '%I:%M %p').time()
warehouse = get_packages()
graph = get_weighted_graph()

hash_map = warehouse.hash_table

# arrange_into_trucks(hash_map)
sort_into_trucks(hash_map.hash_table)
answer = True
# 140
# simulation_truck1()
# 4001 South 700 East Salt Lake City UT 84107
# 2 2530 S 500 E Salt Lake City UT 84106 delivery deadline 17:00:00 44  delivered at None

# print_trucks()
run_simulation_truck1_part3()
run_simulation_truck2_part3()
run_simulation_truck3_part3(truck3_departure_time)
# run_simulation_truck2()


# time and space complexity O(n)
# interface
contin = True
while contin:
    string_time = input('At anytime enter 1 to exit.\nTo view the delivery status of your packages for a given time, please enter in a 12 hour time format.\nFor example, 12:15 AM or 3:30 PM HH:MM AM or HH:MM PM \n')

    if int(string_time) == 1:
        break
    converted_time = convert_to_time(string_time)
    if converted_time != None:
        print("Time entered: " + str(converted_time))
        get_all_packages_before_given_time(converted_time)
    else:
        print("Incorrect time entry. Please match format.")
