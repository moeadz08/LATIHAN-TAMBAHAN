"""
Latihan 2: Pola Akumulator dengan while
Buat program untuk menghitung jumlah kuadrat dari N bilangan bulat pertama.
1. Minta pengguna memasukkan sebuah angka N.
2. Gunakan while loop untuk menghitung 1² + 2² + 3² + ... + N².
3. Cetak hasil akhirnya.
"""

input_user = int(input('masukkan angka N: '))

i = 1
total = 0

while i <= input_user:
    total += i ** 2
    i += 1

print(f"Jumlah kuadrat dari {input_user} bilangan pertama adalah: {total}")