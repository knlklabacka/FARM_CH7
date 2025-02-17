from models import CarCollection, CarModel


test_car_1 = CarModel(brand="ford", make="fusion", year=2019, cm3=1600, km=110000, price=15000)
test_car_2 = CarModel(brand="nissan", make="Pathfinder", year=2025, cm3=3000, km=1000, price=48000)

car_list = CarCollection(cars=[test_car_1, test_car_2])
print(car_list.model_dump())