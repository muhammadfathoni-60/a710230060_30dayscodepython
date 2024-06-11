class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

# Gunakan kelas Person untuk membuat objek, lalu jalankan metode printname:
x = Person("Muhammad", "Fathoni")
x.printname()
