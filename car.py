class Car():
    '''一次模拟汽车的简单尝试'''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self, mileage):
        self.odometer_reading = mileage
        print('this car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('can not roll back on odometers.')


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)


my_electri_car = ElectricCar(make='audi', model='A8L', year=2019)
print(my_electri_car.get_descriptive_name())
my_electri_car.read_odometer(24)
