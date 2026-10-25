print("Tabel perkalian")

try:
    angka = int(input("masukkan angka: "))
    for i in range(1, 11):
        print(f"{angka} x {i} = {angka * i}")
except ValueError:
    print("Error: input harus berupa angka!")