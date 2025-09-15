"""
Pertemuan 7 & 8: Iterasi / Loops
Latihan: "Tebak Angka (dengan Batasan Percobaan)"
Buat game tebak angka yang lebih menantang.
1. Buat variabel angka_rahasia = 42 dan maks_percobaan = 5.
2. Gunakan for loop dengan range(maks_percobaan) untuk memberi pengguna kesempatan
    terbatas.
3. Di setiap iterasi, minta pengguna menebak angka.
4. Beri petunjuk apakah tebakan mereka "Terlalu tinggi" atau "Terlalu rendah".
5. Jika tebakan benar, cetak pesan kemenangan dan keluar dari loop dengan break.
6. Gunakan else setelah for loop. Jika loop selesai tanpa break (artinya semua percobaan habis),
cetak pesan "Game over! Anda kehabisan percobaan."
"""

angka_rahasia = 42
maks_percobaan = 5
for percobaan in range(maks_percobaan):
    tebakan = int(input("Tebak angkanya (antara 1-100): "))
    print(f"Sisa percobaan: {maks_percobaan - percobaan - 1}")
    if tebakan < angka_rahasia:
        print("Terlalu rendah!")
    elif tebakan > angka_rahasia:
        print("Terlalu tinggi!")
    else:
        print("Selamat! Tebakan Anda benar.")
        break
    print()  # Baris kosong untuk pemisah
else:
    print("Game over! Anda kehabisan percobaan.")