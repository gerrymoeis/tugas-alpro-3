"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

angka_user = int(input("Masukan angka positif: "))

while angka_user < 0:
    angka_user = int(input("Hanya menerima angka positif: "))

def cek_angka_prima(angka, basis=2):
    if angka <= 1: return False
    if angka == basis: return True
    if angka % basis == 0: return False

    basis += 1
    return cek_angka_prima(angka, basis)

def angka_prima_terdekat(angka):
    angka -= 1

    if angka <= 1:
        return f"Tidak ada bilangan prima yang lebih kecil dari {angka_user}"
    if cek_angka_prima(angka):
        return f"Bilangan prima yang terdekat dan lebih kecil dari {angka_user} adalah {angka}"

    return angka_prima_terdekat(angka)

print(angka_prima_terdekat(angka_user))

# Versi One Line
primes = [i for i in range(2, angka_user) if 0 not in [i % n for n in range(2, i)]]
print(f"Tidak ada bilangan prima yang lebih kecil dari {angka_user}" if len(primes) <= 0 else f"Bilangan prima yang terdekat dan lebih kecil dari {angka_user} adalah {primes[-1]}")