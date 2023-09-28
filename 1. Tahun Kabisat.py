"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

tahun = int(input("Masukan tahun antara 1900-2020: "))

while not 1900 <= tahun <= 2020:
    tahun = int(input("Tolong masukan tahun antara 1900-2020 saja: "))

if tahun % 4 == 0:
    print("Tahun Kabisat")
else:
    print("Bukan Tahun Kabisat")


# Versi One Line
tahun_kabisat = lambda tahun: not bool((tahun % 4) if (tahun % 100) else (tahun % 400))
print("Tahun Kabisat" if tahun_kabisat(tahun) else "Bukan Tahun Kabisat")