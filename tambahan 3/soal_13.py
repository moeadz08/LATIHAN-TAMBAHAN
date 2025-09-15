"""
Pertemuan 19 & 20: Regular Expression (Regex)
Latihan: "Validasi dan Ekstraksi Info dari Log"
Diberikan beberapa baris log:```
"ERRORï2025-08-04ïGagal koneksi ke database."
"INFOï2025-08-04ïUser 'budi' berhasil login."
"WARNINGï2025-08-05ïDisk hampir penuh."
Tulis program yang:
1. Membuat sebuah pola Regex dengan **grup `()`** untuk menangkap tiga
    bagian: Level Log (ERROR/INFO/WARNING), Tanggal, dan Pesan.
2. Menggunakan `for` loop untuk setiap baris log.
3. Di dalam loop, gunakan `re.search()` untuk mencocokkan pola.
4. Jika cocok, ekstrak dan cetak ketiga bagian tersebut dengan rapi.
"""

"ERRORï2025-08-04ïGagal koneksi ke database."
"INFOï2025-08-04ïUser 'budi' berhasil login."
"WARNINGï2025-08-05ïDisk hampir penuh."

import re
log_data = [
    "ERRORï2025-08-04ïGagal koneksi ke database.",
    "INFOï2025-08-04ïUser 'budi' berhasil login.",
    "WARNINGï2025-08-05ïDisk hampir penuh."
]
pola = r"(ERROR|INFO|WARNING)ï(\d{4}-\d{2}-\d{2})ï(.+)"
for log in log_data:
    hasil = re.search(pola, log)
    if hasil:
        level_log = hasil.group(1)
        tanggal = hasil.group(2)
        pesan = hasil.group(3)
        print(f"Level Log: {level_log}, Tanggal: {tanggal}, Pesan: {pesan}")
    else:
        print("Format log tidak valid:", log)
# ERROR|INFO|WARNING -> grup 1
# \d{4}-\d{2}-\d{2} -> grup 2
# .+ -> grup 3
# () -> grup
# [] -> karakter set
# {} -> quantifier
# . -> sembarang karakter kecuali newline
# \d -> digit [0-9]
# \w -> word character [a-zA-Z0-9_]
# \s -> whitespace [ \t\n\r\f\v]
# ^ -> awal string
# $ -> akhir string
# | -> atau
# \ -> escape character
# re.search() -> mencari pola di string
# re.match() -> mencocokkan pola di awal string
# re.findall() -> mencari semua pola di string dan mengembalikan list
# re.sub() -> mengganti pola di string dengan string lain
# re.compile() -> mengkompilasi pola menjadi objek regex
# import re -> mengimpor modul regex