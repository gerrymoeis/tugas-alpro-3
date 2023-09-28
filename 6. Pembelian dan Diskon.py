"""
    Nama: Gerry Moeis M.D.P
    Kelas: 2023E
    NIM: 23091397164
    Prodi: D4 Manajemen Informatika
"""

barang_jualan = {
    "cpu": 700_000,
    "ram": 380_000,
    "motherboard": 800_000
}
harga = [*barang_jualan.values()]

beli = True
keranjang_belanjaan = []

while beli:
    beli_barang = int(input("Mau beli apa?\n1. CPU\n2. RAM\n3. Motherboard\n"))
    keranjang_belanjaan.append(beli_barang-1)
    beli = True if input("Mau beli lagi? (Y / N): ").lower() == "y" else False

print("\n=== Kwitansi Pembelian ===")
for i, barang in enumerate(barang_jualan.keys()):
    jumlah_barang = keranjang_belanjaan.count(i)
    if jumlah_barang > 0:
        print(f"{barang}: {jumlah_barang}x")

total = sum(harga[i] for i in keranjang_belanjaan)
print(f"Total Belanjaan: Rp {total}")

if total > 1_500_000:
    total = total - total * 0.1
    print("Selamat anda dapat diskon 10%")

print(f"Harga yang harus dibayar: Rp {round(total)}")