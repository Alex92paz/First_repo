class Car:
    vehicle_type = "Automobile"  # Атрибут класса

    def __init__(self, make, model, year):
        # Атрибуты экземпляра
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        # Возвращает строку с информацией об автомобиле
        return f"Year: {self.year}, Make: {self.make}, Model: {self.model}, Vehicle Type: {self.vehicle_type}"

# Создание экземпляров класса Car
car_ford = Car("Ford", "Mustang", 2022)
car_toyota = Car("Toyota", "Camry", 2022)

# Вывод атрибутов экземпляров
print(car_ford.get_info())  # Вывод информации о первом автомобиле
print(car_toyota.get_info())  # Вывод информации о втором автомобиле
