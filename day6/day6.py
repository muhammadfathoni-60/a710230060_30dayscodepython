# Meminta pengguna untuk memasukkan usia
usia = int(input("Masukkan usia Anda: "))

# Menentukan kategori usia
if usia < 0:
    print("Usia tidak valid")
elif usia < 18:
    print("Anda masih anak-anak")
elif usia < 65:
    print("Anda dewasa")
else:
    print("Anda seorang senior")
