"""
Pertemuan 3: Variabel dan Tipe Data Dasar (str, int, float)
Latihan: "Kalkulator Sederhana Biaya Perjalanan"
Buat program interaktif yang menghitung perkiraan biaya bensin untuk sebuah perjalanan.
1. Minta pengguna memasukkan tiga hal:
    Jarak perjalanan dalam kilometer (bisa desimal).
    Konsumsi bahan bakar mobil (km per liter, bisa desimal).
    Harga bensin per liter.
2. Lakukan konversi tipe data yang sesuai untuk setiap input.
3. Hitung berapa liter bensin yang dibutuhkan (jarak / konsumsi).
4. Hitung total biaya perjalanan (liter_bensin * harga_per_liter).
5. Cetak hasilnya dengan format yang jelas, contoh: "Untuk perjalanan 150.5 km, Anda
membutuhkan 12.54 liter bensin dengan total biaya Rp 188125.0"
"""

jarakTempuh = float(input("Jarak tempuh (km): "))
bensinLiter = float(input("Liter bensin yang dipake: "))
hargaBensin = float(input("Harga bensin per liter: "))

kmPerLiter = jarakTempuh / bensinLiter
biayaJalan = bensinLiter * hargaBensin
print(f"Untuk perjalanan {jarakTempuh} km, Anda membutuhkan {kmPerLiter} liter bensin dengan total biaya Rp {biayaJalan:,.2f}")
