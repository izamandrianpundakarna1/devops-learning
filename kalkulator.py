try:
    angka1 = int(input("masukkan angka: "))
    operasi = input("operasi: ")
    angka2 = int(input("masukkan angka: "))

    if operasi == "+":
        hasil = angka1 + angka2
    elif operasi == "-":
        hasil = angka1 - angka2
    elif operasi == "*":
        hasil = angka1 * angka2
    elif operasi == "/":
        hasil = angka1 / angka2
    elif operasi == "%":
        hasil = angka1 % angka2
    elif operasi == "**":
        hasil = angka1 ** angka2
    elif operasi == "//":
        hasil = angka1 // angka2
    else:
        print("Operasi tidak dikenali!")
        hasil = None

    if hasil is not None:
        print("Hasil:", hasil)

except ZeroDivisionError:
    print("Error: tidak bisa membagi dengan nol!")
except ValueError:
    print("Error: input harus berupa angka!")