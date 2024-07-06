class Kalkulator:
    def __init__(self):
        pass
    
    def tambah(self, x, y):
        return x + y
    
    def kurang(self, x, y):
        return x - y
    
    def kali(self, x, y):
        return x * y
    
    def bagi(self, x, y):
        if y == 0:
            return "Error: Pembagian dengan nol tidak diperbolehkan"
        else:
            return x / y

# Contoh penggunaan:
def main():
    calc = Kalkulator()
    
    print("Hasil penjumlahan:", calc.tambah(5, 3))
    print("Hasil pengurangan:", calc.kurang(5, 3))
    print("Hasil perkalian:", calc.kali(5, 3))
    print("Hasil pembagian:", calc.bagi(5, 3))
    print("Hasil pembagian oleh nol:", calc.bagi(5, 0))

if __name__ == "__main__":
    main()
