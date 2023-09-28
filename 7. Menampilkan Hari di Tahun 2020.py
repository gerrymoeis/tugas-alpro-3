"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

print("Program Menampilkan Hari di Tahun 2020")
nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

try:
    bulan = int(input("Masukan bulan yang diinginkan dalam angka (1-12): "))
    while not 1 <= bulan <= 12:
        bulan = int(input("Tolong masukan angka bulan dalam jangkauan (1-12): "))
    
    # Tahun 2020 merupakan tahun kabisat
    if bulan == 2:
        print(f"Jumlah hari di bulan {nama_bulan[bulan-1]}: 29")
    elif bulan % 2 == 0:
        print(f"Jumlah hari di bulan {nama_bulan[bulan-1]}: 30")
    else:
        print(f"Jumlah hari di bulan {nama_bulan[bulan-1]}: 31")
except ValueError:
    print("Input tidak Valid, Hanya menerima angka")