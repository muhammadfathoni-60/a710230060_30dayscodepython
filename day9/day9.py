# Dictionary untuk menyimpan data siswa
siswa = {
    '001': {'nama': 'Budi', 'kelas': '12A', 'nilai': 85},
    '002': {'nama': 'Ani', 'kelas': '12B', 'nilai': 90},
    '003': {'nama': 'Cindy', 'kelas': '12A', 'nilai': 88},
    '004': {'nama': 'David', 'kelas': '12C', 'nilai': 78},
    '005': {'nama': 'Erika', 'kelas': '12B', 'nilai': 92}
}

# Fungsi untuk menampilkan data siswa
def tampilkan_data_siswa():
    print("===== Data Siswa =====")
    for id_siswa, data in siswa.items():
        print(f"ID Siswa: {id_siswa}")
        print(f"Nama: {data['nama']}")
        print(f"Kelas: {data['kelas']}")
        print(f"Nilai: {data['nilai']}")
        print("-----------------------")

# Fungsi utama
def main():
    tampilkan_data_siswa()

if __name__ == "__main__":
    main()
