"""
Latihan 1: Validasi Input dengan while
Buat program yang meminta pengguna memasukkan umur mereka. Program harus terus meminta input
selama pengguna memasukkan nilai yang tidak valid (bukan angka atau angka di luar rentang wajar, misal <
0 atau > 100). Gunakan while True loop, try-except untuk menangani ValueError, dan if untuk
mengecek rentang. Jika input sudah valid, cetak umur tersebut dan hentikan loop dengan break.
"""

while True:
    try:
        user_input = int(input("masukkan umur anda: "))

        if user_input < 10:
            print("Terlalu muda!")
        elif user_input > 50:
            print('Terlalu tua!')
        else:
            print(f'Umur anda adalah: {user_input}')
            print('Terimakasih')
            break
    except ValueError:
        print('plis masukkin angka saja!')