"""
Latihan 21: Persegi Bolong (Hollow Square)
Buat program yang mencetak bingkai persegi berukuran N x N.
Input: N = 5
Output yang diharapkan:
*****
*   *
*   *
*   *
*****
Petunjuk: Di dalam nested loop, gunakan if-else. Cetak bintang (*) hanya jika kamu berada di
baris pertama (i == 0), baris terakhir (i == N-1), kolom pertama (j == 0), atau kolom terakhir (j
== N-1). Jika tidak, cetak spasi.
"""

user_input = int(input("Masukkan ukuran hollow square: "))

for i in range(user_input):
    for x in range(user_input):        # loop kolom
        if i == 0 or i == user_input-1 or x == 0 or x == user_input-1:
            print("*", end="")   # bintang di samping
        else:
            print(" ", end="")   # biar tengah kosong
    print()