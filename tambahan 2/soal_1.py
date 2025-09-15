"""
Latihan 1: Persegi Bintang Solid
Buat program yang mencetak persegi solid yang terdiri dari bintang (*) berukuran N x N.
Input: N = 5
Output yang diharapkan:
*****
*****
*****
*****
Petunjuk: Kamu akan butuh dua for loop yang bersarang (nested). Loop luar untuk baris, loop
dalam untuk kolom.
"""

user_input = int(input("Masukkan nilai N: "))

for i in range(1, user_input+1, 1): # dari 1 sampai  user_input
    for j in range(user_input):
        print("*", end="")
    print()