"""
Latihan 4: Piramida Bintang
Buat program yang mencetak piramida (segitiga sama kaki) setinggi N.
Input: N = 5
Output yang diharapkan:
    *
   ***
  *****
 *******
*********
Petunjuk: Ini adalah tantangan pertama yang membutuhkan logika spasi. Di setiap baris, kamu perlu
mencetak sejumlah spasi, diikuti oleh sejumlah bintang. Coba temukan rumus untuk jumlah spasi dan
jumlah bintang untuk setiap baris i. Jumlah spasi biasanya N - 1 - i dan jumlah bintang 2 * i + 1.
"""

user_input = int(input("Masukkan tinggi piramida: "))

i = 1
while i <= user_input:
    print(" " * (user_input - i) + "*" * (2 * i - 1))
    i += 1