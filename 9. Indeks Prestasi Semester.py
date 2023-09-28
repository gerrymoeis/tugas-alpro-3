"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

POIN_NILAI = {
    "A": 4, "B": 3, "C": 2,
    "D": 1, "E": 0
}

sks = [int(num) for num in input("Masukan jumlah SKS per Matkul (Pisahkan spasi): ").strip().split(" ")]
nilai = [n.upper() for n in input("Masukan nilai per Matkul (Pisahkan spasi): ").strip().split(" ")]
poin = [POIN_NILAI[n] for n in nilai]

data_ip = list(map(lambda x, y: [x, y], sks, nilai))
poin_sks = list(map(lambda x, y: [x, y], sks, poin))

def hitung_ip_semester(sks, poin_sks):
    total_sks = sum(sks)
    total_poin = sum(x*y for [x, y] in poin_sks)
    return total_poin / total_sks

print("=== Indeks Prestasi Semester ===")
for i, [x, y] in enumerate(data_ip):
    print(f"{i+1}. SKS: {x}, Nilai: {y}")
print(f"IP: {hitung_ip_semester(sks, poin_sks)}")