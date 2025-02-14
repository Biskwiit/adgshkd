class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print("-" * 20)

car1 = Car("Jeep", "Wrangler", 2021)
car2 = Car("Mercedes-Benz", "E-Class", 2022)

car1.display_info()
car2.display_info()