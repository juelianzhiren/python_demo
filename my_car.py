# ~ from car import Car, ElectricCar
import car

my_new_car = car.Car("audi", "24", 2016);
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23;
my_new_car.read_odometer();

my_tesla = car.ElectricCar("tesla", "roadster", 2016);
print(my_tesla.get_descriptive_name())
