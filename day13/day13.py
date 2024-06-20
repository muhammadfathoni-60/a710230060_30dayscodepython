def hitung_diskon(total_belanja):
    diskon = 0

    if total_belanja > 100000:
        diskon = 0.1  # diskon 10% jika total belanja lebih dari 100000
    elif total_belanja > 50000:
        diskon = 0.05  # diskon 5% jika total belanja lebih dari 50000
    elif total_belanja > 20000:
        diskon = 0.03  # diskon 3% jika total belanja lebih dari 20000

    return diskon

def main():
    total_belanja = float(input("Masukkan total belanja: "))

    diskon = hitung_diskon(total_belanja)
    if diskon > 0:
        jumlah_diskon = diskon * total_belanja
        total_bayar = total_belanja - jumlah_diskon
        print(f"Total belanja: Rp {total_belanja:,.2f}")
        print(f"Diskon: Rp {jumlah_diskon:,.2f}")
        print(f"Total yang harus dibayar: Rp {total_bayar:,.2f}")
    else:
        print("Total belanja: Rp {total_belanja:,.2f}")
        print("Maaf, tidak ada diskon yang berlaku untuk total belanja ini.")

if __name__ == "__main__":
    main()
