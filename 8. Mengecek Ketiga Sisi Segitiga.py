"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

try:
    sisi_segitiga = [int(num) for num in input("Masukan 3 sisi segitiga (Pisahkan spasi): ").strip().split(" ")]
    while len(sisi_segitiga) != 3:
        sisi_segitiga = [int(num) for num in input("Segitiga sisinya 3 ya kawan (Pisahkan spasi): ").strip().split(" ")]
    
    count = 0
    for sisi in sorted(sisi_segitiga):
        if sorted(sisi_segitiga)[1] == sisi:
            count += 1
    
    print(f"{count if count > 1 else 'Tidak ada'} sisi yang sama")
except ValueError:
    print("Tolong hanya masukan angka bulat (tanpa titik atau koma)")

# try:
#     sisi_segitiga = [int(num) for num in input("Masukan 3 sisi segitiga (Pisahkan spasi): ").strip().split(" ")]
#     while len(sisi_segitiga) != 3:
#         sisi_segitiga = [int(num) for num in input("Segitiga sisinya cuma 3 ya kawan (Pisahkan spasi): ").strip().split(" ")]
#     while sisi_segitiga.count(0) > 0:
#         sisi_segitiga = [int(num) for num in input("Sisi tidak boleh bernilai kurang dari 1 (Pisahkan spasi): ").strip().split(" ")]
    
#     jumlah_sisi_sama = max(sisi_segitiga.count(num) for num in sisi_segitiga)
#     print(f"{jumlah_sisi_sama if jumlah_sisi_sama > 1 else 'Tidak ada'} sisi yang sama")
# except ValueError:
#     print("Tolong hanya masukan angka bulat (tanpa titik atau koma)")