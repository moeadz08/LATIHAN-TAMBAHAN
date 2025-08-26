"""
Latihan 4: Mencari Bilangan Prima Pertama
Buat program untuk menemukan dan mencetak 5 bilangan prima pertama setelah angka 1. Bilangan prima
adalah bilangan yang hanya bisa dibagi oleh 1 dan dirinya sendiri.
• Gunakan while loop luar untuk memastikan kamu sudah menemukan 5 bilangan prima.
• Gunakan for loop di dalamnya untuk mengecek apakah sebuah angka bisa dibagi oleh angka lain
  selain 1 dan dirinya sendiri.
• Kamu akan butuh sebuah "flag" (variabel boolean) untuk menandai apakah sebuah angka prima atau
  tidak
"""

jumlah_bilangan = 0  
angka = 2          # mulainya

while jumlah_bilangan < 5:

    prima = True  

    # kalo bukan prima, skipp
    for i in range(2, angka):
        if angka % i == 0:
            prima = False
            break

    # kalau prima, print
    if prima:
        print(angka)
        jumlah_bilangan += 1

    angka += 1
