"""
Latihan 8: Membangun String dengan Pola
Buat program yang meminta input sebuah kata dari pengguna. Program kemudian harus membangun
sebuah string baru berbentuk "piramida" dari kata tersebut.
• Gunakan for loop dengan range(len(kata)).
• Gunakan slicing kata[:i+1] untuk mendapatkan potongan kata di setiap iterasi.
"""

kata = input("Masukkan sebuah kata: ")

for x in range(len(kata)):
    print(kata[:x+1]) # ngambil dari index paling awal sampe setelahnya(tapi nambah terus 1 persatu)