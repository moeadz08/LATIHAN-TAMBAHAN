"""
Pertemuan 13 & 14: List (Daftar)
Latihan: "Manajemen Daftar Tugas (To-Do List)"
Buat aplikasi to-do list interaktif sederhana.
1. Buat sebuah list kosong bernama tugas.
2. Gunakan while True loop sebagai menu utama.
3. Minta input dari pengguna: "Apa yang ingin Anda lakukan? (tambah, hapus, lihat, keluar)".
4. Gunakan if-elif-else:
    Jika "tambah", minta input tugas baru dan .append() ke list.
    Jika "lihat", cetak semua tugas dalam list dengan nomor urut.
    Jika "hapus", minta nomor tugas yang ingin dihapus, lalu .pop() dari list.
    Jika "keluar", gunakan break untuk menghentikan program.
"""

tugas = []
while True:
    aksi = input("Apa yang ingin Anda lakukan? (tambah, hapus, lihat, keluar): ").strip().lower()
    if aksi == "tambah":
        tugas_baru = input("Masukkan tugas baru: ")
        tugas.append(tugas_baru)
        print(f'Tugas "{tugas_baru}" telah ditambahkan.\n')
    elif aksi == "lihat":
        if not tugas:
            print("Daftar tugas kosong.\n")
        else:
            print("Daftar Tugas:")
            for i, tugas_item in enumerate(tugas, start=1):
                print(f"{i}. {tugas_item}")
            print() 
    elif aksi == "hapus":
        if not tugas:
            print("Daftar tugas kosong, tidak ada yang bisa dihapus.\n")
        else:
            nomor = int(input("Masukkan nomor tugas yang ingin dihapus: "))
            if 1 <= nomor <= len(tugas):
                tugas_dihapus = tugas.pop(nomor - 1)
                print(f'Tugas "{tugas_dihapus}" telah dihapus.\n')
            else:
                print("Nomor tugas tidak valid.\n") 
    elif aksi == "keluar":
        print("Terima kasih telah menggunakan aplikasi to-do list!")
        break
    else:
        print("Aksi tidak dikenal. Silakan coba lagi.\n")