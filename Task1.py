class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Info: {self.year} {self.brand} {self.model}")

# Create two car objects
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2021)
car3 = Car("Ferrari", "F8", 2024)
car4 = Car("Lamborghini", "Urus", 2023)
car5 = Car("Tesla", "Cybertruck", 2025)

# Display their details
car1.display_info()
car2.display_info()
car3.display_info()
car4.display_info()
car5.display_info()