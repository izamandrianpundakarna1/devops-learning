daftar = []

while True:
    print("\n=== DAFTAR BELANJA ===")
    print("1. Tambah barang")
    print("2. Hapus barang")
    print("3. Lihat daftar")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_barang = input("masukkan nama barang yang mau ditambahkan: ") .lower() .strip()
        daftar.append(tambah_barang)
        print(f"barang {tambah_barang} sudah ditambahkan")

    elif pilihan == "2":
        hapus_barang = input("masukkan nama barang yang mau dihapus: ") .lower() .strip()
        if hapus_barang in daftar:
            daftar.remove(hapus_barang)
            print(f"barang {hapus_barang} sudah di hapus")

        else:
            print("barang tidak ada")

    elif pilihan == "3":
        if len(daftar) > 0:
            for i, barang in enumerate(daftar, start=1):
                print(f"{i}. {barang}")

        else:
            print("tidak ada barang yang tersedia")

    elif pilihan == "4":
        break

    else:
        print("pilihan tidak tersedia")