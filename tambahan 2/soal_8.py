"""
Latihan 23: Segitiga Huruf Alfabet
Buat program yang mencetak segitiga yang berisi urutan huruf alfabet.
Input: N = 5
Output yang diharapkan:
A
AB
ABC
ABCD
ABCDE
Petunjuk: Kamu perlu mengonversi angka ke karakter. Gunakan fungsi chr() dan ord(). ord('A')
akan memberimu nilai ASCII untuk 'A'. Kamu bisa menambahkan nilai loop j ke ord('A') lalu
mengubahnya kembali ke karakter dengan chr().
"""

user_input = int(input("Masukkan tinggi segitiga: "))

for i in range(user_input):  # baris
    for j in range(i+1):  # huruf per baris
        print(chr(ord('A') + j), end="")
    print()