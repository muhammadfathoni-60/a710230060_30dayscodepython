# Mendefinisikan sebuah list
buah = ["apel", "pisang", "jeruk", "mangga", "semangka"]

# Menampilkan seluruh elemen dalam list
print("Buah-buahan:")
for item in buah:
    print(item)

# Menampilkan panjang list
print("\nJumlah buah dalam list:", len(buah))

# Menampilkan elemen pertama dalam list
print("\nBuah pertama dalam list:", buah[0])

# Menampilkan elemen terakhir dalam list
print("Buah terakhir dalam list:", buah[-1])

# Menambahkan elemen baru ke dalam list
buah.append("nanas")
print("\nBuah setelah menambahkan 'nanas':", buah)

# Menghapus elemen dari list
buah.remove("apel")
print("Buah setelah menghapus 'apel':", buah)
