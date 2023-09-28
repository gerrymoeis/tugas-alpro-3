"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

[tinggi, lebar] = [int(num) for num in input("Masukan Tinggi dan Lebar yang di inginkan (Pisahkan spasi): ").strip().split(" ")]

if (tinggi * lebar <= 0): print("Input angka tidak valid")
else:
    for baris in range(tinggi):
        print(" ".join(str(num) for num in [*range(lebar * baris + 1, lebar * (baris + 1) + 1)]))

# for baris in range(1, tinggi+1):
#     print(" ".join(str(num) for num in [*range(baris, (lebar+1) * baris)]))

# for angka in range(1, tinggi * lebar):
#     print(angka)