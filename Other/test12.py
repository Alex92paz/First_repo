class Car:
    vehicle_type = "Automobile"

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Year: {self.year}, Make: {self.make}, Model: {self.model}, Vehicle Type: {self.vehicle_type}"

# Создание экземпляра класса Car
my_car = Car("Toyota", "Camry", 2022)

# Вывод атрибутов экземпляра
print(my_car.get_info())
