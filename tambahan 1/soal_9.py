"""
Latihan 9: Menghitung Mundur dengan Melewati Angka
Gunakan for loop dengan range() untuk menghitung mundur dari 20 ke 1. Tapi, jika angka tersebut
adalah kelipatan 4, jangan cetak angka tersebut (gunakan continue).
"""

for i in range(20, 0, -1):  
    if i % 4 == 0: # kalo kelipatan 4
        continue   # skip
    print(i)