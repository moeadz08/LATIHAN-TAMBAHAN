"""
Latihan 24: Pola Papan Catur
Buat program yang mencetak pola papan catur berukuran N x N menggunakan karakter # dan .
Input: N = 8
Output yang diharapkan:
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
# # # #
 # # # #
Petunjuk: Di dalam nested loop, gunakan if-else. Kuncinya ada pada posisi baris (i) dan kolom
(j). Perhatikan bahwa karakter berubah jika i + j adalah genap atau ganjil. Gunakan operator
modulo (%).
"""

user_input = int(input("Masukkan ukuran papan catur: "))

for i in range(user_input):
    for j in range(user_input): # kolom
        if (i + j) % 2 == 0: # apakah genap
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
