try:
    angka = int(input("Masukkan angka: "))
    
    # Cek genap/ganjil
    if angka % 2 == 0:
        print(f"Bilangan {angka} adalah: genap")
    else:
        print(f"Bilangan {angka} adalah: ganjil")
    
    # Cek prima
    is_prima = True
    
    for i in range(2, angka):
        if angka % i == 0:
            is_prima = False
            break
    
    if is_prima and angka > 1:
        print(f"Bilangan {angka} adalah: prima")
    else:
        print(f"Bilangan {angka} bukan prima")

except ValueError:
    print("Error: input harus berupa angka!")