"""
Latihan 3: Iterasi String dengan continue
Buat program yang meminta pengguna memasukkan sebuah kalimat. Program akan mencetak ulang kalimat
tersebut huruf per huruf, tetapi semua huruf vokal (a, i, u, e, o, baik besar maupun kecil) akan
dilewati (tidak dicetak).
• Gunakan for loop untuk mengiterasi setiap huruf dalam kalimat.
• Gunakan if dan continue untuk melewati huruf vokal.
"""

kalimat = input('masukkan sebuah kalimat: ')

vowel = "aiueo"

for huruf in kalimat:
    if huruf.lower() in vowel:
        continue   # nyekip vowel
    print(huruf, end="")  # nge-print tanpa newline