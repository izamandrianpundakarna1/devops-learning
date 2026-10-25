import datetime
import os
import shutil

while True:
    jalan = input("masukkan path yang ingin diback-up: ")

    p = jalan
    r = os.path.basename(p)
    tanggal = str(datetime.date.today())
    nama_backup = f"{r}_backup_{tanggal}"

    if os.path.isdir(jalan):
        print(f"path {jalan} adalah folder")
    else:
        print(f"path {jalan} bukan folder")
        continue

    if os.path.isdir("D:\\"):
        lokasi_backup = "D:\\"
        print("ada")
    else:
        lokasi_backup = os.path.join(os.path.expanduser("~"), "Documents")
        print(lokasi_backup)

    path_backup = os.path.join(lokasi_backup, nama_backup)
    print(path_backup)

    try:
        os.makedirs(path_backup)
        print("folder backup berhasil dibuat")
    except FileExistsError:
        print("peringatan: folder backup hari ini sudah ada")

        pilihan = input("lanjut atau berhenti: ") .lower()
        if pilihan == "berhenti":
            continue
    jumlah_file_level_1 = 0
    jumlah_file_subfolder = 0
    for i in os.listdir(jalan):
        path_file_asli = os.path.join(jalan, i)
        if os.path.isfile(path_file_asli):
            shutil.copy(path_file_asli, path_backup)
            jumlah_file_level_1 += 1
        elif os.path.isdir(path_file_asli):
            tujuan = os.path.join(path_backup, i)
            if os.path.exists(tujuan):
                shutil.rmtree(tujuan)
            shutil.copytree(path_file_asli, tujuan)
            for root, dirs, files in os.walk(tujuan):
                jumlah_file_subfolder += len(files)
    total_file = jumlah_file_level_1 + jumlah_file_subfolder
    print(f"Backup dari {jalan} selesai")
    print(f"Total file di folder : {total_file}")
    print(f"File di dalam subfolder : {jumlah_file_subfolder}")
            
            