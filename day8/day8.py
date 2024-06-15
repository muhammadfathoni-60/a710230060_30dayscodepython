# Program untuk menghitung jumlah bilangan genap dari 1 hingga 10
# dan mencetak hasilnya

# Inisialisasi variabel untuk menyimpan jumlah bilangan genap
jumlah_genap = 0

# Perulangan for untuk mengiterasi dari 1 sampai 10
for num in range(1, 11):
    # Cek apakah bilangan tersebut genap atau tidak
    if num % 2 == 0:
        # Jika genap, tambahkan ke variabel jumlah_genap
        jumlah_genap += num

# Cetak hasil jumlah bilangan genap
print("Jumlah bilangan genap dari 1 sampai 10 adalah:", jumlah_genap)
