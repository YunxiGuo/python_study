from 类操作.battery import Battery
from 类操作.car import Car


class ElectricCar(Car):
    """电动汽车"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_descriptive_name(self):
        """重写父类方法"""

        print('这是电动汽车子类重写父类的方法')


my_electric_car = ElectricCar(make='audi', model='A8L', year=2020)
my_electric_car.get_descriptive_name()
my_electric_car.battery.describe_battery()
