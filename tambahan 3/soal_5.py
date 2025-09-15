"""
Pertemuan 5 & 6: Functions (Membuat blok kode yang bisa dipakai ulang)
Latihan: "Refactor Konverter Suhu"
Ambil kode dari latihan Pertemuan 2 (Kalkulator Konversi Suhu) dan "refactor" (susun ulang) menjadi lebih
baik menggunakan fungsi.
1. Buat sebuah fungsi bernama konversi_suhu yang menerima dua parameter: suhu dan unit
    (string "C" atau "F").
2. Di dalam fungsi, gunakan if-elif untuk mengecek nilai unit:
    Jika unit.upper() == "C", hitung ke Fahrenheit dan return hasilnya.
    Jika unit.upper() == "F", hitung ke Celsius dan return hasilnya.
3. Di luar fungsi, panggil fungsi tersebut beberapa kali dengan nilai berbeda (misal:
    konversi_suhu(30, "C") dan konversi_suhu(86, "F")) dan cetak hasilnya.
"""

# suhu_celcius = 30
# Fahrenheit = (suhu_celcius * 9/5) + 32
# suhu_fahrenheit = Fahrenheit
# print(f"{suhu_celcius} derajat Celsius sama dengan {suhu_fahrenheit} derajat Fahrenheit.")

def konversi_suhu(suhu, unit):
    if unit.upper() == "C":
        return (suhu * 9/5) + 32
    elif unit.upper() == "F":
        return (suhu - 32) * 5/9
    else:
        return "Unit tidak valid. Gunakan 'C' atau 'F'."
print(konversi_suhu(30, "C"))
print(konversi_suhu(86, "F"))
print(konversi_suhu(100, "C"))
print(konversi_suhu(212, "F"))
print(konversi_suhu(50, "X"))