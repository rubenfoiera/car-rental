import random

class Vehicle(object):

    veh_id = 0
    veh_sold = []

    def __init__(self,year,mileage,purchase_price,ser_numb):
        self.__year = year
        self.__mileage = mileage
        self.__purchase_price = purchase_price
        self.__ser_numb = ser_numb
        self.__veh_id = Vehicle.veh_id
        Vehicle.veh_id += 1

    def get_id(self):
        return self.__veh_id

    def __str__(self):
        return "%d" %(self.veh_id)

    @staticmethod
    def generate_vehicle_id():
        Vehicle.veh_id += 100000

Vehicle.generate_vehicle_id()

class Car(Vehicle):

    def __init__(self,year,mileage,purchase_price,ser_numb,doors,wheels):
        super().__init__(year,mileage,purchase_price,ser_numb)
        self.__doors = doors
        self.__wheels = wheels

class Lorry(Vehicle):

    def __init__(self,year,mileage,purchase_price,ser_numb,doors,wheels=2):
        super().__init__(year, mileage, purchase_price, ser_numb)
        self.__doors = doors
        self.__wheels = wheels

class Motorcycle(Vehicle):

    class_count = 0

    def __init__(self,year,mileage,purchase_price,ser_numb,classic=False):
        super().__init__(year,mileage,purchase_price,ser_numb)
        self.__classic = classic
        self.__class = Motorcycle.class_count
        Motorcycle.class_count += 1

class Customer(object):

    def __init__(self, name):
        self.__name = name
        self.__score = self.credit_score()

    def credit_score(self):
        integer = random.randint(1,101)
        if integer > 60:
            return True
        else:
            return False

    def get_score(self):
        return self.__score

    def __str__(self):
        return "Customer: %s" %(self.__name)

class VIP_Customer(Customer):
    def __init__(self,name):
        super().__init__(name)

    def credit_score(self):
        return True

class Employee(object):
    emp_id = 0

    def __init__(self,name):
        self.__name = name
        self.__id = Employee.emp_id
        Employee.emp_id += 1

    def get_name(self):
        return self.__name

    def get_title(self):
        return "%s" %("Subordinate")

    def __str__(self):
        return "Employee: %s is of type %s" %(self.__name, self.get_title())

class Salesman(Employee):

    sales = {}

    def __init__(self, name):
        super().__init__(name)

    def sale(self,vehicle,sales_price,customer):

        if Customer.get_score():
            Salesman.sales[self] = Salesman.sales.get(self,0) + sales_price

        else:
            print("Customer does mot have enough credit score.")



Wendy = Customer("Wendy")
Heidi = VIP_Customer("Heidi")

print(Wendy) # expected output: Customer: Wendy
print(Heidi) # expected output: Customer: Heid
print(Wendy.get_score()) # expected output: True or False depending on random score
print(Heidi.get_score()) # expected output: True

#Veh1 = Vehicle(2008, 65000, 7500, "34567851g4")
#Veh2 = Vehicle(2008, 65000, 7500, "34567851g4")
#Veh3 = Vehicle(2008, 65000, 7500, "34567851g4")



