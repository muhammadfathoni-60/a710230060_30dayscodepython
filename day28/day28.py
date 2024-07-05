# Definisikan kelas 'Buku' untuk merepresentasikan sebuah buku
class Buku:
    def __init__(self, judul, penulis, tahun_terbit):
        self.judul = judul
        self.penulis = penulis
        self.tahun_terbit = tahun_terbit

    def __str__(self):
        return f"{self.judul} ({self.penulis}, {self.tahun_terbit})"


# Definisikan kelas 'Perpustakaan' untuk mengelola kumpulan buku
class Perpustakaan:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        self.daftar_buku.append(buku)

    def daftar_buku_perpustakaan(self):
        print(f"Daftar Buku di Perpustakaan {self.nama}:")
        for buku in self.daftar_buku:
            print(buku)


# Membuat objek buku
buku1 = Buku("Harry Potter", "J.K. Rowling", 1997)
buku2 = Buku("Lord of the Rings", "J.R.R. Tolkien", 1954)

# Membuat objek perpustakaan
perpustakaan1 = Perpustakaan("Perpustakaan Umum")
perpustakaan2 = Perpustakaan("Perpustakaan Sekolah")

# Menambahkan buku ke dalam perpustakaan
perpustakaan1.tambah_buku(buku1)
perpustakaan1.tambah_buku(buku2)
perpustakaan2.tambah_buku(buku2)

# Menampilkan daftar buku di perpustakaan
perpustakaan1.daftar_buku_perpustakaan()
perpustakaan2.daftar_buku_perpustakaan()
