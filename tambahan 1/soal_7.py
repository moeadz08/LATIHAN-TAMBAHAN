"""
Latihan 7: Permainan "FizzBuzz"
Ini adalah soal wawancara coding klasik. Tulis program yang menggunakan for loop untuk mencetak angka
dari 1 hingga 100, dengan aturan:
• Jika angka tersebut kelipatan 3, cetak "Fizz".
• Jika angka tersebut kelipatan 5, cetak "Buzz".
• Jika angka tersebut kelipatan 3 dan 5, cetak "FizzBuzz".
• Jika tidak memenuhi ketiganya, cetak angka itu sendiri.
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:   # kelipatan 3 dan 5
        print("FizzBuzz")
    elif i % 3 == 0:                # kelipatan 3
        print("Fizz")
    elif i % 5 == 0:                # kelipatan 5
        print("Buzz")
    else:                           # selain kelipatan 3 atau 5
        print(i)