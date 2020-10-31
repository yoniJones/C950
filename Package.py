from importlib.resources import Package

from Address import Address
import datetime
import csv

# package class with simple getters and setters
class Package(Address):
    def __init__(self, package_ID, address, city, state, zip, delivery_deadline, mass_kilo, special_note,
                 delivery_status="in route", delivery_time=None):
        super().__init__(address, city, state, zip)
        self.packageID = package_ID
        self.deliveryDeadline = delivery_deadline
        self.massKilo = mass_kilo
        self.specialNote = special_note
        self.delivery_status = delivery_status
        self.delivery_time = delivery_time

    def get_delivery_time(self):
        return self.delivery_time

    def get_delivery_deadline(self):
        return self.deliveryDeadline

    def get_delivery_status(self):
        return "%s" % self.delivery_status

    def get_special_note(self):
        return "%s" % self.specialNote

    def get_package_ID(self):
        return int(self.packageID)

    def get_weight(self):
        return int(self.massKilo)

    def get_address(self):
        return self.address

    def get_city(self):
        return self.city

    def get_state(self):
        return self.state

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

    def update_delivery_status(self, status):
        self.delivery_status = status

    def get_address(self):
        return Address(self.address, self.city, self.state, self.zip)

    def set_delivery_time(self, time):
        self.delivery_time = time;

    def __str__(self):
        return "% s % s %s %s %s delivery deadline %s %s %s delivered at %s" % (
            self.packageID, self.address, self.city, self.state, self.zip, self.deliveryDeadline, self.massKilo,
            self.specialNote, self.delivery_time)
