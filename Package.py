from importlib.resources import Package

import Address
import datetime
import csv



class Package:
    def __init__(self, package_ID, address, city, state, zip, delivery_deadline, mass_kilo, special_note):
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.packageID = package_ID
        self.deliveryDeadline = delivery_deadline
            #datetime.time(delivery_deadline)
        self.massKilo = mass_kilo
        self.specialNote = special_note


    def __str__(self):
        return "% s % s %s %s %s %s %s %s "% (self.packageID,self.address, self.city, self.state, self.zip, self.deliveryDeadline, self.massKilo, self.specialNote)

