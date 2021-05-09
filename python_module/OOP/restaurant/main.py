"""Restaurant system"""
import time
from datetime import datetime
time_order = datetime.now()


class Restaurant:
    """Base class for instruments and person"""
    __name = "Galina"


class Person(Restaurant):
    """Base class for persons in restaurant"""


class Instruments(Restaurant):
    """Base class for restaurant instruments"""
    pass


class Order(Instruments):
    """Derived class from base Instruments. Realized object Order"""
    def __init__(self, some_food):
        self.some_food = some_food

    @staticmethod
    def place_an_order(some_dishes):
        counter = {}
        print(str(time_order))
        for elem in some_dishes:
            counter[elem] = counter.get(elem, 0) + 1

        doubles = {element: count for element, count in counter.items()}
        for key, value in doubles.items():
            print(f'{key}: {value}')

    def inform_kitchen(self):
        print('There is an order!!!')
        self.place_an_order(self.some_food)


class Menu(Instruments):
    """Derived class from base class Instruments. Realized Menu"""
    @staticmethod
    def show_items():
        with open('menu.txt', 'r') as file:
            menu = file.read().strip().split(', ')
        return print('\n'.join(menu))


class Bill(Instruments):
    """Derived class from base class Instruments. Realized bill"""

    def __init__(self, some_list):
        self.some_list = some_list

    prices = {'beer': 30,
              'pizza': 40,
              'sushi': 50,
              'burger': 60,
              'cake': 70}

    def _bill_rest(self):
        """Method for calculating order value"""
        _count = 0
        for elem in self.some_list:
            for key in self.prices.keys():
                if elem == key:
                    _count += self.prices[elem]
        return _count

    def inform_client(self):
        """Bill for client"""
        all_count = self._bill_rest()
        Order.place_an_order(self.some_list)
        # print(f"To pay: {all_count}$")
        return all_count

    def inform_bookkeeping(self):
        """Bill for bookkeeper"""
        count_b = self._bill_rest()
        return count_b


class Bookkeeper(Bill, Person):
    """Realized person - Bookkeeper"""

    def __init__(self, some_list):
        Bill.__init__(self, some_list)

    _tax = 0.18  # NDS

    def generate_report(self):
        """Report from bookkeeper"""
        return print(f'The restaurant received {self._bill_rest() - int(self.inform_bookkeeping() * self._tax)}$')


class Cook(Person):
    """Derived class from base Person. Realised cooking food"""
    time_cooking: float = 20.5

    def cook_food(self, some_food):
        """Realised process cooking"""
        print("Food is cooking")

        for key in some_food:
            print(f"Cooking: {key}")
            time.sleep(2)
        print(f"Done. Your dishes were cooked - {self.time_cooking} minutes")
        return True


class Wardrobe(Person):

    _num_of_place: int = 50 # count of places for clothes

    def take_clothes(self, count):
        if self._num_of_place != 0:
            self._num_of_place -= count
            print("Good evening!")
            return True
        else:
            print("I`m sorry, we don`t have free place for clothes")
            return False


class Administrator(Menu, Person):
    """Realized person - Administrator"""

    @staticmethod
    def call_waiter():
        """Method call waiter"""
        return True

    def give_menu(self):
        print("Here is your menu, please")
        self.show_items()


class Waiter(Person):

    @staticmethod
    def take_order(some_food):
        print("Thanks for order.\nYour order: " + ' '.join(some_food))

    @staticmethod
    def give_dishes(cook_food):
        if cook_food:
            print('Bon Appetit!')
        else:
            print('Your dishes is cooking now')

    @staticmethod
    def bill(give_bill):
        print(f"That`s your bill: {give_bill}$")
        return True


class Deliver(Person):

    @staticmethod
    def drive():
        """Driver deliver order"""
        time.sleep(5)

    @staticmethod
    def give_food(dishes):
        Waiter.give_dishes(dishes)

    @staticmethod
    def bill(order_bill):
        Waiter.bill(order_bill)


galina = Restaurant
main_person = Wardrobe()
main_person.take_clothes(4)
admin = Administrator
print('This is our menu: ')
admin.show_items()
if admin.call_waiter():
    print('I will call the waiter now')
print('...Waiter taking the order...')
sam = Waiter
list_food = ['beer', 'pizza', 'beer', 'beer', 'pizza']
sam.take_order(list_food)
new_order = Order(list_food)
new_order.place_an_order(list_food)
print("...This is order for cook...")
new_order.inform_kitchen()
john = Cook()
print('...Cooking stage...')
john.cook_food(list_food)
print('...Waiter brought the food...')
sam.give_dishes(cook_food=True)
print('...Client ate...')
bill_for_order = Bill(list_food)
print('...Bill for client...')
sam.bill(bill_for_order.inform_client())
bookkeeper = Bookkeeper(list_food)
print('...Bookkeeper generate report...')
bookkeeper.generate_report()
order = 'delivery'
jack = Deliver
print('...If order must be delivered...')
if order == 'delivery':
    print('Order will be delivered')
    print('...The deliveryman delivered the order...')
    jack.drive()
    jack.give_food(list_food)
    print('...Deliveryman give bill...')
    jack.bill(bill_for_order.inform_client())












