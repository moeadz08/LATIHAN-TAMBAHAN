"""
Latihan 3: Segitiga Siku-Siku Terbalik
Buat program yang mencetak segitiga siku-siku terbalik setinggi N.
Input: N = 5
Output yang diharapkan:
*****
****
***
**
*
Petunjuk: Gunakan range() dengan langkah mundur (misalnya range(N, 0, -1)).
"""

user_input = int(input("Masukkan nilai N: "))

for i in range(user_input, 0, -1):
    for j in range(i):
        print("*", end="")
    print()