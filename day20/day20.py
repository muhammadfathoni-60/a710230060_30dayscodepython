# Definisi class Car
class Car:
    # Constructor atau initializer
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
    
    # Method untuk menampilkan informasi mobil
    def display_info(self):
        print(f"Mobil {self.brand} {self.model} berwarna {self.color}")

# Membuat dua instance dari class Car
car1 = Car("Toyota", "Camry", "Hitam")
car2 = Car("Honda", "Civic", "Putih")

# Menampilkan informasi dari setiap instance
print("Informasi Mobil 1:")
car1.display_info()

print("\nInformasi Mobil 2:")
car2.display_info()
