"""
Latihan 10: Piramida Angka Palindromik
Buat program yang mencetak piramida angka yang simetris.
Input: N = 5
Output yang diharapkan:
    1
   121
  12321
 1234321
123454321
Petunjuk: Ini adalah yang paling menantang. Setiap baris terdiri dari tiga bagian: spasi, urutan angka
naik, dan urutan angka turun. Kamu mungkin perlu tiga loop terpisah di dalam loop baris utama: satu
untuk spasi, satu untuk angka naik, dan satu untuk angka turun.
"""

user_input = int(input("Masukkan tinggi piramuda: "))

for i in range(1, user_input+1):
    print(" " * (user_input - i), end="") # spasi
    
    for j in range(1, i+1): # angka naik 
        print(j, end="")
    
    for j in range(i-1, 0, -1): # angka turun
        print(j, end="")
    
    print()