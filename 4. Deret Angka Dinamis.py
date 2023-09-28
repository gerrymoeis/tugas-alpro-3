"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

angka_user = int(input("Masukan angka yang lebih dari 0: "))
while angka_user <= 0:
    angka_user = int(input("Tolong masukan angka yang lebih dari 0: "))

for angka in range(angka_user):
    print(" ".join(str(num) for num in [*range(angka_user-angka, 0, -1)]))