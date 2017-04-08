
from car import Car, ElectricCar, PetrolCar, DieselCar, HibridCar, Dealership

dealership = Dealership()
dealership.create_current_stock()
proceed = 'y'
while proceed == 'y':
    dealership.process_rental()
    proceed = raw_input('continue? Y/N')

quit()

car3 = ElectricCar()
car3.setColour('white')
car3.setMileage(500)
car3.setNumberFuelCells(2)
print 'Colour ' + car3.getColour()
print 'Number of fuel cells ' + str(car3.getNumberFuelCells())



red_car = Car()
print 'Colour ' + red_car.getColour()
print 'Mileage ' + str(red_car.getMileage())
print 'Make ' + red_car.getMake()

red_car.setMake('Ferrari')

print 'Make ' + red_car.getMake() 

print('Getting a paint job - the new colour is ' + red_car.paint('red'))

print 'Colour ' + red_car.getColour()

print ('Car moved' + str(red_car.move(15)) + 'kms')
print 'Mileage ' + str(red_car.getMileage())

print 'Engine Size ' + red_car.engineSize
red_car.engineSize = '3.9'
print 'Engine Size ' + red_car.engineSize
