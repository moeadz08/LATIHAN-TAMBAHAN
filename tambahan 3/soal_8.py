"""
Pertemuan 9 & 10: Bekerja dengan String
Latihan: "Ekstraktor Data Diri"
Diberikan sebuah string data yang formatnya tidak beraturan: data = "NAMA:Budi
Santoso|UMUR:25|KOTA:Jakarta".
Tulis program yang mengekstrak setiap informasi dari string tersebut dan mencetaknya dengan rapi.
1. Gunakan .split('|') untuk memecah data menjadi beberapa bagian.
2. Gunakan for loop untuk setiap bagian.
3. Di dalam loop, gunakan .split(':') lagi untuk memisahkan label dan nilainya.
4. Cetak hasilnya. Output yang diharapkan:
    NAMA = Budi Santoso
    UMUR = 25
    KOTA = Jakarta
"""

data = "NAMA:Budi Santoso|UMUR:25|KOTA:Jakarta"
parts = data.split('|') # Memecah string menjadi bagian-bagian berdasarkan '|'
for part in parts: # Loop untuk setiap bagian dari data
    label, value = part.split(':') # Memisahkan label dan nilai dengan split ':'
    print(f"{label} = {value}")