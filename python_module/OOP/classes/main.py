"""Implementation of the Transport class"""


class Transport:
    """The parent Transport class has 2 attributes name and power"""
    steering_wheel = True

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __getattr__(self, attr):
        """Method informs about the absence of an attribute"""
        return print(f'Attribute "{attr}" does not exist')

    def __gt__(self, other):
        """Return True if hp 1 object greater than hp 2 object"""
        if self.power > other.power:
            return True

    def __ne__(self, other):
        """Return True if hp 1 object no equal hp 2 object"""
        if self.power != other.power:
            return True

    def name_of_transport(self):
        """Method displays the name of the transport"""
        print(f"I have - {self.name}")

    def fuel(self):
        """Type of fuel to be refueled"""
        print(f"Refuel my {self.name}")

    def power_rate(self):
        """The method displays the amount of horsepower the engine has been driving."""
        print(f"My {self.name} has {self.power} hp")

    @staticmethod
    def start():
        """Static method. Method implements a hypothetical engine start"""
        print("Transport started")

    @property
    def information(self):
        return f"{self.name}, {self.power}"


class Auto(Transport):
    """The child class describes an object - a car"""
    _fuel_tank = 40
    __max_distance = 500

    def __init__(self, name, power, model):
        Transport.__init__(self, name, power)
        self.model = model

    def __add__(self, other):
        """Override magic method __add__. Instrument for concatenate 2 cars"""
        car_park = []
        car_park.append(self.name)
        car_park.append(other.name)
        return car_park

    def __eq__(self, other):
        """Method compares object classes"""
        if isinstance(self, Auto) == isinstance(other, Auto):
            return True
        else:
            return False

    def fuel_consumption(self):
        """Fuel consumption per 100 km"""
        return self._fuel_tank*100/self.__max_distance

    def info(self):
        """Displays information about car"""
        print(f"I have {self.name} {self.model}, which has {self.power} hp")

    def fuel(self):
        print(f"Fill my {self.name}  with gasoline")


class Sportcar(Auto):
    """Derived class describes an object - a sports car. Base class - Auto"""
    def __init__(self, name, model, power, year):
        Auto.__init__(self, name, power, model)
        self.year = year

    def time_for_100(self):
        """Displays the time the sports car reached 100 km/h"""
        print(f"My {self.name} {self.model} {self.year} "
              f"realise accelerates to 100 km/h in 3.7 seconds")


class Bus(Transport):
    """Derived class describes the object - bus"""
    def __init__(self, name, power, persons):
        super().__init__(name, power)
        self.persons = persons

    def fuel(self):
        """Override base method "fuel" """
        print(f"Fill my {self.name} with diesel")

    def person_inside(self):
        """Information about the number of possible passengers"""
        print(f"My {self.name} can carry {self.persons} persons")


class Trolleybus(Transport):
    """Derived class describes an object - a trolleybus"""
    def __init__(self, name, power, cycle_charge):
        super().__init__(name, power)
        self.cycle_charge = cycle_charge

    def fuel(self):
        """Override base method "fuel" """
        print(f"Fill my {self.name} with electricity")

    def cost(self):
        """The cost of charging a trolleybus with batteries per day.
        Charge cycle cost * per number of charge cycles """
        cost_cycle = 40
        return cost_cycle * self.cycle_charge


class Tram(Transport):
    """Derived class describes an object - tram"""
    def fuel(self):
        """Override base method "fuel" """
        print(f"Fill my {self.name} with electricity")

    @classmethod
    def method(cls, arg):
        """Return information about your enter and class"""
        print(f'This is class - {cls.__name__}'
              f'\nAs an argument you entered: {arg} ')


class Engine:
    """Class describing the object - engine"""
    def __init__(self, type_eng, volume=1):
        self.type_eng = str(type_eng)
        self.set_volume(volume)

    def transport_tax(self):
        """Method for determining payment of tax"""
        if self.type_eng == 'бензин' and self.volume >= 3:
            return True
        elif self.type_eng == 'дизель' and self.volume >= 2.5:
            return True
        else:
            return False

    # getter method
    def get_volume(self):
        return self.volume

    # setter method
    def set_volume(self, value):
        if value > 6:
            raise ValueError('Entered volume unbelievable')
        self.volume = value


class Tax(Engine, Auto):
    """Car tax class"""
    def __init__(self, name, power, model, type_eng, volume):
        Engine.__init__(self, type_eng, volume)
        Auto.__init__(self, name, power, model)
    # Tale names of cars from file list_of models.txt
    with open('list_of_models.txt', 'r') as file_text:
        list_of_names = file_text.read().strip().split(', ')
    tax_cost = 5000

    def tax(self):
        """Information about your tax"""
        if self.name in self.list_of_names:
            if self.transport_tax():
                print(f"Pay {self.tax_cost} грн USA!!!")

            else:
                print("You don`t pay much tax))")
        else:
            print("You don`t pay tax, congrats")

    def info_tax(self):
        """Information about you"""
        self.info()
        if self.transport_tax():
            print("\nAnd i pay tax")
        else:
            print("\nAnd i don`t pay tax")


mers = Auto('Мерседес', 500, "c300")
mers.fuel()
mers.info()
bmw = Auto('BMW', 600, 'm5')
audi = Auto('Audi', 300, 'a6')
garage = bmw + mers
a = mers + audi
print(a)
bmw.yerl # example of using magic method __getattr__
print(bmw > mers)
print(audi != mers)

bogdan = Bus('27', 400, 40)
print(audi == bogdan)
Tram.method(3)


bogdan.fuel()
bogdan.start()
bogdan.person_inside()
bogdan.power_rate()

star = Trolleybus(5, 600, 6)
star.fuel()
star.name_of_transport()
star.power_rate()
print(f"Расход троллейбуса {star.name} составляет {star.cost()} грн USA")

eco = Tram("Эко", 300)
eco.fuel()

mclaren = Sportcar('Mclaren', '720s', 700, 2015)
mclaren.power_rate()
mclaren.start()
mclaren.info()
mclaren.time_for_100()
print(mclaren.name)
print(mclaren.fuel_consumption())
print(mclaren._fuel_tank)  # protected attribute

my_car = Tax('BMW', 700, 'M8', 'бензин', 5)
my_car.tax()
print(my_car.name)

my_new_car = Tax("ВАЗ", 80, "2107", 'бензин', 2)
my_new_car.tax()
my_new_car.info()

#  Private attribute
try:
    print(mers.__max_distance)
except AttributeError:
    print('__max_distance is a private attribute.')

if mclaren.steering_wheel:
    print(f"Transport {mclaren.name} with a wheel")

print(f"Information about transport: {my_car.information}")

my_new_car.set_volume(7)  # example of using getter and setter


