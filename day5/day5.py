# 1. Menggabungkan string
string1 = "Hello"
string2 = "world!"
gabungan = string1 + " " + string2
print(gabungan)  # Output: Hello world!

# 2. Panjang string
string = "Python"
panjang = len(string)
print("Panjang string:", panjang)  # Output: 6

# 3. Mengonversi huruf besar ke huruf kecil dan sebaliknya
kalimat = "Contoh KALIMAT"
kecil = kalimat.lower()
besar = kalimat.upper()
print("Huruf kecil:", kecil)  # Output: contoh kalimat
print("Huruf besar:", besar)  # Output: CONTOH KALIMAT

# 4. Memisahkan string menjadi daftar kata
kalimat = "Ini adalah contoh kalimat."
kata_kata = kalimat.split()
print("Daftar kata:", kata_kata)  # Output: ['Ini', 'adalah', 'contoh', 'kalimat.']

# 5. Memeriksa keberadaan substring dalam string
kalimat = "Hari ini adalah hari Minggu."
if "Minggu" in kalimat:
    print("Hari Minggu ditemukan.")
else:
    print("Hari Minggu tidak ditemukan.")

# 6. Mengganti substring dalam string
kalimat = "Saya suka programming dengan Python."
kalimat_baru = kalimat.replace("Python", "JavaScript")
print("Kalimat baru:", kalimat_baru)  # Output: Saya suka programming dengan JavaScript.
