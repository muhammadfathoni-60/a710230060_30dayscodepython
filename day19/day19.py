# Definisikan sebuah class bernama Person
class Person:
    # Constructor / initializer untuk class Person
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method untuk menampilkan informasi tentang person
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Membuat instance dari class Person
person1 = Person("John", 25)

# Memanggil method display_info untuk menampilkan informasi person
person1.display_info()
