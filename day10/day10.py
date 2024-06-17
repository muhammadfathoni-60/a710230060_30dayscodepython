# Definisikan sebuah tuple
tuple_data = (1, 2, 3, 4, 5)

# Mengakses elemen-elemen tuple dan mencetaknya satu per satu
print("Isi dari tuple_data:")
for item in tuple_data:
    print(item)

# Menghitung jumlah elemen dalam tuple
jumlah_elemen = len(tuple_data)
print(f"Jumlah elemen dalam tuple_data adalah: {jumlah_elemen}")

# Menambahkan dua tuple
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
tuple_c = tuple_a + tuple_b
print("Hasil penambahan tuple_a dan tuple_b:")
print(tuple_c)

# Mengakses elemen tuple menggunakan indeks
elemen_pertama = tuple_data[0]
elemen_terakhir = tuple_data[-1]
print(f"Elemen pertama: {elemen_pertama}, elemen terakhir: {elemen_terakhir}")

# Menemukan nilai maksimum dan minimum dalam tuple
tuple_angka = (10, 20, 5, 15, 25)
nilai_maksimum = max(tuple_angka)
nilai_minimum = min(tuple_angka)
print(f"Nilai maksimum: {nilai_maksimum}, nilai minimum: {nilai_minimum}")
