# C950 WGUPS package delivery system

The WGUPS Package Delivery system is a type of Traveling Salesman program. In this program, I am required to find the best route for a delivery truck based on a list of constraints. This program was built using the Python programming language and designed using the OOP approach.

- This program is designed to:
- Read in a .csv list off address 
- Create a weighted graph 
- Read in a .csv list of packages.
- Sort through the packages based on addresses and other constraints
- Decide on which truck the packages should go on
- Find the optimized route for each of the trucks (using a greedy algorithm)
- Keep track of delivery statuses
- Keep track of miles driven 
- Print a report of all packages for any given time

This program demonstrates how to:
- Build a chaining hash table
- Build a weighted graph
- Use the Greedy algorithm

To make it better:
This program runs and does what it’s supposed to. However, there should be a better way of sorting through the packages.csv file.
In my code, I had to dynamically pull packages from one truck and insert them into another. Even though I am allowed to do this in this project, I think that it is inefficient. There should be an algorithm that sorts through the packages and inserts them into the correct trucks based on efficiency and package constraints
