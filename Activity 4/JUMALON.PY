class Car:
    def __init__(self, color, model, manufacturer):
        self.color = color
        self.model = model
        self.manufacturer = manufacturer

car1 = Car("Black", "HILUX", "Toyota")
car2 = Car("Gray", "SUV", "Ford")
car3 = Car("Silver", "CIVIC", "Honda")

print("Car 1:")
print("Color:", car1.color)
print("Model:", car1.model)
print("Manufacturer:", car1.manufacturer)
print()

print("Car 2:")
print("Color:", car2.color)
print("Model:", car2.model)
print("Manufacturer:", car2.manufacturer)
print()

print("Car 3:")
print("Color:", car3.color)
print("Model:", car3.model)
print("Manufacturer:", car3.manufacturer)
print()

car1.color = "Green"
car1.model = "Convertible"
car1.manufacturer = "Chevrolet"

print("Modified Car 1:")
print("Color:", car1.color)
print("Model:", car1.model)
print("Manufacturer:", car1.manufacturer)
