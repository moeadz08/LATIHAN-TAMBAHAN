"""
Latihan 22: Diamond Bintang
Buat program yang mencetak bentuk berlian (diamond) setinggi N (N harus ganjil).
Input: N = 5
Output yang diharapkan:
  *
 ***
*****
 ***
  *
Petunjuk: Pecah masalah ini menjadi dua bagian. Buat satu for loop besar untuk mencetak piramida
bagian atas, lalu buat for loop besar kedua untuk mencetak piramida terbalik di bagian bawah.
"""

sisi = int(input("Masukan panjang sisi :"))
panjang = 1 # bintang yang dicetak skarang
count = 1   # ngatur kapan berenti naik dan mulai turun
while True:
    if (count < sisi): # kalo masih belum sepanjang sisi
        print((panjang*"*").center(sisi+1)) # gamake spasi
        count += 2
        panjang += 2
    else:
        print((panjang*"*").center(sisi+1)) # udah nyampe klimaks, turun
        panjang -= 2
        count-=2
        
    if panjang < 1:
        break