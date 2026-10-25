'''
import random

angka_rahasia = random.randint(1, 100)
jumlah_tebakan = 0
print("Tebak angka antara 1 sampai 100!")

try:
    while True:
        jumlah_tebakan = jumlah_tebakan + 1
        angka = int(input("masukkan angka tebakanmu: "))
        if angka < angka_rahasia:
            print("angka tebakan terlalu kecil")
        elif angka > angka_rahasia:
            print("angka tebakan terlalu besar")
        else:
            print("tebakan anda benar")
            print(jumlah_tebakan)
            break
except ValueError:
    print("error: input hanya berupa angka!")
'''
import random

angka_rahasia = random.randint(1, 100)
jumlah_tebakan = 0

print("Tebak angka antara 1 sampai 100!")

while True:
    try:
        angka = int(input("masukkan angka tebakanmu: "))
    except ValueError:
        print("error: input hanya berupa angka!")
        continue   # kembali ke awal loop, minta tebakan lagi

    jumlah_tebakan += 1

    if angka < angka_rahasia:
        print("angka tebakan terlalu kecil")
    elif angka > angka_rahasia:
        print("angka tebakan terlalu besar")
    else:
        print("tebakan anda benar")
        print(jumlah_tebakan)
        break