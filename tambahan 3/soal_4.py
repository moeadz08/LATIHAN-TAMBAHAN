"""
Pertemuan 4: Logika & Kondisi (if, else, elif, operator logika)
Latihan: "Kalkulator Diskon Wahana Bermain"
Buat program untuk menentukan harga tiket masuk wahana bermain berdasarkan usia dan hari kunjungan.
1. Minta input usia (integer) dan hari_kunjungan (string, misal: "senin", "sabtu").
2. Harga normal tiket adalah Rp 75.000.
3. Terapkan aturan diskon berikut menggunakan if-elif-else:
    Jika usia di bawah 5 tahun atau di atas 60 tahun, diskon 50%.
    Jika bukan keduanya, tetapi berkunjung di hari kerja ("senin" sampai "jumat"), diskon 20%.
    Selain itu (usia normal di akhir pekan), tidak ada diskon.
4. Cetak harga tiket akhir yang harus dibayar.
"""

usia = int(input("Masukkan usia Anda: "))
hari_kunjungan = input("Masukkan hari kunjungan (misal: senin): ").lower()
harga_tiket = 75000 # Harga normal tiket dalam rupiah

if usia < 5 or usia > 60:
    diskon = 0.5 # Diskon 50%
elif hari_kunjungan in ["senin", "selasa", "rabu", "kamis", "jumat"]:
    diskon = 0.2 # Diskon 20%
else:
    diskon = 0.0 # Tidak ada diskon

harga_akhir = harga_tiket * (1 - diskon)
print(f"Harga tiket akhir yang harus dibayar: Rp {harga_akhir:,.0f}")