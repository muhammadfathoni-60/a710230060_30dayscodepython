def is_prime(num):
    """Fungsi untuk mengecek apakah suatu bilangan prima."""
    if num <= 1:
        return False
    if num == 2:  # 2 adalah bilangan prima
        return True
    if num % 2 == 0:  # bilangan genap selain 2 bukan prima
        return False
    
    # cek bilangan ganjil lainnya
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def cari_bilangan_prima(start, end):
    """Fungsi untuk mencari bilangan prima dalam rentang tertentu."""
    prime_numbers = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

# Contoh penggunaan:
start = 1
end = 50
primes = cari_bilangan_prima(start, end)
print(f"Bilangan prima antara {start} dan {end} adalah: {primes}")
