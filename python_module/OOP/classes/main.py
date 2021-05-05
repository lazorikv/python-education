"""Реализация класса Transport"""


class Transport:
    """Родительский класс Transport имеет 2 атрибута name(название) и power(мощность двигателя)"""
    steering_wheel = True

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def name_of_transport(self):
        """Метод выводит название транспорта"""
        print(f"У меня - {self.name}")

    def fuel(self):
        """Вид заправляемого топлива"""
        print(f"Заправьте мой {self.name} топливом")

    def power_rate(self):
        """Метод выводит количество лошадиных сил двигателся"""
        print(f"Мой {self.name} имеет {self.power} сил")

    @staticmethod
    def start():
        """Статический метод. метод реализует гипотетический запуск двигателя"""
        print("Транспорт завелся")


class Auto(Transport):
    """Дочерний класс описывает объект - автомобиль"""
    def __init__(self, name, power, model):
        Transport.__init__(self, name, power)
        self.model = model

    def info(self):
        """Выводит информацию о автомобиле"""
        print(f"У меня {self.name} {self.name}, которая имеет {self.power} сил")

    def fuel(self):
        print(f"Заправьте мой {self.name} бензином")


class Sportcar(Auto):
    """Дочерний класс описывает объект - спорткар. Родительский класс - Auto"""
    def __init__(self, name, model, power, year):
        Auto.__init__(self, name, power, model)
        self.year = year

    def time_for_100(self):
        """Выводит время достижения спорткаром скорости 100 км/ч"""
        print(f"Мой {self.name} {self.model} {self.year} "
              f"года до 100 км/ч разгоняется за 3.7 секунд")


class Bus(Transport):
    """Дочерний класс описывает объект - автобус"""
    def __init__(self, name, power, persons):
        super().__init__(name, power)
        self.persons = persons

    def fuel(self):
        """Переопределние родительского метода fuel"""
        print(f"Заправьте мой {self.name} дизелем")

    def person_inside(self):
        """Информация о кол-ве возможных пассажиров"""
        print(f"Моя {self.name} может перевести {self.persons} человек")


class Trolleybus(Transport):
    """Дочерний класс описывает объект - тролейбус"""
    def __init__(self, name, power, cycle_charge):
        super().__init__(name, power)
        self.cycle_charge = cycle_charge

    def fuel(self):
        """Переопределние родительского метода fuel"""
        print(f"Заправьте мой {self.name} электричеством")

    def cost(self):
        """Стоимость заряда троллейбуса с аккумуляторами в день.
        Стоимость цикла заряда * на кол-во циклов заряда"""
        cost_cycle = 40
        return cost_cycle * self.cycle_charge


class Tram(Transport):
    """Дочерний класс описывает объект - автомобиль"""
    def fuel(self):
        """Переопределние родительского метода fuel"""
        print(f"Заправьте мой {self.name} электричеством")


mers = Auto('Мерседес', 500, "c300")
mers.fuel()
mers.info()

bogdan = Bus('27', 400, 40)
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

if mclaren.steering_wheel:
    print(f"Транспорт {mclaren.name} с рулем")
