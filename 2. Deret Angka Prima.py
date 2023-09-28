"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

jumlah_angka_prima = int(input("Masukan jumlah angka prima yang ingin ditampilkan: "))
list_angka_prima = []

def cek_angka_prima(angka, basis=2):
    if angka <= 1: return False
    if angka == basis: return True
    if angka % basis == 0: return False

    basis += 1
    return cek_angka_prima(angka, basis)

angka = 0
while len(list_angka_prima) < jumlah_angka_prima:
    if cek_angka_prima(angka):
        list_angka_prima.append(angka)
    angka += 1

print(f"Bilangan Prima: {list_angka_prima}")
print(f"Total Bilangan Prima: {len(list_angka_prima)}")

# Versi One Line
primes = [i for i in range(2, jumlah_angka_prima*10) if 0 not in [i % n for n in range(2, i)]][:jumlah_angka_prima]
print(f"Bilangan Prima: {primes}")
print(f"Total Bilangan Prima: {len(primes)}")