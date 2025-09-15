"""
Latihan 5: Segitiga Angka Berulang
Buat program yang mencetak segitiga angka di mana angka di setiap baris adalah nomor baris itu sendiri.
Input: N = 5
Output yang diharapkan:
1
22
333
4444
55555
Petunjuk: Mirip dengan segitiga siku-siku, tapi alih-alih mencetak *, cetak nilai dari variabel loop luar.
Gunakan print(i, end="") untuk mencegah pindah baris.
"""

user_input = int(input("Masukkan nilai N: "))

for i in range(1, user_input+1, 1):
    for j in range(i):
        print(i, end="")
    print()